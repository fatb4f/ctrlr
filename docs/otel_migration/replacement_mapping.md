# Replacement Mapping

This page defines the canonical package replacement mapping for OTEL migration.

## Primary package

Use `oracle` for new setup, imports, runtime instrumentation, adapters, and
materializers.

## Legacy to replacement mapping

* `oracle_tools` -> `oracle`
  * replacement scope: OTEL-native adapters/materializers/helpers
* `oracle_api` -> `oracle`
  * replacement scope: OTEL schema/runtime instrumentation surfaces

## Status labels

* `oracle` = active/canonical
* `oracle_api` = deprecated, migration-only
* `oracle_tools` = deprecated, migration-only

## Cutover rule

Docs, examples, and setup guides must present `oracle` as the only primary
workflow path. Legacy packages may be referenced only in explicitly deprecated
migration notes.
