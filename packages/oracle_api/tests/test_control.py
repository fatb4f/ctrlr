from __future__ import annotations

from oracle_api.control import CtrlrError, ensure, invariant, require


def test_control_gates_pass():
    require(True, "ok")
    ensure(True, "ok")
    invariant(True, "ok")


def test_control_gate_failure_includes_data():
    data = {"key": "value"}
    try:
        require(False, "nope", data)
    except CtrlrError as exc:
        message = str(exc)
        assert "nope" in message
        assert "key" in message
        assert "value" in message
    else:
        raise AssertionError("expected CtrlrError")
