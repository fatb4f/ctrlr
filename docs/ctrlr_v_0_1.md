# ctrlr v0.1.0 — Tool Stack and INF1220 Usage Guide

## 1) New tool stack

### What exists now (Milestone 1 = ctrlr v0.1.0)
**ctrlr** is a minimal, Python-only learning substrate that emits interpreter-level evidence.

**Core pieces**
- **ctrlr contracts (Pydantic)**
  - `Lens`, `Span`, `Step`, `RunCapsule`
  - Purpose: a stable “observer language” for algorithms and their transitions.

- **ctrlr trace runtime**
  - `run(...)`, `span(...)`, `step(...)`
  - Output: `trace.jsonl` (append-only, diffable, replayable)
  - Uses `contextvars` for nested spans/calltree.

- **ctrlr control gates**
  - `require(...)`, `ensure(...)`, `invariant(...)` + `CtrlrError`
  - Purpose: convert “why it didn’t break” into explicit checks.

- **ctrlr experiment utilities**
  - `Budget` + `budget(...)`, `seeded(...)`
  - Purpose: bounded runs + deterministic reproduction.

- **ctrlr visualization**
  - `to_mermaid_flow(...)`, `to_mermaid_calltree(...)`
  - Purpose: render predictive flow and call structure.

### Auxiliary “rocketships” (optional but high signal)
- Optional install groups: `aux` (marimo, pytest, hypothesis, snoop, birdseye), `otel` (OpenTelemetry APIs/SDK).
- Install example: `pip install .[aux]` or `pip install .[otel]`.
- **marimo** (interactive notebook/app surface)
  - Use: step table, Mermaid rendering, replay controls.

- **pytest** (mechanical EVAL gate)
  - Use: correctness checks + regression prevention.

- **hypothesis** (controlled exploration)
  - Use: generate inputs; shrink minimal counterexample.

- **pydantic** (contracts)
  - Use: validate states/results; enforce trace structure.

- **snoop / birdseye** (dev-time introspection)
  - Use: inspect locals/call flow while developing.
  - Note: ctrlr remains the canonical evidence format; snoop/birdseye are “inspection tools.”

- **OpenTelemetry (OTel)** *(optional, later)*
  - Use: propagate `Lens` context via baggage/spans.
  - Keep behind extras; do not require for INF1220.

### How this replaces “tool drift”
- ctrlr = the *stable substrate*
- marimo = the *surfacing layer*
- pytest/hypothesis = the *mechanical gates*
- LLM external observer = reads the *same evidence artifacts* and proposes bounded improvements

---

## 2) INF1220 usage guide (pseudocode-first, Python-backed)

### Goal
INF1220 deliverables may be **pseudocode**, but you will **think, test, and trace** in Python.

**Principle:**
- Python implementation = verified reference
- Pseudocode = rendered projection of verified logic

### Workflow overview
1) **Implement** the algorithm in Python.
2) **Instrument** it with ctrlr steps.
3) **Prove** invariants with pytest (and optionally Hypothesis).
4) **Render** Mermaid flow + calltree.
5) **Write** pseudocode using the same variable names and structure.

### What to trace (the INF1220 mental model)
For each algorithm, you want a trace that answers:
- For each call/iteration: **what changed?**
- Why it didn’t break: **which invariant held?**
- Why the plan transitioned: **which guard flipped?**
- What else could have happened: **alternatives**

#### Step vocabulary (use consistently)
- `state_before`: minimal locals snapshot
  - indices (`i`, `j`), pivot, bounds, current node, visited set size
- `guards`:
  - `in_bounds`, `loop_condition`, `found_target`, `queue_nonempty`, `can_swap`
- `action_taken`:
  - `compare`, `swap`, `advance_i`, `push`, `pop`, `visit`, `recurse`, `return`
- `invariants`:
  - sorting: prefix sorted / permutation preserved / partition invariant
  - search: visited monotone / distance nondecreasing / parent pointers valid
- `alternatives`:
  - next branch if condition differs, next swap choice, alternate recursion branch

### Minimal project layout for INF1220 work
You can do this inside a content repo (e.g., INF_1220) consuming ctrlr.

- `notebooks/` (marimo)
- `src/` (reference implementations)
- `tests/` (pytest + hypothesis)
- `out/` (ignored traces and evidence)

### Example: instrumenting a sorting algorithm
**Intent:** generate a step per important transition, not per CPU instruction.

Instrumentation pattern:
- wrap the whole run in `run(lens=..., jsonl_path=...)`
- create spans per function call (especially recursion)
- emit steps at:
  - loop start
  - key comparisons
  - swaps/mutations
  - recursion entry/exit
  - termination conditions

Then:
- render `to_mermaid_flow(steps)` to see predictive flow
- render `to_mermaid_calltree(steps)` to see recursion structure

### Hypothesis: when to use in INF1220
Use it when the algorithm is sensitive to edge cases:
- sorting (duplicates, negative numbers, already sorted)
- recursion (empty/singleton/base-case)
- graph traversal (disconnected graphs)

Pattern:
- Hypothesis generates input
- algorithm runs under ctrlr trace
- invariant checks in pytest
- failing case becomes a minimal counterexample saved as evidence

### Pseudocode mapping (the key INF1220 move)
Maintain a simple mapping discipline:
- Use identical variable names between Python and pseudocode (or a deterministic renaming map).
- The pseudocode “blocks” correspond to the span/step structure:
  - function header ↔ span entry
  - loop ↔ repeated steps with consistent guard names
  - conditionals ↔ `alternatives`

When writing pseudocode:
- Use the trace to justify each step:
  - “why safe” is your invariant explanation
  - “why transitioned” justifies branch/loop decisions

### What evidence to keep for syllabus progression
Per objective/topic:
- one `trace.jsonl`
- one Mermaid flow diagram
- one pytest run output
- optional minimal counterexample

This is sufficient to show real, measurable progression.

---

## Daily INF1220 execution template (10–20 minutes)
1) Pick one micro-objective (single algorithm or sub-part).
2) Implement/refine one function.
3) Add/adjust one invariant.
4) Run tests.
5) Save trace + Mermaid.
6) Write 3–6 lines of pseudocode aligned to the trace.

---

## External observer hook (optional, high signal)
When stuck:
- provide the trace + failing invariant to the observer
- request one bounded next action:
  - “add missing guard”
  - “tighten invariant”
  - “reduce state snapshot noise”
  - “produce a minimal counterexample”

Output should be a Proposal (single change) and success criteria.
