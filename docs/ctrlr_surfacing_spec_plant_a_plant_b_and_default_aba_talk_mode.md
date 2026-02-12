# ctrlr Surfacing Spec (v0.1) — Plant A / Plant B and Default ABA+Talk Mode

## Purpose
Define the **intended functionality** of:
- **Plant A** (repo-work / packet execution) — deterministic, auditable changes
- **Plant B** (manual external observer) — ABA + interactivity after failures/uncertainty
- **Surfacing** (marimo UI + conventions) — interpreter-rendered learning surface

This is a **behavior/spec document** for how you operate the system (and what the surfacing layer should provide), not a runtime implementation spec.

---

## Canonical paths (locked)
- Worktrees: `.codex/.worktrees/<packet_id>/`
- Packets: `.codex/packets/<packet_id>/`
- Evidence: `.codex/out/<packet_id>/`

---

# 1) Plant A — repo-work (Codex packet execution)

## Intended functionality
Plant A is the **mechanical executor**.
- Receives a bounded packet contract (`contract.json` + `EXEC_PROMPT.md`)
- Executes inside an isolated worktree
- Produces evidence under `.codex/out/<packet_id>/`
- Promotes only when checks pass (tests, budgets, allowed paths)

Plant A is *not* where you “think.” Plant A is where you **apply** a single bounded change.

## Inputs
- `.codex/packets/<packet_id>/contract.json`
  - allowed_paths
  - diff budget
  - test_cmd
  - worktree root
  - allowlists for evidence dirtiness
- `.codex/packets/<packet_id>/EXEC_PROMPT.md`
  - step-by-step tasks

## Outputs (evidence contract)
Under `.codex/out/<packet_id>/`:
- `summary.md`
  - PASS/FAIL, what changed, what was proven
- `raw/uv_sync.txt`
- `raw/pytest.txt`
- `raw/diff.txt` + `raw/diffstat.txt`
- optional: `trace.jsonl` (when a run is executed)

## Success criteria (Plant A)
- Diff touches only allowed_paths
- `uv sync --frozen` passes
- `uv run pytest -q` passes
- Evidence bundle exists and is complete
- One commit on the packet branch (or main if that’s the chosen model)

## Example: Plant A packet for INF1220 “instrument insertion sort”
**Packet contract**
- allowed_paths: `src/inf1220/**`, `tests/**`, `notebooks/**`
- test_cmd: `uv run pytest -q`

**Plant A execution**
1) checkout worktree `.codex/.worktrees/packet-inf1220-insertionsort-trace/`
2) implement exactly the requested instrumentation
3) run tests
4) write `.codex/out/<packet_id>/...`
5) commit

---

# 2) Plant B — external observer (manual)

## Intended functionality
Plant B is the **human-in-the-loop external observer**.
- Triggered *after failure* or *uncertainty*
- You manually consult an LLM (chat/Codex session) for:
  - **ABA (B–A–B)**: one bounded next step
  - **Talk mode**: explain/why/alternatives (interpretation)

No automation required. The output of Plant B is a **bounded plan** that becomes the **next packet**.

## Default mode: ABA + Talk
When Plant B is entered, you do both:
- **ABA mode** (controller output): produce the next bounded action
- **Talk mode** (interactive explanation): clarify “why” and “what else could happen”

### Trigger conditions (enter Plant B)
Enter Plant B when any is true:
- pytest fails
- a ctrlr invariant fails
- you cannot name the next smallest deliverable in ≤ 2–3 minutes

## Plant B inputs (manual evidence capsule)
Take from `.codex/out/<packet_id>/`:
- `raw/pytest.txt`
- `raw/diff.txt` / diffstat
- trace artifact (if present): `trace.jsonl` or excerpt
- contract constraints: allowed_paths + budgets

### Evidence capsule (recommended 8 lines)
1) Intent
2) Failure (exact assertion/error)
3) First bad step (where invariants/trace diverge)
4) Expected invariant
5) Constraints (allowed_paths + diff budget)
6) Next smallest deliverable (your guess)
7) Rollback plan
8) “What would success look like?”

## Plant B outputs
### Output A: Proposal (bounded next action)
One action only:
- what to change
- where to change it
- success criteria
- rollback
- scope boundary (illegal moves)

### Output B: Packet stub (manual)
You translate the Proposal into:
- next packet id
- allowed_paths
- tests
- evidence expectations

## Example: manual ABA after a failure
**Failure:** hypothesis finds counterexample where sort violates permutation invariant

**B1 (Observe):**
- read failing test + minimal input
- inspect trace step where swap occurred

**A (Act):**
- LLM proposes: “fix off-by-one in inner loop; add invariant ‘multiset preserved’ check at each swap step”

**B2 (Observe):**
- new packet executes change
- rerun tests; confirm counterexample disappears
- record delta summary

---

# 3) Surfacing layer (marimo) — intended features

## Goal
Surfacing is the **interpreter-rendered dashboard**.
It turns ctrlr evidence into:
- “what happened?” (step table)
- “why safe?” (invariants)
- “why transitioned?” (guards)
- “what else could happen?” (alternatives)
- “how do I see the flow?” (Mermaid)
- “how do I fix the next smallest thing?” (manual ABA assist)

Everything below is *domain-agnostic* and should work for INF1220/1250/1425/2005/MQT1001.

---

## Feature 1 — Trace Browser (Step Table)
### Description
A sortable/filterable table over steps/spans.

### Inputs
- `trace.jsonl` (or derived step list)

### UI controls
- filter by phase (GEN/STRUCT/SELECT/FLOW/EVAL)
- filter by failed invariants
- search by guard name/action name
- range slider over step index

### Output
- selected step index `k`
- derived view objects (before/after, invariants, guards)

### Example (INF1220: insertion sort)
- filter action: `swap`
- show only steps where guard `j>0` flips false

---

## Feature 2 — Step Inspector (Before/After + Why)
### Description
A panel for the selected step that shows:
- state_before / state_after (key locals)
- guard evaluations (why branch taken)
- invariants (why safe)
- “why transitioned” explanation fields
- alternatives (other outcomes + trigger conditions)

### Example
**Step k:** `compare a[j] < a[j-1]`
- guards: `j>0=True`, `a[j]<a[j-1]=True`
- action: `swap`
- invariant: `multiset_preserved=True`, `prefix_sorted_until_i=True`
- alternatives: “if comparison false → advance i; if j==0 → stop inner loop”

---

## Feature 3 — Mermaid Flow View (Predictive Flow)
### Description
Render a high-level flowchart from steps.

### Controls
- group by phase
- collapse repeated loop edges

### Example
Insertion sort flow:
- outer loop → inner compare/swap loop → terminate inner → advance outer

---

## Feature 4 — Mermaid Calltree View (Recursion / Nested spans)
### Description
Render call structure from spans / parent span ids.

### Example (INF1425: quicksort)
- root span quicksort
  - left recursion
  - right recursion
- highlight where pivot partition invariant first breaks

---

## Feature 5 — Invariant Panel (Failure-first)
### Description
A dedicated panel that answers:
- first failing invariant
- first step index where it fails
- show the local state and action that caused it

### Example
Invariant `partition_left<=pivot` fails at step 41.
- show pivot, bounds, offending element

---

## Feature 6 — Hypothesis Counterexample Panel
### Description
When tests fail with Hypothesis:
- display minimal failing input
- provide a “replay with this input” button
- store the input as a reproducible fixture (optional workflow)

### Example
Minimal failing list: `[2, 1, 1]`
- replay generates trace and focuses step inspector on first divergence

---

## Feature 7 — Replay Controls (Deterministic runs)
### Description
Support deterministic reproduction:
- choose seed
- choose budget
- rerun and regenerate trace

### Example
- set seed `12345`
- budget: `max_iters=500`
- rerun; confirm trace stable

---

## Feature 8 — ABA Assist (manual Plant B helper)
### Description
A panel that helps you assemble the evidence capsule and paste it into an LLM.

### Inputs
- latest `.codex/out/<packet_id>/raw/pytest.txt`
- trace excerpt (last N steps)
- contract constraints (allowed_paths + budget)

### Output
- a preformatted “Evidence Capsule” text block

### Example output (ready to paste)
- Intent / Failure / First bad step / Expected invariant / Constraints / Next micro-step guess / Rollback / Success criteria

---

## Feature 9 — Packet Stub Generator (manual)
### Description
Given a Proposal (from the LLM), help you create the next packet skeleton:
- packet id
- allowed_paths
- diff budget
- test cmd
- evidence expectations

### Output
- directory suggestion: `.codex/packets/<new_packet_id>/`
- minimal `contract.json` fields to fill
- minimal `EXEC_PROMPT.md` structure

---

# 4) End-to-end example (INF1220) — failure → ABA → fix

## Scenario
You implement `selection_sort`, add ctrlr steps, and write a property test.
Hypothesis finds a counterexample.

### Plant A (packet run)
- packet executes implementation/instrumentation
- tests fail
- evidence written to `.codex/out/<packet_id>/`

### Plant B (manual ABA + talk)
- you open surfacing
- invariant panel shows first failing step
- ABA assist generates capsule
- you paste into LLM
- you receive: one bounded fix + success criteria

### Plant A (next packet)
- implement fix and strengthen invariant
- rerun tests; pass
- export Mermaid flow

---

## Operational note
Until Plant B is automated, **the system is still complete**: Plant A provides bounded execution + evidence; Plant B provides bounded decision-making + explanation.

This is the intended default mode for early TELUQ progression: **ABA + talk after failure, otherwise keep shipping packets.**

