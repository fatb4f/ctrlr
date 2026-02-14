from __future__ import annotations

from contextlib import contextmanager
from contextvars import ContextVar
from dataclasses import dataclass, field
from typing import Any, Mapping

import os


_VALID_STATUS = {"pass", "fail", "skip"}
_SCHEMA_VERSION = "1.0.0"


@dataclass(frozen=True)
class OTelConfig:
    service_name: str
    traces_exporter: str
    otlp_endpoint: str | None
    resource_attributes: dict[str, str]


@dataclass
class EventRecord:
    name: str
    attributes: dict[str, Any] = field(default_factory=dict)


@dataclass
class SpanRecord:
    name: str
    attributes: dict[str, Any] = field(default_factory=dict)
    events: list[EventRecord] = field(default_factory=list)


def _parse_resource_attributes(raw: str | None) -> dict[str, str]:
    if not raw:
        return {}
    out: dict[str, str] = {}
    for item in raw.split(","):
        pair = item.strip()
        if not pair:
            continue
        if "=" not in pair:
            continue
        key, value = pair.split("=", 1)
        out[key.strip()] = value.strip()
    return out


def load_otel_config(env: Mapping[str, str] | None = None) -> OTelConfig:
    source = env if env is not None else os.environ
    traces_exporter = source.get("OTEL_TRACES_EXPORTER", "none").strip().lower() or "none"
    if traces_exporter not in {"none", "console", "otlp"}:
        raise ValueError(f"unsupported OTEL_TRACES_EXPORTER: {traces_exporter}")

    service_name = source.get("OTEL_SERVICE_NAME", "oracle").strip() or "oracle"
    endpoint = source.get("OTEL_EXPORTER_OTLP_ENDPOINT")
    endpoint = endpoint.strip() if isinstance(endpoint, str) and endpoint.strip() else None
    resource_attributes = _parse_resource_attributes(source.get("OTEL_RESOURCE_ATTRIBUTES"))

    if "service.name" not in resource_attributes:
        resource_attributes["service.name"] = service_name

    return OTelConfig(
        service_name=service_name,
        traces_exporter=traces_exporter,
        otlp_endpoint=endpoint,
        resource_attributes=resource_attributes,
    )


class OTelRuntime:
    _active_spans: ContextVar[tuple[SpanRecord, ...]] = ContextVar("oracle_active_spans", default=())
    _provenance: ContextVar[dict[str, Any] | None] = ContextVar("oracle_provenance", default=None)

    def __init__(self, config: OTelConfig):
        self.config = config
        self.spans: list[SpanRecord] = []
        self._otel_enabled = False
        self._otel_error: str | None = None
        self._tracer = None
        self._configure_otel()

    @classmethod
    def from_env(cls, env: Mapping[str, str] | None = None) -> OTelRuntime:
        return cls(load_otel_config(env))

    @property
    def otel_enabled(self) -> bool:
        return self._otel_enabled

    @property
    def otel_error(self) -> str | None:
        return self._otel_error

    def _configure_otel(self) -> None:
        if self.config.traces_exporter == "none":
            return

        try:
            from opentelemetry import trace
            from opentelemetry.sdk.resources import Resource
            from opentelemetry.sdk.trace import TracerProvider
            from opentelemetry.sdk.trace.export import BatchSpanProcessor, ConsoleSpanExporter
        except Exception as exc:  # pragma: no cover - optional dependency path
            self._otel_error = f"otel import unavailable: {exc}"
            return

        provider = TracerProvider(resource=Resource.create(self.config.resource_attributes))
        processor = None

        if self.config.traces_exporter == "console":
            processor = BatchSpanProcessor(ConsoleSpanExporter())
        elif self.config.traces_exporter == "otlp":
            exporter = None
            kwargs: dict[str, Any] = {}
            if self.config.otlp_endpoint:
                kwargs["endpoint"] = self.config.otlp_endpoint
            try:
                from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter

                exporter = OTLPSpanExporter(**kwargs)
            except Exception:
                try:
                    from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter

                    exporter = OTLPSpanExporter(**kwargs)
                except Exception as exc:  # pragma: no cover - optional dependency path
                    self._otel_error = f"otlp exporter unavailable: {exc}"
                    return
            processor = BatchSpanProcessor(exporter)

        if processor is not None:
            provider.add_span_processor(processor)
            trace.set_tracer_provider(provider)
            self._tracer = trace.get_tracer("oracle.otel_runtime")
            self._otel_enabled = True

    def _merged_with_provenance(self, attrs: dict[str, Any] | None = None) -> dict[str, Any]:
        out = dict(attrs or {})
        provenance = self._provenance.get() or {}
        for key, value in provenance.items():
            out.setdefault(key, value)
        return out

    def _current_span(self) -> SpanRecord | None:
        stack = self._active_spans.get()
        if not stack:
            return None
        return stack[-1]

    @contextmanager
    def _open_span(self, name: str, attributes: dict[str, Any]):
        span_record = SpanRecord(name=name, attributes=dict(attributes))
        stack = self._active_spans.get()
        token = self._active_spans.set(stack + (span_record,))

        otel_cm = None
        if self._otel_enabled and self._tracer is not None:
            otel_cm = self._tracer.start_as_current_span(name)
            otel_span = otel_cm.__enter__()
            for key, value in attributes.items():
                otel_span.set_attribute(key, value)

        try:
            yield span_record
        finally:
            if otel_cm is not None:
                otel_cm.__exit__(None, None, None)
            self.spans.append(span_record)
            self._active_spans.reset(token)

    @contextmanager
    def run_span(
        self,
        *,
        run_id: str,
        seq: int = 0,
        variant_id: str | None = None,
        run_label: str | None = None,
        attributes: dict[str, Any] | None = None,
    ):
        span_attrs: dict[str, Any] = {
            "oracle.evidence.schema_version": _SCHEMA_VERSION,
            "oracle.run_id": run_id,
            "oracle.seq": seq,
        }
        if variant_id:
            span_attrs["oracle.variant_id"] = variant_id
        if run_label:
            span_attrs["oracle.run_label"] = run_label
        span_attrs.update(attributes or {})
        span_attrs = self._merged_with_provenance(span_attrs)
        with self._open_span("oracle.run", span_attrs) as span_record:
            yield span_record

    @contextmanager
    def step_span(
        self,
        *,
        run_id: str,
        step_id: str,
        seq: int,
        variant_id: str | None = None,
        run_label: str | None = None,
        attributes: dict[str, Any] | None = None,
    ):
        span_attrs: dict[str, Any] = {
            "oracle.evidence.schema_version": _SCHEMA_VERSION,
            "oracle.run_id": run_id,
            "oracle.step_id": step_id,
            "oracle.seq": seq,
        }
        if variant_id:
            span_attrs["oracle.variant_id"] = variant_id
        if run_label:
            span_attrs["oracle.run_label"] = run_label
        span_attrs.update(attributes or {})
        span_attrs = self._merged_with_provenance(span_attrs)
        with self._open_span("oracle.step", span_attrs) as span_record:
            yield span_record

    def set_provenance_file(self, filepath: str, lineno: int) -> None:
        current = dict(self._provenance.get() or {})
        current["code.filepath"] = filepath
        current["code.lineno"] = lineno
        self._provenance.set(current)

    def set_provenance_cell(self, notebook_id: str, cell_id: str) -> None:
        current = dict(self._provenance.get() or {})
        current["oracle.notebook_id"] = notebook_id
        current["oracle.cell_id"] = cell_id
        self._provenance.set(current)

    def _emit_event(self, name: str, attributes: dict[str, Any]) -> None:
        span = self._current_span()
        if span is None:
            raise RuntimeError("no active span")
        merged = self._merged_with_provenance(attributes)
        span.events.append(EventRecord(name=name, attributes=merged))

        if self._otel_enabled:  # pragma: no cover - requires optional dependency
            from opentelemetry import trace

            current = trace.get_current_span()
            current.add_event(name, merged)

    def emit_event(self, name: str, attributes: dict[str, Any]) -> None:
        self._emit_event(name, attributes)

    def emit_guard(self, condition: str, status: str) -> None:
        if status not in _VALID_STATUS:
            raise ValueError(f"invalid guard status: {status}")
        self._emit_event(
            "oracle.guard",
            {
                "oracle.guard.condition": condition,
                "oracle.guard.status": status,
            },
        )

    def emit_invariant(self, invariant_id: str, statement: str, status: str) -> None:
        if status not in _VALID_STATUS:
            raise ValueError(f"invalid invariant status: {status}")
        self._emit_event(
            "oracle.invariant",
            {
                "oracle.invariant.id": invariant_id,
                "oracle.invariant.statement": statement,
                "oracle.invariant.status": status,
            },
        )

    def emit_explanation(self, text: str) -> None:
        self._emit_event("oracle.explanation", {"oracle.explanation.text": text})
