# Packet 0203 — Mermaid flow

## Intent
Add `to_mermaid_flow(...)` helper for deterministic flow rendering from trace steps.

## Deliverables
- `src/ctrlr/mermaid.py` (new, flow helper)
- Exports in `src/ctrlr/__init__.py`
- Tests in `tests/test_mermaid_flow.py`
- Short doc note in README (if needed)

## Constraints
- Deterministic output: stable IDs, stable ordering, consistent escaping.
- No new base runtime deps.

## Implementation notes
- Define minimal input schema and stick to it.
- Preserve input order or apply explicit deterministic sorting (pick one and test it).
- Escape labels to keep Mermaid output stable.

## Tests
- Golden test: canonical trace input ⇒ exact Mermaid string.
- Ordering test: codify ordering behavior.

## Evidence
- Pytest log
- Diffstat
