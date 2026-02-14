# Oracle Overview

This repo uses an OTEL-native evidence model for DSA development and debugging.
The canonical runtime, adapters, and materializers live in `packages/oracle`.

## Core idea

Build and debug DSAs by emitting structured evidence first:

* step and run spans
* guard and invariant outcomes
* explanation events
* provenance (VS Code file/line or Marimo notebook/cell)

## Canonical package

Primary package: `oracle`

Capabilities:
* OTEL runtime helpers for run/span/step/event emission
* adapter surfaces for the Evidence-First DSA workflow tools
* materializers that reconstruct ordered steps and outcomes

## Workflow surfaces

* VS Code + Codex-IDE: coding, debugging, test runs
* Marimo + ACP: notebook execution and evidence surfacing

Both surfaces share one OTEL config model and one schema contract.

## Evidence-First DSA workflow

Tool stack:
* `pytest`, `hypothesis`
* `snoop`, `birdseye`
* `hunter`, `viztracer`
* `coverage`, `pytest-cov`

Reference:
* `docs/evidence_first_dsa_workflow.md`
* `docs/otel_migration/schema.md`
* `docs/otel_migration/schema_contract.json`

## Deprecated packages

`oracle_api` and `oracle_tools` are deprecated and retained only for migration
compatibility during cutover. New docs, setup, and imports should target
`oracle`.
