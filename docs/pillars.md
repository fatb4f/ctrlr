# Pillar layout

This repo is organized around three pillars:

- **P1 — Computation as a System** (`src/cbia_workbench/p1_compute/`)
  - bootstrap surfaces (REPL + material loading)
  - consumer-side contracts (material presence, manifest presence)

- **P2 — Statistics as Inference** (`src/cbia_workbench/p2_inference/`)
  - pure operators and small evaluation helpers (no I/O, no environment)

- **P3 — Control & Adaptation** (`src/cbia_workbench/p3_control/`)
  - external-observer / stage adapters
  - EOFL gate helpers
  - session logging (NDJSON event stream)

## Compatibility

Legacy import paths remain available for now:

- `cbia_workbench.operators.*` → `cbia_workbench.p2_inference.operators.*`
- `cbia_workbench.observe.*` → `cbia_workbench.p3_control.observe.*`
- `cbia_workbench.repl.*` → `cbia_workbench.p1_compute` and `cbia_workbench.p3_control`

Prefer the pillar namespaces for all new code.
