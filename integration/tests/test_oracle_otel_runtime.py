from __future__ import annotations

import importlib.util
import inspect
import json
import sys
from pathlib import Path

import pytest


ROOT = Path(__file__).resolve().parents[2]
MODULE_PATH = ROOT / "packages" / "oracle" / "src" / "oracle" / "otel_runtime.py"
SCHEMA_CONTRACT_PATH = ROOT / "docs" / "otel_migration" / "schema_contract.json"


def _load_runtime_module():
    spec = importlib.util.spec_from_file_location("oracle_otel_runtime", MODULE_PATH)
    assert spec is not None and spec.loader is not None
    mod = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = mod
    spec.loader.exec_module(mod)
    return mod


def _load_schema_contract() -> dict:
    return json.loads(SCHEMA_CONTRACT_PATH.read_text(encoding="utf-8"))


def _assert_span_matches_contract(contract: dict, attrs: dict) -> None:
    for key in contract["span"]["required_attributes"]:
        assert key in attrs, f"missing span key {key}"
    for group in contract["span"]["required_one_of"]:
        assert any(key in attrs for key in group), f"missing one_of keys: {group}"


def _assert_event_matches_contract(contract: dict, event_name: str, attrs: dict) -> None:
    event_contract = contract["events"][event_name]
    for key in event_contract["required_attributes"]:
        assert key in attrs, f"missing event key {key}"
    for enum_key, allowed in event_contract["enums"].items():
        assert attrs[enum_key] in allowed, f"invalid enum for {enum_key}"


def test_load_otel_config_from_env() -> None:
    runtime = _load_runtime_module()
    cfg = runtime.load_otel_config(
        {
            "OTEL_SERVICE_NAME": "oracle-m2",
            "OTEL_TRACES_EXPORTER": "otlp",
            "OTEL_EXPORTER_OTLP_ENDPOINT": "http://localhost:4318",
            "OTEL_RESOURCE_ATTRIBUTES": "deployment.environment=dev,service.namespace=oracle",
        }
    )
    assert cfg.service_name == "oracle-m2"
    assert cfg.traces_exporter == "otlp"
    assert cfg.otlp_endpoint == "http://localhost:4318"
    assert cfg.resource_attributes["deployment.environment"] == "dev"
    assert cfg.resource_attributes["service.namespace"] == "oracle"
    assert cfg.resource_attributes["service.name"] == "oracle-m2"


def test_runtime_emits_schema_compatible_spans_and_events() -> None:
    runtime_mod = _load_runtime_module()
    contract = _load_schema_contract()

    rt = runtime_mod.OTelRuntime.from_env({"OTEL_TRACES_EXPORTER": "none"})
    rt.set_provenance_file("packages/oracle/src/oracle/otel_runtime.py", 123)
    rt.set_provenance_cell("nb-m2", "cell-1")

    with rt.run_span(run_id="run-001", run_label="baseline"):
        with rt.step_span(run_id="run-001", step_id="step-1", seq=1, run_label="baseline"):
            rt.emit_guard("n > 0", "pass")
            rt.emit_invariant("inv_size", "size == len(items)", "pass")
            rt.emit_explanation("transition is safe")

    assert len(rt.spans) == 2
    step_span = next(span for span in rt.spans if span.name == "oracle.step")
    _assert_span_matches_contract(contract, step_span.attributes)
    assert step_span.attributes["code.filepath"] == "packages/oracle/src/oracle/otel_runtime.py"
    assert step_span.attributes["code.lineno"] == 123
    assert step_span.attributes["oracle.notebook_id"] == "nb-m2"
    assert step_span.attributes["oracle.cell_id"] == "cell-1"

    by_name = {e.name: e.attributes for e in step_span.events}
    _assert_event_matches_contract(contract, "oracle.guard", by_name["oracle.guard"])
    _assert_event_matches_contract(contract, "oracle.invariant", by_name["oracle.invariant"])
    _assert_event_matches_contract(contract, "oracle.explanation", by_name["oracle.explanation"])


def test_event_status_enums_are_enforced() -> None:
    runtime_mod = _load_runtime_module()
    rt = runtime_mod.OTelRuntime.from_env({"OTEL_TRACES_EXPORTER": "none"})
    with rt.run_span(run_id="run-001", run_label="baseline"):
        with rt.step_span(run_id="run-001", step_id="step-1", seq=1, run_label="baseline"):
            with pytest.raises(ValueError):
                rt.emit_guard("n > 0", "maybe")
            with pytest.raises(ValueError):
                rt.emit_invariant("inv", "x", "unknown")


def test_runtime_module_has_no_legacy_runtime_imports() -> None:
    runtime_mod = _load_runtime_module()
    source = inspect.getsource(runtime_mod)
    assert "oracle_api" not in source
    assert "oracle_tools" not in source
