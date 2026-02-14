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

## Tracker

1. Define OTEL evidence schema (span + event attributes) for the DSA workflow.
2. Publish schema contract/versioning doc with required keys
   (`oracle.evidence.schema_version`, run/variant labels, ordering, guard and
   invariant outcomes, VS Code + Marimo provenance fields).
3. Implement OTEL instrumentation helpers independent of `oracle_api` and
   `oracle_tools`.
4. Build adapters/materializers for workflow tools
   (`pytest`/`hypothesis`, `snoop`/`birdseye`, `hunter`/`viztracer`,
   `coverage`/`pytest-cov`).
5. Validate VS Code OTel compatibility against the milestones above.
6. Validate Marimo OTel compatibility against the milestones above.
7. Update docs to OTEL-only guidance for evidence-first workflows.
8. Add verification tests for OTEL evidence (schema, export, and tool
   correlation).
9. Remove/deprecate remaining `oracle_api` and `oracle_tools` usage (docs,
   tests, imports, package wiring).
