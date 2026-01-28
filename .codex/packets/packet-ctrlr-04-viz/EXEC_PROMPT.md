Objective:
- Render interpreter trace to Mermaid.
  - to_mermaid_flow: step0->step1 linear flow, optionally grouped by Lens.phase
  - to_mermaid_calltree: call-tree using parent_span_id relationships (if present)

Contract:
- .codex/packets/packet-ctrlr-04-viz/contract.json is authoritative.

Rules:
- Execute in worktree: .codex/.worktrees/packet-ctrlr-04-viz
- Modify only allowed_paths.
- Run: uv sync --frozen; uv run pytest -q
- Evidence: .codex/out/packet-ctrlr-04-viz/

Tasks:
1) Create src/ctrlr/viz.py:
   - to_mermaid_flow(steps, group_by_phase=True) -> str
   - to_mermaid_calltree(steps) -> str
   - sanitize labels (escape quotes/newlines)
2) Update src/ctrlr/__init__.py exports.
3) Tests:
   - output starts with "flowchart TD"
   - contains expected node ids and edges for a tiny synthetic Step list

Evidence bundle (.codex/out/packet-ctrlr-04-viz/):
- summary.md
- raw/uv_sync.txt
- raw/pytest.txt
- raw/diffstat.txt
