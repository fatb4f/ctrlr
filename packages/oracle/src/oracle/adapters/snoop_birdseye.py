from __future__ import annotations

from typing import Any, Mapping, Sequence

from oracle.otel_runtime import OTelRuntime, SpanRecord


def _event_seq(record: Mapping[str, Any], fallback: int) -> int:
    raw = record.get("seq", fallback)
    try:
        return int(raw)
    except (TypeError, ValueError):
        return fallback


def _is_monotonic(values: Sequence[int]) -> bool:
    if not values:
        return True
    for idx in range(1, len(values)):
        if values[idx] < values[idx - 1]:
            return False
    return True


def emit_snoop_trace(
    runtime: OTelRuntime,
    *,
    run_id: str,
    seq: int,
    records: Sequence[Mapping[str, Any]],
    variant_id: str | None = None,
    run_label: str | None = None,
    step_id: str = "snoop.trace",
) -> SpanRecord:
    with runtime.step_span(
        run_id=run_id,
        step_id=step_id,
        seq=seq,
        variant_id=variant_id,
        run_label=run_label,
        attributes={
            "oracle.adapter.family": "snoop+birdseye",
            "oracle.adapter.source": "snoop",
            "oracle.snoop.count": len(records),
        },
    ) as span:
        seq_values: list[int] = []
        for idx, record in enumerate(records, start=1):
            record_seq = _event_seq(record, idx)
            seq_values.append(record_seq)
            runtime.emit_event(
                "oracle.snoop.event",
                {
                    "oracle.run_id": run_id,
                    "oracle.step_id": step_id,
                    "oracle.adapter.seq": record_seq,
                    "oracle.snoop.message": str(record.get("message", "")),
                    "code.filepath": str(record.get("filepath", "")),
                    "code.lineno": int(record.get("lineno", 0) or 0),
                },
            )

        guard_status = "pass" if records else "skip"
        invariant_status = "pass" if _is_monotonic(seq_values) else "fail"
        runtime.emit_guard("snoop.records > 0", guard_status)
        runtime.emit_invariant("snoop.seq.monotonic", "snoop sequence is monotonic", invariant_status)
        runtime.emit_explanation(f"snoop records materialized: {len(records)}")
        return span


def emit_birdseye_trace(
    runtime: OTelRuntime,
    *,
    run_id: str,
    seq: int,
    frames: Sequence[Mapping[str, Any]],
    variant_id: str | None = None,
    run_label: str | None = None,
    step_id: str = "birdseye.trace",
) -> SpanRecord:
    with runtime.step_span(
        run_id=run_id,
        step_id=step_id,
        seq=seq,
        variant_id=variant_id,
        run_label=run_label,
        attributes={
            "oracle.adapter.family": "snoop+birdseye",
            "oracle.adapter.source": "birdseye",
            "oracle.birdseye.count": len(frames),
        },
    ) as span:
        for idx, frame in enumerate(frames, start=1):
            runtime.emit_event(
                "oracle.birdseye.frame",
                {
                    "oracle.run_id": run_id,
                    "oracle.step_id": step_id,
                    "oracle.adapter.seq": idx,
                    "oracle.birdseye.module": str(frame.get("module", "")),
                    "oracle.birdseye.function": str(frame.get("function", "")),
                    "code.filepath": str(frame.get("filepath", "")),
                    "code.lineno": int(frame.get("lineno", 0) or 0),
                },
            )

        guard_status = "pass" if frames else "skip"
        runtime.emit_guard("birdseye.frames > 0", guard_status)
        runtime.emit_invariant(
            "birdseye.frame.identity",
            "birdseye frames include module+function identity",
            "pass" if all(frame.get("function") for frame in frames) else "fail",
        )
        runtime.emit_explanation(f"birdseye frames materialized: {len(frames)}")
        return span
