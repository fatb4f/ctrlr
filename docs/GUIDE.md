# CBIA-Tooling — Technical Usage Guide

## Purpose
`cbia-tooling` is a consumer-side workbench used to **run**, **observe**, and **control** learning/dev work driven by generated materials (typically from `cbia-builder`). It does **not** generate the materials; it consumes them, provides REPL ergonomics, enforces contracts, and captures evidence.

## Control Strategies Implemented
### 1) `/eofl` Gate
A hard gate before non-trivial actions.
- **Observer snapshot**: intent, current state, next smallest deliverable, constraints
- **Pre-action gate**: goal, success criteria, rollback, bounded inputs
- **Post-action update**: outcome, evidence, next step

### 2) External-Observer Feedback Loop
Closed loop:
**Observe → Orient → Decide → Act → Record → Review → Update**
- Observe/Record: session logs, stage events
- Orient/Review: operators/reducers, summaries/metrics
- Decide: `/eofl` gating
- Act: REPL + operator execution
- Update: constraints (tests/contracts), next gate snapshot

## Architecture: Pillars
Code is organized under a single package (`src/cbia_workbench/`) with pillar namespaces.

### P1 — Computation as a System (`p1_compute/`)
- Bootstrap and runtime surfaces (REPL wiring, material loading)
- Material contract verification (shape checks, required files)
- Safety/guardrails (fail-fast checks)

Control lens: **feedforward** (setup) + **saturation** (invariants).

### P2 — Statistics as Inference (`p2_inference/`)
- Pure operators (normalize, summarize, extract)
- Optional metrics/reducers over drill outputs/logs

Control lens: **feedback** (signals from evidence).

### P3 — Control & Adaptation (`p3_control/`)
- `/eofl` gate helpers
- Session logging (NDJSON)
- Observer/stage adapters (optional algoctrl bridge)

Control lens: **feedback controller** + **saturation gates**.

## Directory Layout (Reference)
```text
cbia-tooling/
  content/
    material/              # mounted from cbia-builder (read-only)
    manifest.json          # optional provenance copy

  repl/
    konch.py               # REPL entrypoint

  tools/
    sync_material.py       # populate content/material/
    verify_material.py     # contract checks
    report_logs.py         # optional: summarize NDJSON

  src/
    cbia_workbench/
      p1_compute/
        bootstrap.py
        contracts.py

      p2_inference/
        operators/
          normalize.py
          summarize.py
          extract.py
        metrics/
          simple_metrics.py   # optional

      p3_control/
        eofl/
          gate.py
        logging/
          session_ndjson.py
        observe/
          algoctrl_adapter.py

      shared/
        types.py
        util.py

  tests/
    test_contracts.py
    test_operators_pure.py
    test_logging_schema.py

  docs/
    pillars.md
    workflow.md
```

## Core Workflow
### 1) Sync material from `cbia-builder`
Populate `content/material/` (read-only input).
```bash
just sync
# or
python tools/sync_material.py
```

### 2) Verify contracts (mandatory)
Fail-fast before running drills.
```bash
just verify-material
# or
python tools/verify_material.py
```

### 3) Start controlled REPL
```bash
just repl
```
REPL should:
- load material references
- wire a session logger
- expose EOFL helpers and operators

### 4) Use `/eofl` gate around work
In REPL, run:
- snapshot → pre_action → (do work) → post_action
Ensure each step emits a structured log event.

## Evidence Model (NDJSON)
Logs are **append-only NDJSON**.
Minimum recommended fields per event:
- `ts` (timestamp)
- `session_id`
- `event_type` (e.g. `eofl.snapshot`, `eofl.pre_action`, `stage`, `result`)
- `payload` (structured)

NDJSON is used because it is streamable, tool-agnostic, and easy to post-process.

## Coverage Quantification (Practical)
Score the loop capabilities (0–2 each):
- Observe, Orient, Decide, Act, Record, Review, Update-policy, Saturation
Coverage % = `sum(scores) / (2 * N)`.

Second metric: **evidence completeness**
- snapshot logged
- pre-action logged
- action/stage events logged
- post-action logged
Completeness = fraction present.

## Frictionless Expansion Checks
### Add new operator (target <10 min)
- Add module in `p2_inference/operators/`
- Keep pure (no I/O, no hidden state)
- Add a unit test

### Add new control step (target <15 min)
- Add helper under `p3_control/`
- Emit an event type
- (Optional) add reducer under P2

## Boundaries
`cbia-tooling` does not:
- generate learning materials
- own schemas/renderers/build ledger
Those belong to `cbia-builder`.

## Minimal Guarantees
- Stable pillar entrypoints
- Executable contracts
- Evidence-first logging
- One-way dependency direction: P3 → P2 → P1 (avoid reverse coupling)

