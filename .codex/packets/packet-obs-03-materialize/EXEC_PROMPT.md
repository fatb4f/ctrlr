Objective:
- Materialize a Proposal into a next packet contract stub (Plant B -> Plant A bridge).

Contract:
- .codex/packets/packet-obs-03-materialize/contract.json is authoritative.

Rules:
- Execute in worktree: .codex/.worktrees/packet-obs-03-materialize
- Modify only allowed_paths.
- Run: uv sync --frozen; uv run pytest -q
- Evidence: .codex/out/packet-obs-03-materialize/

Tasks:
1) Create tools/external_observer/materialize.py:
   - function proposal_to_packet_stub(proposal) -> dict/PacketStub
   - ensure output includes:
     - packet_id (derived)
     - base_ref main
     - branch name
     - allowed_paths / diff_budget / test_cmd
     - worktree_policy with `.codex/.worktrees`
2) Tests:
   - stub json validates against PacketStub model
   - derived ids are deterministic

Evidence bundle (.codex/out/packet-obs-03-materialize/):
- summary.md
- raw/uv_sync.txt
- raw/pytest.txt
- raw/diffstat.txt
