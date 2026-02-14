from __future__ import annotations

from typing import Any, Iterable

from oracle.otel_runtime import SpanRecord


def _to_int(value: Any, default: int = 0) -> int:
    try:
        return int(value)
    except (TypeError, ValueError):
        return default


def materialize_dsa_steps(spans: Iterable[SpanRecord]) -> dict[str, Any]:
    ordered = sorted((span for span in spans if span.name == "oracle.step"), key=lambda s: _to_int(s.attributes.get("oracle.seq")))
    steps: list[dict[str, Any]] = []

    for span in ordered:
        guards: list[dict[str, Any]] = []
        invariants: list[dict[str, Any]] = []
        for event in span.events:
            attrs = event.attributes
            if event.name == "oracle.guard":
                guards.append(
                    {
                        "condition": attrs.get("oracle.guard.condition"),
                        "status": attrs.get("oracle.guard.status"),
                    }
                )
            elif event.name == "oracle.invariant":
                invariants.append(
                    {
                        "id": attrs.get("oracle.invariant.id"),
                        "statement": attrs.get("oracle.invariant.statement"),
                        "status": attrs.get("oracle.invariant.status"),
                    }
                )

        provenance = {}
        for key in ("code.filepath", "code.lineno", "oracle.notebook_id", "oracle.cell_id"):
            if key in span.attributes:
                provenance[key] = span.attributes[key]

        steps.append(
            {
                "run_id": span.attributes.get("oracle.run_id"),
                "step_id": span.attributes.get("oracle.step_id"),
                "seq": _to_int(span.attributes.get("oracle.seq")),
                "adapter_family": span.attributes.get("oracle.adapter.family"),
                "adapter_source": span.attributes.get("oracle.adapter.source"),
                "guards": guards,
                "invariants": invariants,
                "provenance": provenance,
            }
        )

    return {"steps": steps}
