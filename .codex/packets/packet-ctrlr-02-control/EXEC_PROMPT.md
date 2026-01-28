Objective:
- Implement control gates: CtrlrError + require/ensure/invariant.
- Each gate should optionally emit a failure Step/Event (keep minimal: at least raise with structured data).

Contract:
- .codex/packets/packet-ctrlr-02-control/contract.json is authoritative.

Rules:
- Execute in worktree: .codex/.worktrees/packet-ctrlr-02-control
- Modify only allowed_paths.
- Run: uv sync --frozen; uv run pytest -q
- Evidence: .codex/out/packet-ctrlr-02-control/

Tasks:
1) Create src/ctrlr/control.py:
   - CtrlrError(RuntimeError)
   - require(cond, msg, data?) -> None
   - ensure(cond, msg, data?) -> None
   - invariant(cond, msg, data?) -> None
   - On failure: raise CtrlrError with msg + data (repr-safe)
   - Optional: integrate with trace.step(...) if a run context exists (safe no-op otherwise).
2) Update src/ctrlr/__init__.py exports.
3) Tests:
   - gate passes do nothing
   - gate fails raises CtrlrError and contains message + data

Evidence bundle (.codex/out/packet-ctrlr-02-control/):
- summary.md
- raw/uv_sync.txt
- raw/pytest.txt
- raw/diffstat.txt
