# Configuration and Settings

This document defines the local setup for development and learning work in the
`oracle` monorepo.

## 1) Python venv

Create and activate a virtual environment in the active worktree.

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
```

Install the OTEL-native runtime package from repo root:

```bash
python -m pip install -e packages/oracle
```

Optional OTEL exporter extras:

```bash
python -m pip install -e "packages/oracle[otel]"
```

## 2) VS Code + Extensions

Required:
* VS Code
* Codex-IDE extension

Recommended:
* Python extension
* Pylance

Settings (workspace or user):
* Default interpreter: the `.venv` inside the worktree you are actively using
* Terminal activates venv automatically

## 3) Marimo + ACP

Install Marimo in the active venv:

```bash
python -m pip install marimo
```

Use the `codex-cli` ACP extension when running Marimo so the notebook is aware
of the Codex workflow.

## 4) Codex for Marimo and VS Code

* VS Code uses Codex-IDE for interactive coding + debugging.
* Marimo uses `codex-cli` `acp-ext` for notebook workflows and evidence capture.

Keep these roles stable:
* VS Code is the primary debugger and test runner.
* Marimo is the evidence surfacing and explanation surface.

## 5) OTEL runtime config

Set exporters via environment variables:

```bash
export OTEL_TRACES_EXPORTER=console
export OTEL_SERVICE_NAME=oracle
export OTEL_RESOURCE_ATTRIBUTES=deployment.environment=dev,service.namespace=oracle
```

OTLP example:

```bash
export OTEL_TRACES_EXPORTER=otlp
export OTEL_EXPORTER_OTLP_ENDPOINT=http://localhost:4318
```

## 6) Evidence-First DSA Workflow tools

Optional debugging tools (install only if needed):
* `pytest`
* `hypothesis`
* `snoop`
* `birdseye`
* `hunter`
* `viztracer`
* `coverage`
* `pytest-cov`

Add these to the venv when you are ready to use them:

```bash
python -m pip install pytest hypothesis snoop birdseye hunter viztracer coverage pytest-cov
```

## 7) Deprecated packages

`oracle_api` and `oracle_tools` are deprecated. Do not use them as primary
install/import targets in new workflows. See
`docs/otel_migration/replacement_mapping.md` for migration mapping.
