Objective:
- Implement observer ingest: read ctrlr JSONL trace -> normalized run model.

Contract:
- .codex/packets/packet-obs-01-ingest/contract.json is authoritative.

Rules:
- Execute in worktree: .codex/.worktrees/packet-obs-01-ingest
- Modify only allowed_paths.
- Run: uv sync --frozen; uv run pytest -q
- Evidence: .codex/out/packet-obs-01-ingest/

Tasks:
1) Create tools/external_observer/ingest.py:
   - function load_trace(jsonl_path) -> (capsule, spans, steps)
   - minimal derived summary: counts, last step, any failed invariants (if modeled)
2) Tests:
   - create a tiny synthetic JSONL in tmp path and ensure ingest returns expected structure

Evidence bundle (.codex/out/packet-obs-01-ingest/):
- summary.md
- raw/uv_sync.txt
- raw/pytest.txt
- raw/diffstat.txt
