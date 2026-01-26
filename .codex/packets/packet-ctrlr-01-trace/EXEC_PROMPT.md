Objective:
- Implement ctrlr trace runtime: run/span/step + JSONL writer/reader + contextvars current span/lens.

Contract:
- .codex/packets/packet-ctrlr-01-trace/contract.json is authoritative.

Rules:
- Execute in worktree: .codex/.worktrees/packet-ctrlr-01-trace
- Modify only allowed_paths.
- Run: uv sync --frozen; uv run pytest -q
- Evidence: out/packet-ctrlr-01-trace/

Tasks:
1) Create src/ctrlr/trace.py:
   - context managers: run(lens, jsonl_path), span(name, lens?, data?)
   - function: step(...) -> Step (validated)
   - helpers: current_lens(), current_span_id()
   - JSONL: write_jsonl(), read_jsonl() returning (RunCapsule, [Span], [Step])
   - Use contextvars; avoid global mutable state.
2) Update src/ctrlr/__init__.py exports.
3) Tests:
   - write/read JSONL roundtrip (capsule+span+step)
   - nested spans set parent_id correctly (if you include it in Span/Step)

Evidence bundle (out/packet-ctrlr-01-trace/):
- summary.md
- raw/uv_sync.txt
- raw/pytest.txt
- raw/diffstat.txt
