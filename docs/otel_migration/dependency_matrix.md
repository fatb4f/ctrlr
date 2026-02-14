# OTel Migration Dependency Matrix

This matrix tracks legacy dependencies on deprecated packages and defines the
OpenTelemetry compatibility contract for the Evidence-First DSA workflow.

## Deprecation scope

- `oracle_api`: deprecated, replaced by OTEL-native schema and instrumentation.
- `oracle_tools`: deprecated, replaced by `oracle` (OTEL-native
  adapters/materializers/helpers).

## Replacement package/module

- `oracle`: canonical home for OTEL-native adapters, materializers, and helper
  utilities that replace legacy `oracle_tools` behavior.

## Evidence-First DSA Workflow tools

- `pytest`, `hypothesis`
- `snoop`, `birdseye`
- `hunter`, `viztracer`
- `coverage`, `pytest-cov`

## OTel compatibility definitions

Required OTEL evidence metadata (all workflows):

- `oracle.evidence.schema_version`
- `oracle.run_id`
- `oracle.variant_id` and/or `oracle.run_label`
- deterministic step ordering key (`oracle.seq`)
- guard/invariant outcome fields

### VS Code use case

OTel compatibility is satisfied when all of the following are true:

- Running tests/debug sessions from VS Code emits OTEL traces for algorithm
  runs (operations, guards, invariants, transitions).
- Evidence-first tool outputs can be correlated to the same trace/run id.
- Editor provenance is present (`code.filepath`, `code.lineno` at minimum).
- OTEL export works with both local development (`console`/`file`) and OTLP
  endpoints configured through environment variables.
- Failure analysis remains actionable from VS Code output (trace id + event
  attributes are visible without custom notebook tooling).

### Marimo use case

OTel compatibility is satisfied when all of the following are true:

- Executing notebook cells emits OTEL traces/events with cell provenance.
- Notebook provenance is present (`oracle.notebook_id`, `oracle.cell_id`).
- Evidence artifacts rendered in notebooks map to trace/run ids so users can
  navigate from explanation to raw telemetry.
- OTEL export supports the same environment-variable configuration used in VS
  Code to keep one operational model across both workflows.
- Interactive reruns preserve deterministic comparison metadata for evidence
  review (run labels, variant ids, invariant outcomes).

## Tool-to-OTel mapping targets

- `pytest`, `hypothesis`: map test examples/cases to OTEL spans and attach
  assertion outcomes as event attributes.
- `snoop`, `birdseye`: adapt runtime introspection output into OTEL events or
  linked evidence records.
- `hunter`, `viztracer`: translate call/line traces into OTEL-linked
  structures for calltree/flow materialization.
- `coverage`, `pytest-cov`: export run-level coverage summaries as OTEL-linked
  evidence metadata.

## M3 adapter output contract (locked)

Each adapter path must emit one `oracle.step` span with required schema keys:
`oracle.evidence.schema_version`, `oracle.run_id`, `oracle.seq`, and
`oracle.variant_id` or `oracle.run_label`.

- `pytest`/`hypothesis`
  - Shape: step span + `oracle.pytest.case` event.
  - Correlation keys: `oracle.run_id`, `oracle.step_id`, `oracle.adapter.seq`.
  - Ordering: `oracle.seq` on span; `oracle.adapter.seq` on case events.
- `snoop`/`birdseye`
  - Shape: step span + `oracle.snoop.event` or `oracle.birdseye.frame` events.
  - Correlation keys: `oracle.run_id`, `oracle.step_id`, `oracle.adapter.seq`.
  - Ordering: `oracle.seq` on span; `oracle.adapter.seq` on trace/frame events.
- `hunter`/`viztracer`
  - Shape: step span + `oracle.hunter.event` or `oracle.viztracer.event` events.
  - Correlation keys: `oracle.run_id`, `oracle.step_id`, `oracle.adapter.seq`.
  - Ordering: `oracle.seq` on span; `oracle.adapter.seq` for event order.
- `coverage`/`pytest-cov`
  - Shape: step span + `oracle.coverage.summary` event.
  - Correlation keys: `oracle.run_id`, `oracle.step_id`, `oracle.adapter.seq`.
  - Ordering: run summary uses the step span `oracle.seq` and summary event
    `oracle.adapter.seq`.

All adapter paths must also emit `oracle.guard`, `oracle.invariant`, and
`oracle.explanation` events to preserve materializer compatibility for step
sequence, invariant/guard outcomes, and provenance.

## Adapter requirements for non-OTel-native tools

`snoop`, `birdseye`, `hunter`, and `viztracer` are treated as non-OTel-native
in this repo. Compatibility requires configured adapters/materializers.

- `snoop`
  - Capture trace events and map them to OTEL span events with run/trace ids.
  - Preserve step ordering and guard/invariant context in event attributes.
- `birdseye`
  - Export debugger session artifacts as OTEL-linked evidence records.
  - Maintain source location mapping (module/function/line) for replay.
- `hunter`
  - Convert `Event` stream output into OTEL span events or child spans.
  - Keep call parent/child linkage for calltree reconstruction.
- `viztracer`
  - Materialize VizTracer trace output into OTEL-linked call/flow structures.
  - Preserve timing and function identity for performance/causality review.

Minimum acceptance criteria for all four tools:

- Same run/trace id correlation model in VS Code and Marimo.
- OTEL export path works with local exporters and OTLP endpoints.
- At least one verification test per adapter path in CI.

## Legacy dependency matrix (to remove)

- `packages/oracle_tools/src/oracle_tools/mermaid.py`
  - Depends on `oracle_api.contracts` (`Span`, `Step`).
- `packages/oracle_tools/src/oracle_tools/budget.py`
  - Depends on `oracle_api.control` (`CtrlrError`, `ensure`).
- `packages/oracle_tools/tests/test_mermaid.py`
  - Imports `oracle_api.contracts` (`Lens`, `Phase`, `Pillar`, `Span`, `Step`).
- `packages/oracle_tools/tests/test_experiment.py`
  - Imports `oracle_api.control` and `oracle_api.seeded`.
- `packages/oracle_tools/pyproject.toml`
  - Direct dependency on `oracle_api`.

## Repo integrations

- `integration/tests/test_imports.py`
  - Imports `oracle_api`.

## Docs + guidance

- `docs/oracle-ctrlr.md`
  - Describes `oracle_api` as core pieces.
- `docs/oracle_overview.md`
  - Refers to `oracle_api` as stable substrate and instrumentation target.
- `docs/basic_usage.md`
  - Layout + dependency rule mentions `oracle_api`.
- `docs/configuration_and_settings.md`
  - Install instructions for `oracle_api`.
- `docs/dev_flow.md`
  - Mentions promoting stable code into `oracle_api`.

## Package metadata

- `pyproject.toml`
  - Workspace member includes `packages/oracle_api`.
- `packages/oracle_api/*`
  - Tests + modules.

## Migration target state

- No runtime or tests import `oracle_api` or `oracle_tools`.
- Evidence-first workflow tools operate through OTEL adapters implemented in
  `oracle`.
- VS Code and Marimo both pass OTEL compatibility criteria defined above.
