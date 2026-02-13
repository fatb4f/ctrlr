# OTel Migration Tracker

This tracker covers the deprecation of `oracle_api` and adoption of an
OpenTelemetry-based evidence stack.

## Evidence-First DSA Workflow tools

* `pytest`, `hypothesis`
* `snoop`, `birdseye`
* `hunter`, `viztracer`
* `coverage`, `pytest-cov`

## Tracker

1. Define OTEL evidence schema (span + event attributes) for the DSA workflow.
2. Implement OTEL instrumentation helpers (likely in `oracle_tools`).
3. Build a trace materializer/adapter for Mermaid renderers.
4. Update tool stack dependencies (oracle_tools no longer requires oracle_api).
5. Update docs to reference OTEL path + evidence-first workflow.
6. Add verification tests for OTEL evidence (schema + basic export).
7. Deprecate oracle_api usage (docs + tests + imports).
