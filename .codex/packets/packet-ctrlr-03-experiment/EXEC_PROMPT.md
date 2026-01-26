Objective:
- Implement budgets + deterministic seeding utilities (small, stdlib-first).

Contract:
- .codex/packets/packet-ctrlr-03-experiment/contract.json is authoritative.

Rules:
- Execute in worktree: .codex/.worktrees/packet-ctrlr-03-experiment
- Modify only allowed_paths.
- Run: uv sync --frozen; uv run pytest -q
- Evidence: out/packet-ctrlr-03-experiment/

Tasks:
1) Create src/ctrlr/experiment.py:
   - Budget dataclass(max_iters:int|None, max_seconds:float|None)
   - budget(budget)->contextmanager yielding tick(); tick raises CtrlrError when exhausted
   - seeded(seed)->contextmanager that seeds stdlib random; restore previous state on exit
2) Update src/ctrlr/__init__.py exports.
3) Tests:
   - budget tick exhausts at expected iteration count
   - seeded produces deterministic random sequences and restores state

Evidence bundle (out/packet-ctrlr-03-experiment/):
- summary.md
- raw/uv_sync.txt
- raw/pytest.txt
- raw/diffstat.txt
