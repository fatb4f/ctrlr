import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from ctrlr import Step, to_mermaid_flow


def test_mermaid_flow_golden() -> None:
    steps = [
        Step(step_id="s1", name="start"),
        Step(step_id="s2", name='do "x"'),
        Step(step_id="s3", name="end\nline"),
    ]
    out = to_mermaid_flow(steps)
    expected = (
        "flowchart TD\n"
        '  S_s1["s1: start"]\n'
        '  S_s2["s2: do \\"x\\""]\n'
        '  S_s3["s3: end\\nline"]\n'
        "  S_s1 --> S_s2\n"
        "  S_s2 --> S_s3\n"
    )
    assert out == expected


def test_mermaid_flow_preserves_order() -> None:
    steps = [
        {"step_id": "b", "name": "B"},
        {"step_id": "a", "name": "A"},
    ]
    out = to_mermaid_flow(steps)
    assert "S_b --> S_a" in out
