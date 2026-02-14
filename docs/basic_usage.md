# Basic Usage

## Layout

Primary paths inside `oracle`:

```text
packages/
  oracle/
    src/oracle/...
integration/
docs/
courses/
pyproject.toml
```

Legacy migration paths (deprecated, non-primary):

```text
packages/oracle_api/
packages/oracle_tools/
```

## Dependency rules

* New runtime, adapters, and materializers import from `oracle`.
* New docs and examples must use `oracle` as the canonical package.
* References to `oracle_api` and `oracle_tools` are allowed only as explicitly
  deprecated migration context.

## Worktrees

Suggested branches:

```text
WT         Branch
main       main
runtime    work/oracle-runtime
course     course/<course-id>
```

Bootstrap:

```bash
git clone git@github.com:<owner>/oracle.git oracle-main
cd oracle-main
git checkout main

git worktree add ../oracle-runtime -b work/oracle-runtime main
git worktree add ../oracle-course  -b course/inf2220 main
```

Operational rule:

* Develop in non-`main` worktrees and merge to `main` through PRs.

## Evidence-First DSA Workflow tools

* `pytest`, `hypothesis`
* `snoop`, `birdseye`
* `hunter`, `viztracer`
* `coverage`, `pytest-cov`

These tools feed OTEL-linked evidence emitted and materialized through
`packages/oracle/src/oracle`.
