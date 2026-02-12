from __future__ import annotations

from oracle_api.contracts import Lens, Phase, Pillar, RunCapsule, Span, Step


def test_lens_roundtrip_json():
    lens = Lens(lens_id="lens-1", pillar=Pillar.P1, phase=Phase.GEN, label="seed")
    payload = lens.model_dump_json()
    restored = Lens.model_validate_json(payload)
    assert restored.model_dump() == lens.model_dump()


def test_minimal_span_step_run():
    lens = Lens(lens_id="lens-2", pillar=Pillar.P2, phase=Phase.STRUCT)
    span = Span(span_id="span-1", name="root", lens=lens)
    step = Step(step_id="step-1", name="do", lens=lens, span_id=span.span_id)
    capsule = RunCapsule(run_id="run-1", lens=lens)
    assert span.span_id == "span-1"
    assert step.span_id == "span-1"
    assert capsule.run_id == "run-1"
