from __future__ import annotations

from typing import Any


class CtrlrError(RuntimeError):
    def __init__(self, message: str, data: dict[str, Any] | None = None) -> None:
        self.data = data
        super().__init__(self._format(message, data))

    @staticmethod
    def _format(message: str, data: dict[str, Any] | None) -> str:
        if data is None:
            return message
        return f"{message} | data={data!r}"


def _emit_failure_step(kind: str, message: str, data: dict[str, Any] | None) -> None:
    try:
        from .trace import current_lens, step

        lens = current_lens()
        if lens is None:
            return
        step(name=kind, lens=lens, ok=False, data={"message": message, "data": data})
    except Exception:
        return


def require(cond: bool, message: str, data: dict[str, Any] | None = None) -> None:
    if cond:
        return
    _emit_failure_step("require", message, data)
    raise CtrlrError(message, data)


def ensure(cond: bool, message: str, data: dict[str, Any] | None = None) -> None:
    if cond:
        return
    _emit_failure_step("ensure", message, data)
    raise CtrlrError(message, data)


def invariant(cond: bool, message: str, data: dict[str, Any] | None = None) -> None:
    if cond:
        return
    _emit_failure_step("invariant", message, data)
    raise CtrlrError(message, data)
