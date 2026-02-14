from __future__ import annotations

from typing import Any, Mapping, Sequence

from oracle.otel_runtime import OTelRuntime, SpanRecord


def emit_hunter_events(
    runtime: OTelRuntime,
    *,
    run_id: str,
    seq: int,
    events: Sequence[Mapping[str, Any]],
    variant_id: str | None = None,
    run_label: str | None = None,
    step_id: str = "hunter.trace",
) -> SpanRecord:
    with runtime.step_span(
        run_id=run_id,
        step_id=step_id,
        seq=seq,
        variant_id=variant_id,
        run_label=run_label,
        attributes={
            "oracle.adapter.family": "hunter+viztracer",
            "oracle.adapter.source": "hunter",
            "oracle.hunter.count": len(events),
        },
    ) as span:
        for idx, event in enumerate(events, start=1):
            runtime.emit_event(
                "oracle.hunter.event",
                {
                    "oracle.run_id": run_id,
                    "oracle.step_id": step_id,
                    "oracle.adapter.seq": idx,
                    "oracle.hunter.kind": str(event.get("kind", "")),
                    "oracle.hunter.function": str(event.get("function", "")),
                    "code.filepath": str(event.get("filepath", "")),
                    "code.lineno": int(event.get("lineno", 0) or 0),
                },
            )

        guard_status = "pass" if events else "skip"
        invariant_status = "pass" if all(e.get("function") for e in events) else "fail"
        runtime.emit_guard("hunter.events > 0", guard_status)
        runtime.emit_invariant(
            "hunter.call.identity",
            "hunter events include function identity",
            invariant_status,
        )
        runtime.emit_explanation(f"hunter events materialized: {len(events)}")
        return span


def emit_viztracer_trace(
    runtime: OTelRuntime,
    *,
    run_id: str,
    seq: int,
    records: Sequence[Mapping[str, Any]],
    variant_id: str | None = None,
    run_label: str | None = None,
    step_id: str = "viztracer.trace",
) -> SpanRecord:
    with runtime.step_span(
        run_id=run_id,
        step_id=step_id,
        seq=seq,
        variant_id=variant_id,
        run_label=run_label,
        attributes={
            "oracle.adapter.family": "hunter+viztracer",
            "oracle.adapter.source": "viztracer",
            "oracle.viztracer.count": len(records),
        },
    ) as span:
        for idx, record in enumerate(records, start=1):
            runtime.emit_event(
                "oracle.viztracer.event",
                {
                    "oracle.run_id": run_id,
                    "oracle.step_id": step_id,
                    "oracle.adapter.seq": idx,
                    "oracle.viztracer.name": str(record.get("name", "")),
                    "oracle.viztracer.duration_us": int(record.get("duration_us", 0) or 0),
                    "oracle.viztracer.start_us": int(record.get("start_us", 0) or 0),
                },
            )

        guard_status = "pass" if records else "skip"
        invariant_status = "pass"
        for record in records:
            duration_us = int(record.get("duration_us", 0) or 0)
            if duration_us < 0:
                invariant_status = "fail"
                break
        runtime.emit_guard("viztracer.records > 0", guard_status)
        runtime.emit_invariant(
            "viztracer.duration.non_negative",
            "viztracer durations are non-negative",
            invariant_status,
        )
        runtime.emit_explanation(f"viztracer records materialized: {len(records)}")
        return span
