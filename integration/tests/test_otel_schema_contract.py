from __future__ import annotations

import json
from pathlib import Path

import pytest


CONTRACT_PATH = Path("docs/otel_migration/schema_contract.json")


def _load_contract() -> dict:
    return json.loads(CONTRACT_PATH.read_text(encoding="utf-8"))


def _validate_span(contract: dict, attributes: dict) -> None:
    required = contract["span"]["required_attributes"]
    for key in required:
        assert key in attributes, f"missing required span attribute: {key}"

    for group in contract["span"]["required_one_of"]:
        assert any(key in attributes for key in group), (
            "missing required one-of span attributes: " + ", ".join(group)
        )


def _validate_event(contract: dict, name: str, attributes: dict) -> None:
    event_contract = contract["events"][name]

    for key in event_contract["required_attributes"]:
        assert key in attributes, f"missing required event attribute {key} for {name}"

    for enum_key, allowed_values in event_contract["enums"].items():
        if enum_key in attributes:
            assert attributes[enum_key] in allowed_values, (
                f"invalid enum for {enum_key}: {attributes[enum_key]}"
            )


def test_contract_file_exists() -> None:
    assert CONTRACT_PATH.exists(), f"missing contract file: {CONTRACT_PATH}"


def test_minimal_valid_payload_passes() -> None:
    contract = _load_contract()

    span_attrs = {
        "oracle.evidence.schema_version": "1.0.0",
        "oracle.run_id": "run-001",
        "oracle.seq": 1,
        "oracle.run_label": "baseline",
        "code.filepath": "packages/oracle_otel/runtime.py",
        "code.lineno": 42,
        "oracle.notebook_id": "nb-01",
        "oracle.cell_id": "cell-01",
    }
    _validate_span(contract, span_attrs)

    _validate_event(
        contract,
        "oracle.guard",
        {"oracle.guard.condition": "n > 0", "oracle.guard.status": "pass"},
    )
    _validate_event(
        contract,
        "oracle.invariant",
        {
            "oracle.invariant.id": "inv_size",
            "oracle.invariant.statement": "size == len(items)",
            "oracle.invariant.status": "pass",
        },
    )
    _validate_event(
        contract,
        "oracle.explanation",
        {"oracle.explanation.text": "transition is safe"},
    )


@pytest.mark.parametrize(
    "bad_span",
    [
        {
            "oracle.evidence.schema_version": "1.0.0",
            "oracle.seq": 1,
            "oracle.run_label": "baseline",
        },
        {
            "oracle.evidence.schema_version": "1.0.0",
            "oracle.run_id": "run-001",
            "oracle.seq": 1,
        },
    ],
)
def test_span_validation_fails_on_missing_required_keys(bad_span: dict) -> None:
    contract = _load_contract()
    with pytest.raises(AssertionError):
        _validate_span(contract, bad_span)


def test_event_validation_fails_on_invalid_enum() -> None:
    contract = _load_contract()
    with pytest.raises(AssertionError):
        _validate_event(
            contract,
            "oracle.guard",
            {"oracle.guard.condition": "n > 0", "oracle.guard.status": "unknown"},
        )
