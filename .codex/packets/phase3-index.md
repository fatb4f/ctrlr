# Phase 3 packet index (ctrlr + external_observer)

Conventions
- Worktrees: `.codex/.worktrees/<packet_id>` (gitignored)
- Packets: `.codex/packets/<packet_id>/`
- Evidence: `.codex/out/<packet_id>/` (gitignored)

Execution order (recommended)
1) ctrlr core
   - packet-ctrlr-00-contracts
   - packet-ctrlr-01-trace
   - packet-ctrlr-02-control
   - packet-ctrlr-03-experiment
   - packet-ctrlr-04-viz
   - packet-ctrlr-05-otel (optional; keep behind extras)

2) external observer (Domain 1 controller)
   - packet-obs-00-contracts
   - packet-obs-01-ingest
   - packet-obs-02-propose (deterministic; no LLM required)
   - packet-obs-03-materialize (proposal -> next packet stub)

Notes
- Early packets assume only `uv sync --frozen` + `uv run pytest -q`.
- Evidence bundles are written under `.codex/out/<packet_id>/` and ignored by git.
