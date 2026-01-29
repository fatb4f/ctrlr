from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable

from .contracts import Span


@dataclass(frozen=True)
class _SpanNode:
    span_id: str
    name: str
    parent_span_id: str | None


def _normalize_span(item: Span | dict) -> _SpanNode:
    if isinstance(item, Span):
        return _SpanNode(span_id=item.span_id, name=item.name, parent_span_id=item.parent_span_id)
    if isinstance(item, dict):
        if "span_id" not in item or "name" not in item:
            raise ValueError("span must include span_id and name")
        return _SpanNode(
            span_id=str(item["span_id"]),
            name=str(item["name"]),
            parent_span_id=item.get("parent_span_id"),
        )
    raise TypeError("span must be Span or dict")


def _safe_id(raw_id: str, prefix: str) -> str:
    out = []
    for ch in raw_id:
        if ch.isalnum() or ch == "_":
            out.append(ch)
        else:
            out.append("_")
    return prefix + "".join(out)


def _escape_label(text: str) -> str:
    return (
        text.replace("\\", "\\\\")
        .replace("\"", "\\\"")
        .replace("\n", "\\n")
        .replace("\r", "\\r")
    )


def _detect_self_cycle(nodes: list[_SpanNode]) -> None:
    for node in nodes:
        if node.parent_span_id == node.span_id:
            raise ValueError("span parent cycle detected")


def to_mermaid_calltree(spans: Iterable[Span | dict]) -> str:
    """Render a deterministic Mermaid calltree from ordered spans."""
    nodes = [_normalize_span(s) for s in spans]
    node_ids = {n.span_id for n in nodes}
    _detect_self_cycle(nodes)

    lines = ["flowchart TD"]
    root_id = "ROOT"
    lines.append(f'  {root_id}["root"]')

    for node in nodes:
        node_id = _safe_id(node.span_id, "SPAN_")
        label = _escape_label(f"{node.span_id}: {node.name}")
        lines.append(f'  {node_id}["{label}"]')

    for node in nodes:
        parent = node.parent_span_id
        if parent is None or parent not in node_ids:
            lines.append(f"  {root_id} --> {_safe_id(node.span_id, 'SPAN_')}")
        else:
            lines.append(f"  {_safe_id(parent, 'SPAN_')} --> {_safe_id(node.span_id, 'SPAN_')}")

    return "\n".join(lines) + "\n"
