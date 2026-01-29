import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from ctrlr import Span, to_mermaid_calltree


def test_mermaid_calltree_golden() -> None:
    spans = [
        Span(span_id="s1", name="root"),
        Span(span_id="s2", name='child "a"', parent_span_id="s1"),
        Span(span_id="s3", name="leaf\nline", parent_span_id="s2"),
    ]
    out = to_mermaid_calltree(spans)
    expected = (
        "flowchart TD\n"
        '  ROOT["root"]\n'
        '  SPAN_s1["s1: root"]\n'
        '  SPAN_s2["s2: child \\"a\\""]\n'
        '  SPAN_s3["s3: leaf\\nline"]\n'
        "  ROOT --> SPAN_s1\n"
        "  SPAN_s1 --> SPAN_s2\n"
        "  SPAN_s2 --> SPAN_s3\n"
    )
    assert out == expected


def test_mermaid_calltree_missing_parent_attaches_root() -> None:
    spans = [
        {"span_id": "a", "name": "A", "parent_span_id": "missing"},
        {"span_id": "b", "name": "B"},
    ]
    out = to_mermaid_calltree(spans)
    assert "ROOT --> SPAN_a" in out
    assert "ROOT --> SPAN_b" in out


def test_mermaid_calltree_cycle_raises() -> None:
    spans = [
        {"span_id": "x", "name": "X", "parent_span_id": "x"},
    ]
    try:
        to_mermaid_calltree(spans)
    except ValueError as exc:
        assert "cycle" in str(exc)
    else:
        raise AssertionError("expected ValueError")
