Objective:
- Implement ctrlr contracts (Lens/Span/Step/RunCapsule) with stdlib dataclasses + lightweight JSON helpers.

Contract:
- .codex/packets/packet-ctrlr-00-contracts/contract.json is authoritative.

Rules:
- Execute in worktree: .codex/.worktrees/packet-ctrlr-00-contracts
- Modify only allowed_paths.
- Run tests: uv sync --frozen; uv run pytest -q
- Evidence: .codex/out/packet-ctrlr-00-contracts/

Tasks:
1) Create src/ctrlr/contracts.py with:
   - Enums: Pillar(P1/P2/P3), Phase(GEN/STRUCT/SELECT/FLOW/EVAL)
   - Lightweight models: Lens, Span, Step, RunCapsule
   - Provide model_dump/model_validate and model_dump_json/model_validate_json helpers
   - Keep fields minimal and JSON-serializable; no new dependencies
2) Create/update src/ctrlr/__init__.py exports for these contracts.
3) Add tests:
   - schema roundtrip: model_validate_json(model_dump_json()) works
   - minimal Step/Span/RunCapsule validates

Evidence bundle (.codex/out/packet-ctrlr-00-contracts/):
- summary.md (what changed, PASS/FAIL)
- raw/uv_sync.txt
- raw/pytest.txt
- raw/diffstat.txt
