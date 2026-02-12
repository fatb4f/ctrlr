from __future__ import annotations

from typing import Iterable

from oracle_api.contracts import Span, Step


def _sanitize_id(raw: str, prefix: str) -> str:
    safe = "".join(ch if ch.isalnum() else "_" for ch in raw)
    if not safe:
        safe = prefix
    if safe[0].isdigit():
        safe = f"{prefix}_{safe}"
    return safe


def _quote_label(label: str) -> str:
    return label.replace('"', '\\"')


def to_mermaid_flow(steps: Iterable[Step], direction: str = "TD") -> str:
    step_list = list(steps)
    lines: list[str] = [f"flowchart {direction}"]
    node_ids: list[str] = []

    for idx, step_obj in enumerate(step_list, start=1):
        node_id = _sanitize_id(step_obj.step_id, f"step_{idx}")
        node_ids.append(node_id)
        label = _quote_label(step_obj.name)
        lines.append(f'  {node_id}["{label}"]')

    for left, right in zip(node_ids, node_ids[1:]):
        lines.append(f"  {left} --> {right}")

    return "\n".join(lines)


def to_mermaid_calltree(spans: Iterable[Span], direction: str = "TD") -> str:
    span_list = list(spans)
    lines: list[str] = [f"flowchart {direction}"]
    span_ids = {span.span_id: _sanitize_id(span.span_id, "span") for span in span_list}

    for span_obj in span_list:
        node_id = span_ids[span_obj.span_id]
        label = _quote_label(span_obj.name)
        lines.append(f'  {node_id}["{label}"]')

    for span_obj in span_list:
        parent = span_obj.parent_span_id
        if parent and parent in span_ids:
            lines.append(f"  {span_ids[parent]} --> {span_ids[span_obj.span_id]}")

    return "\n".join(lines)
