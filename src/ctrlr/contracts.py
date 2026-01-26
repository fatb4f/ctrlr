from __future__ import annotations

import json
from dataclasses import dataclass
from enum import Enum
from typing import Any, ClassVar


class Pillar(str, Enum):
    P1 = "P1"
    P2 = "P2"
    P3 = "P3"


class Phase(str, Enum):
    GEN = "GEN"
    STRUCT = "STRUCT"
    SELECT = "SELECT"
    FLOW = "FLOW"
    EVAL = "EVAL"


class _Model:
    _fields: ClassVar[tuple[str, ...]] = ()

    def model_dump(self) -> dict[str, Any]:
        raise NotImplementedError

    def model_dump_json(self) -> str:
        return json.dumps(self.model_dump(), separators=(",", ":"), sort_keys=True)

    @classmethod
    def model_validate(cls, data: dict[str, Any]) -> "_Model":
        raise NotImplementedError

    @classmethod
    def model_validate_json(cls, payload: str) -> "_Model":
        return cls.model_validate(json.loads(payload))


@dataclass(frozen=True)
class Lens(_Model):
    lens_id: str
    pillar: Pillar
    phase: Phase
    label: str | None = None
    data: dict[str, Any] | None = None

    def model_dump(self) -> dict[str, Any]:
        return {
            "lens_id": self.lens_id,
            "pillar": self.pillar.value,
            "phase": self.phase.value,
            "label": self.label,
            "data": self.data,
        }

    @classmethod
    def model_validate(cls, data: dict[str, Any]) -> "Lens":
        return cls(
            lens_id=str(data["lens_id"]),
            pillar=Pillar(data["pillar"]),
            phase=Phase(data["phase"]),
            label=data.get("label"),
            data=data.get("data"),
        )


@dataclass(frozen=True)
class Span(_Model):
    span_id: str
    name: str
    lens: Lens | None = None
    parent_span_id: str | None = None
    data: dict[str, Any] | None = None

    def model_dump(self) -> dict[str, Any]:
        return {
            "span_id": self.span_id,
            "name": self.name,
            "lens": self.lens.model_dump() if self.lens else None,
            "parent_span_id": self.parent_span_id,
            "data": self.data,
        }

    @classmethod
    def model_validate(cls, data: dict[str, Any]) -> "Span":
        lens_data = data.get("lens")
        return cls(
            span_id=str(data["span_id"]),
            name=str(data["name"]),
            lens=Lens.model_validate(lens_data) if lens_data else None,
            parent_span_id=data.get("parent_span_id"),
            data=data.get("data"),
        )


@dataclass(frozen=True)
class Step(_Model):
    step_id: str
    name: str
    lens: Lens | None = None
    span_id: str | None = None
    ok: bool = True
    data: dict[str, Any] | None = None

    def model_dump(self) -> dict[str, Any]:
        return {
            "step_id": self.step_id,
            "name": self.name,
            "lens": self.lens.model_dump() if self.lens else None,
            "span_id": self.span_id,
            "ok": self.ok,
            "data": self.data,
        }

    @classmethod
    def model_validate(cls, data: dict[str, Any]) -> "Step":
        lens_data = data.get("lens")
        return cls(
            step_id=str(data["step_id"]),
            name=str(data["name"]),
            lens=Lens.model_validate(lens_data) if lens_data else None,
            span_id=data.get("span_id"),
            ok=bool(data.get("ok", True)),
            data=data.get("data"),
        )


@dataclass(frozen=True)
class RunCapsule(_Model):
    run_id: str
    lens: Lens
    started_at: float | None = None
    meta: dict[str, Any] | None = None

    def model_dump(self) -> dict[str, Any]:
        return {
            "run_id": self.run_id,
            "lens": self.lens.model_dump(),
            "started_at": self.started_at,
            "meta": self.meta,
        }

    @classmethod
    def model_validate(cls, data: dict[str, Any]) -> "RunCapsule":
        return cls(
            run_id=str(data["run_id"]),
            lens=Lens.model_validate(data["lens"]),
            started_at=data.get("started_at"),
            meta=data.get("meta"),
        )
