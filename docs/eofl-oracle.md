# EOFL Oracle (standby)

EOFL ("end of fixed loop") is defined in this repo as a **technical process playbook** for disciplined iteration and evidence capture.
In the current repo state, EOFL **does not run as an in-repo controller** and is **on standby** until the workflow is stabilized.

Until then, the active capability is a **minimal external observer loop** implemented using:

- **VS Code + Codex IDE** (primary repo observation, navigation, explanations, bounded edit suggestions)
- **marimo + ACP** (interactive analysis surface; executable notebooks; agent-assisted exploration)
- normal **Python test/debug** workflow in VS Code

This document defines the **playbook-entities** and the **minimal EOFL environment** needed to operate EOFL-in-standby.

---

## Playbook-entities (canonical)

These entities are the stable “process API”. External operators/tools may store state and evidence elsewhere.

### Target
A concrete working directory (typically a git worktree) and its constraints.

- `worktree`: path + branch
- `allowed_paths`: list of repo-relative path prefixes
- `forbidden_outputs`: files/folders that must not appear in git status
- `verification`: commands that must pass (e.g. `pytest`, linters)

### PlanCard
The smallest unit of intent that is safe to attempt.

- `intent`: one sentence
- `success_criteria`: 3–7 bullet checks
- `scope`: allowed paths + explicit non-goals
- `rollback`: how to revert safely
- `stop_rules`: time cap, iteration cap, “same failure twice”, etc.

### Observation
A recorded answer to a specific question about the repo state.

- `question`
- `finding` (short)
- `references` (files/lines, commands, outputs)

### Proposal
A bounded change suggestion (may or may not be applied by an external operator).

- `diff_summary` (what changes and why)
- `files_touched`
- `risk_notes`
- `verification_plan`

### EvidenceRef
A pointer to externally-stored evidence (no required storage location).

- `test_run`: command + result
- `trace_or_log`: reference id/path
- `coverage`: report pointer (optional)
- `repro_case`: minimal failing input (optional)

### Decision
The end-of-loop outcome.

- `status`: continue | stop | rescope
- `why`
- `next_plan`: next PlanCard id/title

---

## Minimal EOFL environment (Codex + VS Code + marimo)

### Required
1. **VS Code**
   - Python extension configured to use the repo virtualenv
   - Codex IDE extension installed and authenticated

2. **Python toolchain**
   - one reproducible environment setup for running tests (uv/venv)

3. **marimo**
   - runnable notebooks for analysis (in-repo or adjacent)
   - ACP configured for an agent connection (read-only or bounded-edit)

### Observer-mode operating rules
- **Default to read/observe**: ask questions, locate files, explain failures.
- **Edits are always bounded**: declare allowed paths + success criteria before applying.
- **Verification is mandatory**: every applied change must include a test run.
- **Evidence is referenced, not stored here**: record `EvidenceRef` pointers in PR/issue text.

---

## Minimal loop (observer-first)

Use this as the default day-to-day workflow while EOFL is on standby.

1. **Select Target**
   - choose worktree (`api`, `tools`, or a course worktree)
   - confirm a clean baseline (`git status`)

2. **Write a PlanCard**
   - intent + success criteria + scope + stop rules

3. **Collect Observations (Codex IDE)**
   - ask: “where is X implemented?”, “why is this failing?”, “what are invariants here?”

4. **Produce a Proposal**
   - diff summary + touched files + verification plan

5. **Apply change (optional)**
   - manual edit or external operator (not specified here)

6. **Verify**
   - run the verification commands from Target

7. **Capture EvidenceRef**
   - tests + any traces/coverage pointers

8. **Make a Decision**
   - continue / stop / rescope, and the next PlanCard

---

## When EOFL leaves standby

EOFL can be promoted from “observer loop” to “controller loop” once:

- there is a stable, repeatable workflow for bounded edits
- evidence capture has stable identifiers and locations (operator-owned)
- the repo’s branch/worktree discipline is consistently enforced

At that point, this document should be updated to specify the controller interface and validation rules.
