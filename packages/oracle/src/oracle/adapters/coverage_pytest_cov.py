from __future__ import annotations

from oracle.otel_runtime import OTelRuntime, SpanRecord


_VALID_SOURCES = {"coverage", "pytest-cov"}


def emit_coverage_summary(
    runtime: OTelRuntime,
    *,
    run_id: str,
    seq: int,
    covered_lines: int,
    total_lines: int,
    source: str = "coverage",
    threshold_percent: float | None = None,
    variant_id: str | None = None,
    run_label: str | None = None,
    step_id: str = "coverage.summary",
) -> SpanRecord:
    if source not in _VALID_SOURCES:
        raise ValueError(f"invalid coverage source: {source}")
    if covered_lines < 0 or total_lines < 0:
        raise ValueError("coverage values must be non-negative")
    if covered_lines > total_lines:
        raise ValueError("covered_lines cannot exceed total_lines")

    percent = 0.0 if total_lines == 0 else round((covered_lines / total_lines) * 100.0, 4)

    with runtime.step_span(
        run_id=run_id,
        step_id=step_id,
        seq=seq,
        variant_id=variant_id,
        run_label=run_label,
        attributes={
            "oracle.adapter.family": "coverage+pytest-cov",
            "oracle.adapter.source": source,
        },
    ) as span:
        runtime.emit_event(
            "oracle.coverage.summary",
            {
                "oracle.run_id": run_id,
                "oracle.step_id": step_id,
                "oracle.adapter.seq": seq,
                "oracle.coverage.covered_lines": covered_lines,
                "oracle.coverage.total_lines": total_lines,
                "oracle.coverage.percent": percent,
            },
        )

        guard_status = "pass"
        if total_lines == 0:
            guard_status = "skip"
        if threshold_percent is not None and total_lines > 0 and percent < threshold_percent:
            guard_status = "fail"
        runtime.emit_guard("coverage.percent >= threshold", guard_status)
        runtime.emit_invariant(
            "coverage.percent.range",
            "0 <= coverage.percent <= 100",
            "pass" if 0.0 <= percent <= 100.0 else "fail",
        )
        runtime.emit_explanation(f"{source} coverage: {percent:.2f}%")
        return span
