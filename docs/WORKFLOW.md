# Trunk-Based Worktrees Workflow

## Purpose

This document defines the **canonical development and collaboration workflow** for this repository.

The workflow is:

* **Trunk-based** at the collaboration level
* **Worktree-based** at the local execution level
* **PR-gated** for any non-trivial change

Worktrees are treated as a **local ergonomics and isolation layer**, not as a branching model.

---

## Core Principles

1. **`main` is always releasable**

   * No broken builds, failing checks, or incomplete work on trunk.
   * `main` must always fast-forward cleanly.

2. **Short-lived work units**

   * All non-trivial work is scoped into small, mergeable packets.
   * Long-lived branches and large diffs are explicitly avoided.

3. **Deterministic collaboration**

   * Codex and human contributors operate under explicit scope and guardrails.
   * All merges are gated by mechanical checks.

4. **Local isolation, global simplicity**

   * Multiple worktrees are allowed locally.
   * The shared repository history remains linear and readable.

---

## Roles

### Maintainer (Human)

* Defines intent and acceptance criteria
* Approves and merges PRs
* Owns trunk quality and release readiness

### Codex (Automation)

* Operates only inside an assigned worktree and branch
* Produces bounded, auditable diffs
* Never commits directly to `main`

---

## Units of Work

### Packet

A **packet** is the smallest unit of work that:

* Can be merged independently
* Improves the repository state
* Has clear scope, success criteria, and rollback

Packets are expected to be:

* Small
* Reviewable
* Deterministic

---

## Branch Naming

All packet branches MUST follow this format:

```
pkt/<area>/<id>-<slug>
```

Examples:

* `pkt/pipeline-sre/012-control-map-gate`
* `pkt/content-gen/031-inf1220-m1-07-drills`

---

## Worktree Layout (Local)

The canonical layout is:

```
repo/                    # trunk worktree (main)
repo--pkt-012-foo/        # packet worktree
repo--review/             # optional review worktree
```

* `repo/` always tracks `main`
* Packet worktrees are disposable

---

## Creating a Packet Worktree

From the trunk worktree:

```bash
git worktree add -b pkt/<area>/<id>-<slug> ../repo--pkt-<id>-<slug> origin/main
```

Rules:

* One active Codex packet worktree at a time
* Parallelism is achieved by queueing packets, not concurrent mutation

---

## Packet Lifecycle

### 0. Define the Packet (Pre-work Gate)

Each packet MUST define:

* **Intent**: what is changing and why
* **Success criteria**: verifiable outcomes
* **Boundaries**:

  * allowed paths
  * forbidden outputs
  * diff budget
* **Rollback**: how to revert safely

This gate is required before Codex execution.

---

### 1. Implement in Packet Worktree

* All changes occur inside the packet worktree
* Commits may be granular
* Worktree must remain within declared boundaries

---

### 2. Mechanical Checks (Mandatory)

Before PR creation, the packet branch MUST pass:

* Formatting and linting
* Tests (if applicable)
* Schema and invariant validation
* Control / assurance / OPA gates (if applicable)
* Regeneration and drift checks (where required)

Failure at this stage blocks the packet.

---

### 3. Pull Request

PR requirements:

* Title: `pkt(<area>): <slug>`
* Description includes:

  * packet intent
  * scope summary
  * evidence artifacts
  * explicit success verification

---

### 4. Merge Policy

* **Squash merge** is the default
* Merge commits are allowed only when multi-commit history is meaningful
* `main` must fast-forward cleanly after merge

---

### 5. Cleanup

After merge:

```bash
git worktree remove ../repo--pkt-<id>-<slug>
git worktree prune
```

* Delete packet branch
* Pull `main` with `--ff-only`

---

## Direct Trunk Edits

Edits MAY be made directly on `main` ONLY if:

* Change duration is <5 minutes
* No structural or behavioral impact
* No Codex involvement

Otherwise, a packet is required.

---

## Concurrency Policy

* Maximum one active Codex packet at a time
* Optional review worktrees are allowed
* Conflicting packets must be serialized

---

## Enforcement

This workflow is enforced via:

* Human review
* Preflight scripts
* CI gates
* Policy / assurance checks

Non-conforming changes must be rejected.

---

## Rationale

This workflow:

* Preserves trunk-based simplicity
* Enables parallel local contexts without branch switching
* Makes Codex collaboration safe and auditable
* Keeps repository history linear and readable

It is intentionally conservative by default and optimized for correctness and clarity over raw throughput.
