# OTEL Evidence Schema Contract (M1)

## Contract versioning

- Contract id: `oracle.otel.schema_contract`
- Current version: `1.0.0`
- Required span attribute: `oracle.evidence.schema_version=1.0.0`
- Compatibility rule:
  - Patch version updates (`1.0.x`) are additive/non-breaking.
  - Minor/major updates require migration notes and updated validation fixtures.

## Required span attributes

Every Evidence-First DSA span that participates in the contract must include:

- `oracle.evidence.schema_version`
- `oracle.run_id`
- `oracle.seq`

At least one of:

- `oracle.variant_id`
- `oracle.run_label`

## Event model

Guard, invariant, and explanation payloads are event-level.

### `oracle.guard`

Required attributes:

- `oracle.guard.condition`
- `oracle.guard.status` with enum `{pass, fail, skip}`

### `oracle.invariant`

Required attributes:

- `oracle.invariant.id`
- `oracle.invariant.statement`
- `oracle.invariant.status` with enum `{pass, fail, skip}`

### `oracle.explanation`

Required attributes:

- `oracle.explanation.text`

## Provenance minima

### VS Code/editor provenance

When editor provenance exists, use OTel semantic-convention fields:

- `code.filepath`
- `code.lineno`

### Marimo provenance

For notebook-cell execution:

- `oracle.notebook_id`
- `oracle.cell_id`

