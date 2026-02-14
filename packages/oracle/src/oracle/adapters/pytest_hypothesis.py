from __future__ import annotations

import json
from typing import Any, Mapping

from oracle.otel_runtime import OTelRuntime, SpanRecord


_VALID_CASE_OUTCOMES = {"pass", "fail", "skip"}


def _normalize_example(example: Mapping[str, Any] | None) -> str | None:
    if example is None:
        return None
    return json.dumps(example, sort_keys=True, separators=(",", ":"))


def emit_pytest_hypothesis_case(
    runtime: OTelRuntime,
    *,
    run_id: str,
    seq: int,
    nodeid: str,
    outcome: str,
    hypothesis_example: Mapping[str, Any] | None = None,
    failure_message: str | None = None,
    variant_id: str | None = None,
    run_label: str | None = None,
    step_id: str | None = None,
) -> SpanRecord:
    if outcome not in _VALID_CASE_OUTCOMES:
        raise ValueError(f"invalid test outcome: {outcome}")

    resolved_step_id = step_id or f"pytest:{nodeid}"
    source = "pytest+hypothesis" if hypothesis_example is not None else "pytest"
    span_attrs = {
        "oracle.adapter.family": "pytest+hypothesis",
        "oracle.adapter.source": source,
        "oracle.pytest.nodeid": nodeid,
    }

    with runtime.step_span(
        run_id=run_id,
        step_id=resolved_step_id,
        seq=seq,
        variant_id=variant_id,
        run_label=run_label,
        attributes=span_attrs,
    ) as span:
        case_event = {
            "oracle.run_id": run_id,
            "oracle.step_id": resolved_step_id,
            "oracle.pytest.nodeid": nodeid,
            "oracle.pytest.outcome": outcome,
            "oracle.adapter.seq": seq,
        }
        example_json = _normalize_example(hypothesis_example)
        if example_json is not None:
            case_event["oracle.hypothesis.example"] = example_json
        if failure_message:
            case_event["oracle.pytest.failure_message"] = failure_message
        runtime.emit_event("oracle.pytest.case", case_event)

        guard_status = "pass" if outcome == "pass" else "skip" if outcome == "skip" else "fail"
        runtime.emit_guard("oracle.pytest.outcome == pass", guard_status)
        runtime.emit_invariant(
            "pytest.case.identity",
            "pytest case nodeid is non-empty",
            "pass" if bool(nodeid.strip()) else "fail",
        )
        runtime.emit_explanation(f"{nodeid} outcome: {outcome}")
        return span
