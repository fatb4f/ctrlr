Objective:
- Define observer Domain 1 contracts with stdlib dataclasses + lightweight JSON helpers.

Contract:
- .codex/packets/packet-obs-00-contracts/contract.json is authoritative.

Rules:
- Execute in worktree: .codex/.worktrees/packet-obs-00-contracts
- Modify only allowed_paths.
- Run: uv sync --frozen; uv run pytest -q
- Evidence: .codex/out/packet-obs-00-contracts/

Tasks:
1) Create tools/external_observer/contracts.py with lightweight models:
   - ObserverSnapshot (minimal run summary + last N steps pointers)
   - Proposal (single bounded action: next_micro_step, success_criteria, rollback, bounded_scope)
   - PacketStub (packet_id, branch, allowed_paths, diff_budget, test_cmd, evidence_required)
2) Add tests: model roundtrip (model_dump_json/model_validate_json) and minimal validation.

Evidence bundle (.codex/out/packet-obs-00-contracts/):
- summary.md
- raw/uv_sync.txt
- raw/pytest.txt
- raw/diffstat.txt
