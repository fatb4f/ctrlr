# OTel Migration Dependency Matrix

Backward dependencies on `oracle_api`.

## Evidence-First DSA Workflow tools

- `pytest`, `hypothesis`
- `snoop`, `birdseye`
- `hunter`, `viztracer`
- `coverage`, `pytest-cov`

## Tool stack (highest priority)

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
