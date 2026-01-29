# Packet 0202 — Deterministic seeding

## Intent
Add `seeded(...)` helper to control RNG state deterministically.

## Deliverables
- `src/ctrlr/seeded.py` (new)
- Exports in `src/ctrlr/__init__.py`
- Tests in `tests/test_seeded.py`
- Short doc note in README (if needed)

## Constraints
- No new base runtime deps.
- Deterministic behavior; restore RNG state on exit.
- Optional NumPy seeding only if installed (lazy import).

## Implementation notes
- Implement as context manager.
- Seed Python `random` and restore prior state on exit.
- If NumPy is available, seed and restore its RNG state too.
- Nested contexts should be deterministic and restore correctly.

## Tests
- Same seed ⇒ same output
- Different seed ⇒ different output
- State restoration (no cross-test contamination)
- Nested contexts behave predictably

## Evidence
- Pytest log
- Diffstat
