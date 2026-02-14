# Dev Flow

This repo is a monorepo organized with worktrees. Day-to-day work happens in the
non-`main` worktrees, while `main` stays clean and PR-gated.

Terminology:
* A **worktree** is a checkout location tied to a branch.
* `courses/<course>/...` is a content subtree inside that checkout.

## Working Environment

The stack is:
1. VS Code + Codex-IDE extension
2. Marimo + `codex-cli` `acp-ext`
3. OTEL-native `oracle` package + workflow tools

This stack is stable even as the specific workflow evolves.

## VS Code Workflow

Open the worktree you intend to modify as your workspace root in VS Code.

* Debugging runs from the selected worktree.
* Breakpoints and tests execute in that worktree context.
* Automation should only produce diffs; VS Code handles the interactive loop.

### Multi-root (runtime + content)

When runtime and course content live in different worktrees, use a multi-root
workspace.

Recommended setup:
* Add both folders to the workspace:
  * `../oracle-runtime`
  * `../oracle-inf2220`
* Save a workspace file (for example `oracle.code-workspace`).

Practical defaults:
* Set the Python interpreter to the runtime worktree environment.
* Use the course folder as the working directory for Marimo/notebook runs.
* Run tests and launch configs from the runtime folder; reference course files by
  relative path.

## Marimo Workflow

Use Marimo for exploratory or instructional content tied to a specific course.

* Run Marimo from the relevant course worktree (for example `oracle-inf2220`).
* Keep notebook assets scoped to the course directories.
* Promote stable runtime/adapter/materializer code into `packages/oracle`.

## Worktree Checklist

* Choose the worktree that matches the intent (`runtime` or a course).
* Run tests and debugging in that worktree.
* Merge only via PR into `main`.

Deprecated package note:
* `oracle_api` and `oracle_tools` are migration-only and not the primary target
  for new development.
