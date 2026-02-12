# ctrlr bench (draft) — v0.1 core, surfacing, and gaps

## Purpose
This doc consolidates:
- ctrlr v0.1 tool stack and INF1220 usage
- Plant A / Plant B / surfacing spec
- Open doc/code alignment gaps (from Issue #1)

It is a **behavioral + usage benchmark** for ctrlr: what exists, how to use it, what the surfacing layer should show, and what remains missing.

---

## 0) Canonical paths (locked)
- Worktrees: `.codex/.worktrees/<packet_id>/`
- Packets: `.codex/packets/<packet_id>/`
- Evidence: `.codex/out/<packet_id>/`

---

## 1) ctrlr v0.1 — tool stack

### v0.1 core pieces (exists now)
- **Contracts** (`Lens`, `Span`, `Step`, `RunCapsule`)
  - Stable observer language for algorithms and transitions
  - Core contracts are dataclasses; Pydantic is surface-level (validation at boundaries, observer Proposal schemas)
- **Trace runtime** (`run(...)`, `span(...)`, `step(...)`)
  - Output: JSONL trace (path provided via `jsonl_path`)
  - Uses `contextvars` for nested spans/calltree
- **Control gates** (`require(...)`, `ensure(...)`, `invariant(...)` + `CtrlrError`)
  - Make “why it didn’t break” explicit

### v0.2 planned (not implemented yet) — **P0**
- **Experiment utilities (P0)**: `Budget`, `budget(...)`, `seeded(...)`
  - Bounded runs + deterministic reproduction
- **Visualization (P0)**: `to_mermaid_flow(...)`, `to_mermaid_calltree(...)`
  - Predictive flow + call structure

### Tooling required for coursework — **P0**
- `marimo` — interactive surfacing layer
- `pytest` — mechanical correctness gate
- `hypothesis` — controlled exploration / counterexamples
- `snoop` / `birdseye` — developer-time inspection
- OpenTelemetry (optional) — propagate Lens context via spans (only if you are using spans)

---

## 2) Plant A — repo-work (packet execution)

### Intended functionality
Plant A is the **mechanical executor**.
- Receives a bounded packet contract (`contract.json` + `EXEC_PROMPT.md`)
- Executes inside an isolated worktree
- Produces evidence under `.codex/out/<packet_id>/`
- Promotes only when checks pass (tests, budgets, allowed paths)

Plant A is not where you “think.” Plant A is where you **apply** a single bounded change.

### Inputs
- `.codex/packets/<packet_id>/contract.json`
  - allowed_paths
  - diff budget
  - test_cmd
  - worktree root
  - allowlists for evidence dirtiness
- `.codex/packets/<packet_id>/EXEC_PROMPT.md`
  - step-by-step tasks

### Outputs (evidence contract)
Under `.codex/out/<packet_id>/`:
- `summary.md` (PASS/FAIL, what changed, what was proven)
- `raw/uv_sync.txt`
- `raw/pytest.txt`
- `raw/diff.txt` + `raw/diffstat.txt`
- optional: JSONL trace (path provided via `jsonl_path`)

### Evidence completeness checklist (Plant A)
- Evidence folder must contain:
  - `summary.md`
  - `raw/pytest.txt`
  - `raw/uv_sync.txt`
  - `raw/diff.txt`
  - `raw/diffstat.txt`
- JSONL trace is optional only when a traced program runs (record the actual filename/path used)

### Success criteria (Plant A)
- Diff touches only allowed_paths
- `uv sync --frozen` passes
- `uv run pytest -q` passes
- Evidence bundle exists and is complete
- One commit on the packet branch (or main if that’s the chosen model)

---

## 3) Plant B — external observer (manual)

### Intended functionality
Plant B is the **human-in-the-loop external observer**.
- Triggered after failure or uncertainty
- Manually consult LLM for:
  - **ABA (B–A–B)**: one bounded next step
  - **Talk mode**: explain/why/alternatives

### Default mode: ABA + Talk
When Plant B is entered, do both:
- **ABA mode** (controller output): produce the next bounded action
- **Talk mode** (interactive explanation): clarify “why” and “what else could happen”

**Default loop:** after any failure, build the capsule → ask LLM for one bounded action + success criteria + rollback → convert into next packet.

### Trigger conditions
Enter Plant B when any is true:
- pytest fails
- a ctrlr invariant fails
- you cannot name the next smallest deliverable in ≤ 2–3 minutes

### Evidence capsule (recommended 8 lines)
1) Intent
2) Failure (exact assertion/error)
3) First bad step (where invariants/trace diverge)
4) Expected invariant
5) Constraints (allowed_paths + diff budget)
6) Next smallest deliverable (your guess)
7) Rollback plan
8) “What would success look like?”

### Outputs
**Output A: Proposal (bounded next action)**
- what to change
- where to change it
- success criteria
- rollback
- scope boundary (illegal moves)

**Proposal format (example)**
- Change: fix off-by-one in inner loop
- Where: `<repo-relative-path under allowed_paths>`
- Success: invariant holds for all tests; no new failures
- Rollback: revert last commit
- Illegal moves: no new deps; no changes outside `src/algos/**`

**Output B: Packet stub (manual)**
- next packet id
- allowed_paths
- tests
- evidence expectations

---

## 4) Surfacing layer (marimo) — intended features

### Goal
Surfacing is the **interpreter-rendered dashboard**.
It turns ctrlr evidence into:
- “what happened?” (step table)
- “why safe?” (invariants)
- “why transitioned?” (guards)
- “what else could happen?” (alternatives)
- “how do I see the flow?” (Mermaid)
- “how do I fix the next smallest thing?” (manual ABA assist)

Surfacing starts by selecting a `packet_id`, then auto-loads `.codex/out/<packet_id>/raw/*` and a chosen trace path.

### Feature 1 — Trace Browser (Step Table)
- Sortable/filterable table over steps/spans
- Inputs: JSONL trace (path provided via `jsonl_path`)
- Controls: phase filter, failed invariants, guard/action search, step range
- Output: selected step index `k` + derived view objects

### Feature 2 — Step Inspector (Before/After + Why)
- Show `state_before` / `state_after`
- Guard evaluations (why branch taken)
- Invariants (why safe)
- “why transitioned” fields
- Alternatives + trigger conditions

### Feature 3 — Mermaid Flow View (Predictive Flow)
- Render flowchart from steps
- Controls: group by phase, collapse repeated loop edges
Example (INF1220: insertion sort)
- Flow: outer loop → compare → swap → inner stop → advance i
- Collapsed edges: repeated swap loop becomes one cycle

### Feature 4 — Mermaid Calltree View (Recursion / Nested spans)
- Render call structure from spans / parent span ids
- Highlight first invariant failure step
Example (INF1220: merge sort)
- Root: mergesort
- Children: left recursion, right recursion
- Highlight: first failure at merge step 12

### Feature 5 — Invariant Panel (Failure-first)
- First failing invariant
- First step index where it fails
- Local state + action that caused it
Example (INF1220: insertion sort)
- Invariant: `prefix_sorted_until_i` fails at step 41
- State: `i=5, j=2, a[j]=3, a[j-1]=5`
- Action: `swap`

### Feature 6 — Hypothesis Counterexample Panel
- Show minimal failing case from Hypothesis
- Link to step index where invariant first fails
- Allow re-run with the failing seed
Example (INF1220: insertion sort)
- Counterexample: `[3, 2, 2]`
- First failure: step 9
- Seed: `123456789`

### Feature 7 — Replay Controls (deferred if not implemented)
- Seed selector, budget slider, rerun button
- Regenerate trace at a chosen `jsonl_path`
Example (INF1220: insertion sort)
- Rerun with seed `123456789` and budget `200`
- Output: new trace for comparison

### Feature 8 — ABA Assist (deferred if not implemented)
- Auto-build 8-line evidence capsule from `.codex/out/<packet_id>/raw/*` + trace excerpt
Example (INF1220: insertion sort)
- Capsule auto-fills failing assertion + first bad step
- User edits 1–2 lines before asking LLM

### Feature 9 — Packet Stub Helper (deferred if not implemented)
- Convert Proposal into next packet skeleton (contract + EXEC prompt)
Example (INF1220: insertion sort)
- Generates `contract.json` with allowed_paths + test_cmd
- Generates `EXEC_PROMPT.md` with bounded steps

---

## 5) INF1220 usage guide (pseudocode-first, Python-backed)

### Principle
- Python implementation = verified reference
- Pseudocode = rendered projection of verified logic

### Workflow overview
1) Implement the algorithm in Python.
2) Instrument with ctrlr steps.
3) Prove invariants with pytest (optionally Hypothesis).
4) Render Mermaid flow + calltree.
5) Write pseudocode using the same variable names/structure.

### What to trace (INF1220 mental model)
- For each call/iteration: what changed?
- Why it didn’t break: which invariant held?
- Why the plan transitioned: which guard flipped?
- What else could happen: alternatives

### Step vocabulary (consistent naming)
- `state_before`: minimal locals snapshot
- `guards`: `in_bounds`, `loop_condition`, `found_target`, `queue_nonempty`, `can_swap`
- `action_taken`: `compare`, `swap`, `advance_i`, `push`, `pop`, `visit`, `recurse`, `return`
- `invariants`: prefix sorted / permutation preserved / partition invariant (etc.)
- `alternatives`: next branch if condition differs

### Hypothesis use
- Use for edge cases: duplicates, negatives, already-sorted, empty/singleton, disconnected graphs
- Hypothesis generates input → ctrlr trace → invariants checked in pytest

### Pseudocode mapping discipline
- Same variable names between Python and pseudocode (or a deterministic renaming map)
- Pseudocode blocks correspond to span/step structure
- Use trace to justify each step (invariant = “why safe”; guard = “why transitioned”)

### Minimum daily recipe (repeatable)
- Pick a micro-objective (single function or sub-step)
- Implement and instrument 1–2 key steps
- Add 1 invariant
- Run pytest
- Export Mermaid flow or calltree
- Write a matching pseudocode block

---

## 6) Open gaps / doc-to-code alignment (Issue #1)

### Missing items in `src/ctrlr`
- Experiment utilities: `Budget`, `budget(...)`, `seeded(...)`
- Visualization helpers: `to_mermaid_flow(...)`, `to_mermaid_calltree(...)`

### v0.2 work item
- Add minimal implementations under `src/ctrlr`, with tests and exports (via packets)

### Acceptance criteria
- `Budget`, `budget`, `seeded` available via `ctrlr` package
- `to_mermaid_flow` and `to_mermaid_calltree` available via `ctrlr` package
- Tests cover basic behavior and pass

### Notes / follow-ups
- Keep all docs aligned to dataclass-based core contracts and explicit `jsonl_path` traces
