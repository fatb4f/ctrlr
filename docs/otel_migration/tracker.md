# OTel Migration Tracker

This tracker covers deprecation of `oracle_api` and `oracle_tools` and adoption
of an OpenTelemetry-based evidence stack.

## Evidence-First DSA Workflow tools

* `pytest`, `hypothesis`
* `snoop`, `birdseye`
* `hunter`, `viztracer`
* `coverage`, `pytest-cov`

## OTel compatibility milestones

### VS Code use case

Compatibility is complete when:

1. VS Code-driven runs emit OTEL traces with operations, guards, invariants,
   and transitions.
2. Tool outputs are correlated to run/trace ids.
3. Export works for local development and OTLP backends via env vars.

### Marimo use case

Compatibility is complete when:

1. Cell execution emits OTEL traces/events with cell provenance.
2. Notebook evidence views can resolve run/trace ids.
3. Export configuration matches VS Code semantics to keep one operational
   contract.

## Milestones

### M1 - Schema contract locked

Exit criteria:
1. OTEL evidence schema is documented and versioned.
2. Required keys are fixed: schema version, run/variant identifiers, sequence
   ordering, guard/invariant outcomes, and provenance for VS Code + Marimo.
3. A validation fixture exists for one expected trace payload.

Evidence:
1. `docs/otel_migration/` schema contract doc committed.
2. Contract validation test passing in CI.

### M2 - OTEL core runtime in `oracle`

Exit criteria:
1. `oracle` provides OTEL-native helpers for run/span/step/event emission.
2. Runtime is independent of `oracle_api` and `oracle_tools`.
3. Export configuration is environment-variable driven and documented.

Evidence:
1. New runtime module in `oracle` with unit tests.
2. CI confirms trace export for local exporter and OTLP configuration.

### M3 - Adapter/materializer coverage

Exit criteria:
1. Adapters/materializers implemented in `oracle` for:
   `pytest`/`hypothesis`, `snoop`/`birdseye`, `hunter`/`viztracer`,
   `coverage`/`pytest-cov`.
2. Each adapter path preserves run/trace correlation.
3. Non-OTel-native tool outputs are mapped or linked to OTEL evidence.

Evidence:
1. At least one CI test per adapter path.
2. Generated evidence demonstrates required linkage keys.
3. Adapter contract section in `docs/otel_migration/dependency_matrix.md`
   defines shape/correlation/order for each path.

### M4 - Workflow compatibility validated

Exit criteria:
1. VS Code compatibility milestones are satisfied.
2. Marimo compatibility milestones are satisfied.
3. Deterministic rerun comparison metadata is present and stable.

Evidence:
1. Integration tests for VS Code and Marimo paths pass.
2. Verification artifact or report references trace/run correlation.

### M5 - Documentation cutover

Exit criteria:
1. OTEL-only guidance is published for setup and workflows.
2. Legacy guidance referencing `oracle_api`/`oracle_tools` is removed or
   clearly marked deprecated.
3. Migration notes include replacement mapping to `oracle`.

Evidence:
1. Docs diff removes stale install/import instructions.
2. Linkable migration notes are available in repo docs.

### M6 - Deprecation enforcement

Exit criteria:
1. Runtime/tests no longer import `oracle_api` or `oracle_tools`.
2. CI gates fail on deprecated imports and wiring regressions.
3. Package/workspace wiring is aligned to OTEL-native `oracle` paths.

Evidence:
1. Import checks pass for replacement modules and fail for deprecated modules.
2. Final cleanup PR removes remaining deprecated usage.

## Tracker

1. Define OTEL evidence schema (span + event attributes) for the DSA workflow.
2. Publish schema contract/versioning doc with required keys
   (`oracle.evidence.schema_version`, run/variant labels, ordering, guard and
   invariant outcomes, VS Code + Marimo provenance fields).
3. Implement OTEL instrumentation helpers in `oracle` (independent of
   `oracle_api` and `oracle_tools`).
4. Build adapters/materializers in `oracle` for workflow tools
   (`pytest`/`hypothesis`, `snoop`/`birdseye`, `hunter`/`viztracer`,
   `coverage`/`pytest-cov`).
5. Validate VS Code OTel compatibility against the milestones above.
6. Validate Marimo OTel compatibility against the milestones above.
7. Update docs to OTEL-only guidance for evidence-first workflows.
8. Add verification tests for OTEL evidence (schema, export, and tool
   correlation).
9. Remove/deprecate remaining `oracle_api` and `oracle_tools` usage (docs,
   tests, imports, package wiring).
