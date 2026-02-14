# Oracle Tool Stack and Evidence-First Workflow

This document describes the OTEL-native stack and how it maps to the current
`oracle` layout.

## 1) Core package (`oracle`)

`oracle` is the canonical implementation for evidence-first DSA work:
* OTEL runtime helpers for run/span/step/event emission
* schema-aligned evidence keys and provenance fields
* adapters/materializers for workflow tool outputs

Purpose: one OTEL-native observer language for algorithm transitions, replay,
and comparison.

## 2) Evidence-First DSA tool stack

* `pytest`, `hypothesis`
* `snoop`, `birdseye`
* `hunter`, `viztracer`
* `coverage`, `pytest-cov`

## 3) Canonical Workflow

The canonical workflow is the Evidence‑First DSA Workflow:
* `docs/evidence_first_dsa_workflow.md`

INF1220-specific usage is a direct application of that workflow to
pseudocode-first deliverables.

## 4) Example (DSA + OTEL evidence-first)

Example: stack operations in a course worktree.

1. Define the model
   * State: `items`, `size`
   * Ops: `push`, `pop`
   * Invariants: `inv_size == len(items)`
2. Implement `push` and `pop` minimally.
3. Trace `push, push, pop` with `state_before`/`state_after`.
4. Add one boundary test (pop on empty).
5. Fix the first invariant failure (if any).
6. Summarize in one paragraph: what changed and why it’s safe.

This workflow produces evidence artifacts first, then code/pseudocode follows.

## 5) Deprecated references

`oracle_api` and `oracle_tools` are deprecated and should not be used as the
primary path in new setup or usage docs. Replacement mapping is documented in
`docs/otel_migration/replacement_mapping.md`.
