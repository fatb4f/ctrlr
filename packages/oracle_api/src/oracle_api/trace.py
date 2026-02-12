from __future__ import annotations

import json
import time
from contextlib import contextmanager
from contextvars import ContextVar
from pathlib import Path
from typing import Iterable
from uuid import uuid4

from .contracts import Lens, RunCapsule, Span, Step


_current_lens: ContextVar[Lens | None] = ContextVar("ctrlr_current_lens", default=None)
_current_span_id: ContextVar[str | None] = ContextVar("ctrlr_current_span_id", default=None)
_current_jsonl_path: ContextVar[Path | None] = ContextVar("ctrlr_current_jsonl_path", default=None)


def _write_record(path: Path, record_type: str, data: dict, mode: str) -> None:
    line = json.dumps({"type": record_type, "data": data}, separators=(",", ":"), sort_keys=True)
    with path.open(mode, encoding="utf-8") as handle:
        handle.write(line + "\n")


def _append_record(record_type: str, data: dict) -> None:
    path = _current_jsonl_path.get()
    if path is None:
        return
    _write_record(path, record_type, data, "a")


def current_lens() -> Lens | None:
    return _current_lens.get()


def current_span_id() -> str | None:
    return _current_span_id.get()


@contextmanager
def run(lens: Lens, jsonl_path: str | Path):
    path = Path(jsonl_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    capsule = RunCapsule(run_id=str(uuid4()), lens=lens, started_at=time.time())
    _write_record(path, "run", capsule.model_dump(), "w")

    token_lens = _current_lens.set(lens)
    token_span = _current_span_id.set(None)
    token_path = _current_jsonl_path.set(path)
    try:
        yield capsule
    finally:
        _current_jsonl_path.reset(token_path)
        _current_span_id.reset(token_span)
        _current_lens.reset(token_lens)


@contextmanager
def span(name: str, lens: Lens | None = None, data: dict | None = None):
    active_lens = lens or current_lens()
    span_id = str(uuid4())
    parent_id = current_span_id()
    span_obj = Span(
        span_id=span_id,
        name=name,
        lens=active_lens,
        parent_span_id=parent_id,
        data=data,
    )
    _append_record("span", span_obj.model_dump())

    token_span = _current_span_id.set(span_id)
    try:
        yield span_obj
    finally:
        _current_span_id.reset(token_span)


def step(
    name: str,
    lens: Lens | None = None,
    span_id: str | None = None,
    ok: bool = True,
    data: dict | None = None,
) -> Step:
    active_lens = lens or current_lens()
    effective_span_id = span_id if span_id is not None else current_span_id()
    step_obj = Step(
        step_id=str(uuid4()),
        name=name,
        lens=active_lens,
        span_id=effective_span_id,
        ok=ok,
        data=data,
    )
    _append_record("step", step_obj.model_dump())
    return step_obj


def write_jsonl(
    jsonl_path: str | Path,
    capsule: RunCapsule,
    spans: Iterable[Span],
    steps: Iterable[Step],
) -> None:
    path = Path(jsonl_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    _write_record(path, "run", capsule.model_dump(), "w")
    for span_obj in spans:
        _write_record(path, "span", span_obj.model_dump(), "a")
    for step_obj in steps:
        _write_record(path, "step", step_obj.model_dump(), "a")


def read_jsonl(jsonl_path: str | Path) -> tuple[RunCapsule, list[Span], list[Step]]:
    path = Path(jsonl_path)
    capsule: RunCapsule | None = None
    spans: list[Span] = []
    steps: list[Step] = []

    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        record = json.loads(line)
        record_type = record.get("type")
        data = record.get("data")
        if record_type == "run":
            capsule = RunCapsule.model_validate(data)
        elif record_type == "span":
            spans.append(Span.model_validate(data))
        elif record_type == "step":
            steps.append(Step.model_validate(data))

    if capsule is None:
        raise ValueError("run capsule missing from jsonl")

    return capsule, spans, steps
