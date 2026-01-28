Objective:
- Implement deterministic proposal generation (no LLM).
- Given an ingest summary, propose ONE bounded next action.

Contract:
- .codex/packets/packet-obs-02-propose/contract.json is authoritative.

Rules:
- Execute in worktree: .codex/.worktrees/packet-obs-02-propose
- Modify only allowed_paths.
- Run: uv sync --frozen; uv run pytest -q
- Evidence: .codex/out/packet-obs-02-propose/

Tasks:
1) Create tools/external_observer/propose.py:
   - propose_next(capsule, spans, steps) -> Proposal
   - Heuristic priority:
     a) if any invariant false in last step -> propose "add/repair invariant capture"
     b) else if no steps -> propose "add minimal step emission in target function"
     c) else propose "tighten state snapshots" or "add alternatives list"
   - Output must be stable/deterministic.
2) Tests:
   - for synthetic traces, proposal matches expected class of recommendation

Evidence bundle (.codex/out/packet-obs-02-propose/):
- summary.md
- raw/uv_sync.txt
- raw/pytest.txt
- raw/diffstat.txt
