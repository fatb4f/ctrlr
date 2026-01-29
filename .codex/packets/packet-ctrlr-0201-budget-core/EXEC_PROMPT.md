# Packet 0201 — Budget core

## Intent
Add `Budget` dataclass + helpers with a minimal, stable API and deterministic behavior.

## Deliverables
- `src/ctrlr/budget.py` (new)
- Exports in `src/ctrlr/__init__.py`
- Tests in `tests/test_budget.py`

## Constraints
- No new base runtime deps.
- Deterministic behavior; no nondeterministic metadata in outputs.
- Keep API surface small and explicit.

## Implementation notes
- Decide and document:
  - Mutable vs immutable `consume()` behavior
  - Overflow behavior (deny/raise/clamp)
  - Invariants (`limit >= 0`, `used >= 0`, `used <= limit` policy)
- Provide `remaining` property.

## Tests
- Construction invariants
- `consume()` monotonicity
- Overflow behavior matches the contract
- `repr`/`str` stable and informative

## Evidence
- Pytest log
- Diffstat
