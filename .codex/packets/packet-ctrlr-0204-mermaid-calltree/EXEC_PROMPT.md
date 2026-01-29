# Packet 0204 — Mermaid calltree

## Intent
Add `to_mermaid_calltree(...)` helper for deterministic calltree rendering from spans.

## Deliverables
- `src/ctrlr/mermaid.py` (calltree helper)
- Exports in `src/ctrlr/__init__.py`
- Tests in `tests/test_mermaid_calltree.py`

## Constraints
- Deterministic output: stable IDs, stable ordering, consistent escaping.
- No new base runtime deps.

## Implementation notes
- Define minimal input schema for spans: `span_id`, `name`, `parent_span_id`.
- Missing parent: treat as root span.
- Cycle: raise a clear error.

## Tests
- Golden test: canonical span input ⇒ exact Mermaid string.
- Missing parent behavior is deterministic.
- Cycle behavior matches contract.

## Evidence
- Pytest log
- Diffstat
