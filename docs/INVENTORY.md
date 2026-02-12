# Inventory (v0)

## A. Content consumption (green)
- material pulled from build repo via sparse-checkout into `content/material/`
- optional provenance copied to `content/manifest.json`

## B. Execution
- `konch` REPL entrypoint (`just repl`)
- session logging (`.logs/*.ndjson`)

## C. Context helpers (modules)
- `cbia_workbench.observe.algoctrl_adapter`
- `cbia_workbench.repl.eofl` (External-Observer Feedback Loop)
- `cbia_workbench.operators.*`
