Objective:
- Define observer Domain 1 contracts (Pydantic) for B-A-B loop outputs.

Contract:
- .codex/packets/packet-obs-00-contracts/contract.json is authoritative.

Rules:
- Execute in worktree: .codex/.worktrees/packet-obs-00-contracts
- Modify only allowed_paths.
- Run: uv sync --frozen; uv run pytest -q
- Evidence: out/packet-obs-00-contracts/

Tasks:
1) Create tools/external_observer/contracts.py with Pydantic models:
   - ObserverSnapshot (minimal run summary + last N steps pointers)
   - Proposal (single bounded action: next_micro_step, success_criteria, rollback, bounded_scope)
   - PacketStub (packet_id, branch, allowed_paths, diff_budget, test_cmd, evidence_required)
2) Add tests: model roundtrip and minimal validation.

Evidence bundle (out/packet-obs-00-contracts/):
- summary.md
- raw/uv_sync.txt
- raw/pytest.txt
- raw/diffstat.txt
