from __future__ import annotations

from pathlib import Path

from oracle_api.contracts import Lens, Phase, Pillar
from oracle_api.trace import read_jsonl, run, span, step, write_jsonl


def test_trace_jsonl_roundtrip(tmp_path: Path):
    lens = Lens(lens_id="lens-1", pillar=Pillar.P1, phase=Phase.GEN)
    jsonl_path = tmp_path / "trace.jsonl"

    with run(lens, jsonl_path) as capsule:
        with span("root") as span_obj:
            step_obj = step("step-1", span_id=span_obj.span_id)

    capsule_out, spans_out, steps_out = read_jsonl(jsonl_path)
    assert capsule_out.run_id == capsule.run_id
    assert spans_out[0].span_id == span_obj.span_id
    assert steps_out[0].step_id == step_obj.step_id


def test_write_read_jsonl(tmp_path: Path):
    lens = Lens(lens_id="lens-2", pillar=Pillar.P2, phase=Phase.STRUCT)
    jsonl_path = tmp_path / "manual.jsonl"

    with run(lens, jsonl_path):
        pass

    capsule_out, _, _ = read_jsonl(jsonl_path)
    write_jsonl(jsonl_path, capsule_out, [], [])
    capsule_round, spans_round, steps_round = read_jsonl(jsonl_path)

    assert capsule_round.run_id == capsule_out.run_id
    assert spans_round == []
    assert steps_round == []
