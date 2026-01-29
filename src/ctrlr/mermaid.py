from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable

from .contracts import Step


@dataclass(frozen=True)
class _FlowNode:
    step_id: str
    name: str


def _normalize_step(item: Step | dict) -> _FlowNode:
    if isinstance(item, Step):
        return _FlowNode(step_id=item.step_id, name=item.name)
    if isinstance(item, dict):
        if "step_id" not in item or "name" not in item:
            raise ValueError("step must include step_id and name")
        return _FlowNode(step_id=str(item["step_id"]), name=str(item["name"]))
    raise TypeError("step must be Step or dict")


def _safe_id(step_id: str) -> str:
    out = []
    for ch in step_id:
        if ch.isalnum() or ch == "_":
            out.append(ch)
        else:
            out.append("_")
    return "S_" + "".join(out)


def _escape_label(text: str) -> str:
    return (
        text.replace("\\", "\\\\")
        .replace("\"", "\\\"")
        .replace("\n", "\\n")
        .replace("\r", "\\r")
    )


def to_mermaid_flow(steps: Iterable[Step | dict]) -> str:
    """Render a deterministic Mermaid flowchart from ordered steps."""
    nodes = [_normalize_step(s) for s in steps]
    lines = ["flowchart TD"]

    for node in nodes:
        node_id = _safe_id(node.step_id)
        label = _escape_label(f"{node.step_id}: {node.name}")
        lines.append(f'  {node_id}["{label}"]')

    for prev, nxt in zip(nodes, nodes[1:]):
        lines.append(f"  {_safe_id(prev.step_id)} --> {_safe_id(nxt.step_id)}")

    return "\n".join(lines) + "\n"
