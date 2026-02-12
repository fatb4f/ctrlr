# INF1220 — TP1 Drill Bank (M1-aligned)
_Generated: 2026-01-15_

## Objectives (from `cbia-content/inf1220/objectives/tp1.extracted.json`)
- **INF1220-TP1-O-01**: Design an efficient pseudocode algorithm to decide whether an array’s element-sum **exceeds 100**, using **early termination** and handling edge cases (empty array, extremely large array).
- **INF1220-TP1-O-02**: Produce **precise, readable, language-agnostic pseudocode** with clear inputs, variables, and outputs.
- **INF1220-TP1-O-03**: Execute pseudocode **line-by-line** and report variable values at each step.
- **INF1220-TP1-O-04**: Diagnose and explain a **logical error** in provided pseudocode (FizzBuzz variant) and provide a corrected version.
- **INF1220-TP1-O-05**: Compare executions of original vs corrected pseudocode and summarize iteration behavior to highlight differences.

---
## Conventions used in this drill bank
- Arrays are written like `[55, 55, 55]`.
- Assignment: `<-`
- Boolean values: `true / false`
- Modulo: `a % b` = remainder of Euclidean division.
- Loop template:
```text
sum <- 0
FOR each x IN A DO
    sum <- sum + x
END FOR
```

---
## O-01 — Early-termination sum>100 algorithm (10 drills)
### Drill 1 — Output only
**Task:** For each array `A`, return `true` iff `sum(A) > 100` (strictly greater). Use early termination when possible.
- A1 = `[]`
- A2 = `[100]`
- A3 = `[101]`
- A4 = `[55, 55, 55, 55]`
- A5 = `[1, 2, 3, 5, 6]`

**Answer:** A1 `false`, A2 `false`, A3 `true`, A4 `true` (stop after 2 elems), A5 `false`.
### Drill 2 — Minimal pseudocode
**Task:** Write pseudocode for `EXCEEDS_100(A)` returning `true/false` with early termination.

**Answer (one valid solution):**
```text
Inputs:
    A: array of positive integers
Variables:
    sum: integer <- 0
    x: integer
Output:
    boolean

FOR each x IN A DO
    sum <- sum + x
    IF sum > 100 THEN
        RETURN true
    END IF
END FOR
RETURN false
```
### Drill 3 — Big-array reasoning
**Task:** Explain (1 sentence) why early termination matters if `A` can have 10^12 elements.

**Answer:** Without early termination you may need to read all 10^12 items; early termination can stop after a small prefix once `sum > 100`.
### Drill 4 — Trace until termination
**Task:** Trace `sum` and stopping point for `A = [40, 30, 50, 1]`.

**Answer:** sums: 40 → 70 → 120; return `true` after processing the 3rd element.
### Drill 5 — Edge case: exactly 100
**Task:** For `A = [60, 40, 999]`, what happens with early termination?

**Answer:** sum hits 100 at 2nd element (not >100, continue), then becomes 1099 at 3rd element → return `true` after 3rd.
### Drill 6 — Constraint change
**Task:** If the requirement becomes `sum(A) >= 100`, what single change is needed?

**Answer:** Replace `sum > 100` with `sum >= 100`.
### Drill 7 — Invariant (1 line)
**Task:** State a loop invariant for the algorithm in Drill 2.

**Answer:** After processing `k` elements, `sum` equals the sum of the first `k` elements of `A`.
### Drill 8 — Worst-case inputs
**Task:** Give an example of an array where early termination gives **no** savings.

**Answer:** Any array whose total sum ≤ 100, e.g., `[1,1,1,...]` with sum 100 or less; you must read all elements.
### Drill 9 — Best-case inputs
**Task:** Give an example of an array where early termination gives maximum savings.

**Answer:** `[101, ...]` — returns `true` after the first element.
### Drill 10 — Guard against overflow (conceptual)
**Task:** If numbers can be very large, name one safe strategy (no need to code).

**Answer:** Check `sum > 100` before adding by using a bound (e.g., if `sum > 100 - x` then return true), or use a numeric type that can’t overflow for the expected data.

---
## O-02 — Pseudocode precision & readability (6 drills)
### Drill 1 — Identify what’s missing
**Task:** What’s missing from this pseudocode header?
```text
sum <- 0
FOR each x IN A DO
    sum <- sum + x
END FOR
RETURN sum > 100
```

**Answer:** Inputs/outputs are not declared; variable types/meaning aren’t stated; function name is missing.
### Drill 2 — Make it language-agnostic
**Task:** Rewrite this line to be language-agnostic: `for (int i=0; i<A.length; i++)`.

**Answer:** `FOR i from 0 to length(A)-1 DO`.
### Drill 3 — Remove ambiguity
**Task:** Rewrite “repeat until it’s big enough” as a precise condition for the sum>100 problem.

**Answer:** “Repeat until `sum > 100`.”
### Drill 4 — Naming
**Task:** Replace variable names to improve clarity: `s`, `t`, `x`.

**Answer:** `sum`, `array`, `value` (or similar meaningful names).
### Drill 5 — Precondition statement
**Task:** Add a precondition for inputs to avoid hidden assumptions.

**Answer:** `A is an array of positive integers` (or specify allowed negatives if permitted).
### Drill 6 — Output clarity
**Task:** Make the output explicit: returning a boolean should be stated how?

**Answer:** Add `Output: boolean` and use `RETURN true/false`.

---
## O-03 — Tracing pseudocode (6 drills)
### Drill 1 — Trace table
**Task:** Trace the loop.
```text
sum <- 0
A <- [55, 55, 10]
FOR each x IN A DO
    sum <- sum + x
    IF sum > 100 THEN
        RETURN true
    END IF
END FOR
RETURN false
```
Fill `(x, sum)` per iteration and stop when it returns.

**Answer:** (55,55) → (55,110) then returns `true` on 2nd iteration.
### Drill 2 — Off-by-one check
**Task:** Trace `i`.
```text
i <- 0
WHILE i < 3 DO
    i <- i + 1
END WHILE
```
What is `i` at the end?

**Answer:** `3`.
### Drill 3 — Condition flip
**Task:** Trace and decide output.
```text
x <- 10
IF NOT (x > 5 AND x < 9) THEN
    print("A")
ELSE
    print("B")
END IF
```

**Answer:** prints `A`.
### Drill 4 — Nested conditional trace
**Task:** Trace output.
```text
x <- 15
IF x % 3 == 0 THEN
    print("Fizz")
    IF x % 5 == 0 THEN
        print("Buzz")
    END IF
END IF
```

**Answer:** prints `Fizz` then `Buzz`.
### Drill 5 — Array indexing trace
**Task:** Trace `sum`.
```text
A <- [1,2,3,4]
sum <- 0
FOR i from 0 to length(A)-1 DO
    sum <- sum + A[i]
END FOR
RETURN sum
```

**Answer:** `10`.
### Drill 6 — Early termination trace
**Task:** How many loop iterations execute?
```text
A <- [99, 2, 50]
sum <- 0
FOR each x IN A DO
    sum <- sum + x
    IF sum > 100 THEN RETURN true END IF
END FOR
RETURN false
```

**Answer:** 2 iterations (99→101 then stop).

---
## O-04 — Debugging a FizzBuzz variant (5 drills)
### Drill 1 — Spot the logical bug (ordering)
**Task:** What is wrong?
```text
IF n % 3 == 0 THEN
    print("Fizz")
ELSE IF n % 5 == 0 THEN
    print("Buzz")
ELSE IF n % 15 == 0 THEN
    print("FizzBuzz")
ELSE
    print(n)
END IF
```

**Answer:** The `n % 15 == 0` case is unreachable because any multiple of 15 matches `%3==0` first.
### Drill 2 — Correct it
**Task:** Provide a corrected version (minimal change).

**Answer:** Check `%15` first:
```text
IF n % 15 == 0 THEN
    print("FizzBuzz")
ELSE IF n % 3 == 0 THEN
    print("Fizz")
ELSE IF n % 5 == 0 THEN
    print("Buzz")
ELSE
    print(n)
END IF
```
### Drill 3 — Another common bug (wrong operator)
**Task:** Why is this wrong?
```text
IF n % 3 == 0 OR n % 5 == 0 THEN
    print("FizzBuzz")
END IF
```

**Answer:** It prints `FizzBuzz` for multiples of 3 *or* 5, but `FizzBuzz` should be only multiples of both (15).
### Drill 4 — Fix the operator
**Task:** Fix the condition.

**Answer:** Use `AND` or `%15==0`:
`IF (n % 3 == 0) AND (n % 5 == 0) THEN ...`
### Drill 5 — Explain in 2 sentences
**Task:** Explain the nature of the bug in Drill 1.

**Answer:** The bug is **logical**: the program structure makes the intended case impossible to reach. The condition order must reflect specificity (most specific first).

---
## O-05 — Compare executions (3 drills)
### Drill 1 — Compare outputs for n=15
**Task:** Original (buggy) from O-04 Drill 1 vs corrected. What does each print for `n=15`?

**Answer:** Buggy prints `Fizz`; corrected prints `FizzBuzz`.
### Drill 2 — Summarize behavior over 1..15
**Task:** In one sentence, describe the difference over `n = 1..15`.

**Answer:** The buggy version never produces `FizzBuzz`; the corrected version produces `FizzBuzz` exactly at multiples of 15.
### Drill 3 — Iteration-level summary (no full trace)
**Task:** For the corrected version, list the special outputs (non-numbers) from 1..16.

**Answer:** `3:Fizz, 5:Buzz, 6:Fizz, 9:Fizz, 10:Buzz, 12:Fizz, 15:FizzBuzz`.

---
## Optional: Math recall drills that directly support TP1 (10 drills)
1. Evaluate `NOT (P AND Q)` for `P=true, Q=false` → **true**.
2. Rewrite `NOT (A OR B)` → **(NOT A) AND (NOT B)**.
3. Compute `17 % 5` → **2**.
4. Condition “odd” → `n % 2 != 0`.
5. Condition “in [10..20]” → `10 <= n AND n <= 20`.
6. If `sum` is 95 and next `x` is 10, will `sum + x > 100`? → **true**.
7. If `A=[]`, what is `sum(A)` by convention? → **0**.
8. If `sum` already 101, should you read more elements? → **no** (early terminate).
9. State loop invariant for accumulator sum → **sum equals sum of processed prefix**.
10. De Morgan: `NOT (x>0 AND y>0)` → **(x<=0) OR (y<=0)**.
