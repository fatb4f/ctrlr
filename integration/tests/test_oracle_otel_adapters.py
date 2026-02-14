from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
ORACLE_SRC = ROOT / "packages" / "oracle" / "src"
SCHEMA_CONTRACT_PATH = ROOT / "docs" / "otel_migration" / "schema_contract.json"
if str(ORACLE_SRC) not in sys.path:
    sys.path.insert(0, str(ORACLE_SRC))

from oracle import OTelRuntime, materialize_dsa_steps
from oracle.adapters import (
    emit_birdseye_trace,
    emit_coverage_summary,
    emit_hunter_events,
    emit_pytest_hypothesis_case,
    emit_snoop_trace,
    emit_viztracer_trace,
)


def _load_schema_contract() -> dict:
    return json.loads(SCHEMA_CONTRACT_PATH.read_text(encoding="utf-8"))


def _assert_span_contract(contract: dict, attrs: dict) -> None:
    for key in contract["span"]["required_attributes"]:
        assert key in attrs, f"missing span key {key}"
    for one_of in contract["span"]["required_one_of"]:
        assert any(key in attrs for key in one_of), f"missing one_of keys: {one_of}"


def _assert_schema_events(contract: dict, span_event_map: dict[str, dict]) -> None:
    for event_name in ("oracle.guard", "oracle.invariant", "oracle.explanation"):
        attrs = span_event_map[event_name]
        event_contract = contract["events"][event_name]
        for key in event_contract["required_attributes"]:
            assert key in attrs, f"missing {event_name} key {key}"
        for enum_key, allowed_values in event_contract["enums"].items():
            assert attrs[enum_key] in allowed_values


def _event_attrs(span, event_name: str) -> dict:
    for event in span.events:
        if event.name == event_name:
            return event.attributes
    raise AssertionError(f"missing event: {event_name}")


def test_pytest_hypothesis_adapter_emits_correlated_events() -> None:
    contract = _load_schema_contract()
    rt = OTelRuntime.from_env({"OTEL_TRACES_EXPORTER": "none"})
    rt.set_provenance_file("integration/tests/test_oracle_otel_adapters.py", 1)

    step = emit_pytest_hypothesis_case(
        rt,
        run_id="run-m3-pytest",
        seq=10,
        nodeid="tests/test_demo.py::test_case",
        outcome="fail",
        hypothesis_example={"n": 2},
        failure_message="assert 2 == 3",
        run_label="baseline",
    )

    _assert_span_contract(contract, step.attributes)
    case_event = _event_attrs(step, "oracle.pytest.case")
    assert case_event["oracle.run_id"] == "run-m3-pytest"
    assert case_event["oracle.step_id"] == "pytest:tests/test_demo.py::test_case"
    _assert_schema_events(contract, {e.name: e.attributes for e in step.events})

    materialized = materialize_dsa_steps(rt.spans)
    assert materialized["steps"][0]["seq"] == 10
    assert materialized["steps"][0]["run_id"] == "run-m3-pytest"
    assert materialized["steps"][0]["guards"][0]["status"] == "fail"


def test_snoop_birdseye_adapter_path_emits_correlated_events() -> None:
    contract = _load_schema_contract()
    rt = OTelRuntime.from_env({"OTEL_TRACES_EXPORTER": "none"})
    rt.set_provenance_cell("marimo-nb-01", "cell-5")

    snoop_step = emit_snoop_trace(
        rt,
        run_id="run-m3-introspection",
        seq=20,
        records=[
            {"seq": 1, "message": "x=1", "filepath": "algo.py", "lineno": 10},
            {"seq": 2, "message": "x=2", "filepath": "algo.py", "lineno": 11},
        ],
        run_label="variant-a",
    )
    birdseye_step = emit_birdseye_trace(
        rt,
        run_id="run-m3-introspection",
        seq=21,
        frames=[{"module": "algo", "function": "step", "filepath": "algo.py", "lineno": 22}],
        run_label="variant-a",
    )

    _assert_span_contract(contract, snoop_step.attributes)
    _assert_span_contract(contract, birdseye_step.attributes)
    assert _event_attrs(snoop_step, "oracle.snoop.event")["oracle.run_id"] == "run-m3-introspection"
    assert _event_attrs(birdseye_step, "oracle.birdseye.frame")["oracle.run_id"] == "run-m3-introspection"
    _assert_schema_events(contract, {e.name: e.attributes for e in snoop_step.events})
    _assert_schema_events(contract, {e.name: e.attributes for e in birdseye_step.events})

    materialized = materialize_dsa_steps(rt.spans)
    assert [step["seq"] for step in materialized["steps"]] == [20, 21]
    assert materialized["steps"][0]["provenance"]["oracle.notebook_id"] == "marimo-nb-01"


def test_hunter_viztracer_adapter_path_emits_correlated_events() -> None:
    contract = _load_schema_contract()
    rt = OTelRuntime.from_env({"OTEL_TRACES_EXPORTER": "none"})

    hunter_step = emit_hunter_events(
        rt,
        run_id="run-m3-trace",
        seq=30,
        events=[{"kind": "call", "function": "dfs", "filepath": "algo.py", "lineno": 44}],
        run_label="trace",
    )
    viz_step = emit_viztracer_trace(
        rt,
        run_id="run-m3-trace",
        seq=31,
        records=[{"name": "dfs", "duration_us": 180, "start_us": 1000}],
        run_label="trace",
    )

    _assert_span_contract(contract, hunter_step.attributes)
    _assert_span_contract(contract, viz_step.attributes)
    assert _event_attrs(hunter_step, "oracle.hunter.event")["oracle.step_id"] == "hunter.trace"
    assert _event_attrs(viz_step, "oracle.viztracer.event")["oracle.step_id"] == "viztracer.trace"
    _assert_schema_events(contract, {e.name: e.attributes for e in hunter_step.events})
    _assert_schema_events(contract, {e.name: e.attributes for e in viz_step.events})

    materialized = materialize_dsa_steps(rt.spans)
    assert materialized["steps"][0]["adapter_source"] == "hunter"
    assert materialized["steps"][1]["adapter_source"] == "viztracer"


def test_coverage_pytest_cov_adapter_path_emits_correlated_events() -> None:
    contract = _load_schema_contract()
    rt = OTelRuntime.from_env({"OTEL_TRACES_EXPORTER": "none"})

    step = emit_coverage_summary(
        rt,
        run_id="run-m3-coverage",
        seq=40,
        covered_lines=96,
        total_lines=120,
        source="pytest-cov",
        threshold_percent=70.0,
        run_label="coverage",
    )

    _assert_span_contract(contract, step.attributes)
    summary_event = _event_attrs(step, "oracle.coverage.summary")
    assert summary_event["oracle.run_id"] == "run-m3-coverage"
    assert summary_event["oracle.coverage.percent"] == 80.0
    _assert_schema_events(contract, {e.name: e.attributes for e in step.events})

    materialized = materialize_dsa_steps(rt.spans)
    assert materialized["steps"][0]["seq"] == 40
    assert materialized["steps"][0]["invariants"][0]["status"] == "pass"
