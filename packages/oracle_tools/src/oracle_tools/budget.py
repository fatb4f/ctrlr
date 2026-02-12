from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from oracle_api.control import CtrlrError, ensure


@dataclass
class Budget:
    limit: int
    used: int = 0
    label: str | None = None
    data: dict[str, Any] | None = None

    @property
    def remaining(self) -> int:
        return max(self.limit - self.used, 0)

    def consume(self, amount: int = 1, data: dict[str, Any] | None = None) -> None:
        ensure(amount >= 0, "budget consume amount must be non-negative", {"amount": amount})
        next_used = self.used + amount
        if next_used > self.limit:
            raise CtrlrError(
                "budget exceeded",
                {
                    "limit": self.limit,
                    "used": self.used,
                    "amount": amount,
                    "label": self.label,
                    "data": data,
                },
            )
        self.used = next_used


def budget(limit: int, label: str | None = None, data: dict[str, Any] | None = None) -> Budget:
    ensure(limit >= 0, "budget limit must be non-negative", {"limit": limit})
    return Budget(limit=limit, label=label, data=data)
