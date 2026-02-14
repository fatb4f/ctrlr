# OTEL Runtime Configuration (M2)

The `oracle` runtime reads standard OTEL-style environment variables for trace
configuration:

- `OTEL_TRACES_EXPORTER`: `none`, `console`, or `otlp`
- `OTEL_SERVICE_NAME`: service name for resource `service.name`
- `OTEL_EXPORTER_OTLP_ENDPOINT`: OTLP endpoint for `otlp` exporter mode
- `OTEL_RESOURCE_ATTRIBUTES`: comma-separated `key=value` pairs

The runtime always emits schema-aligned keys for Evidence-First DSA spans and
events, including:

- span attrs: `oracle.evidence.schema_version`, `oracle.run_id`, `oracle.seq`
- one-of span attrs: `oracle.variant_id` or `oracle.run_label`
- event attrs for guards/invariants/explanations as defined in
  `docs/otel_migration/schema_contract.json`

Provenance:

- VS Code/editor provenance: `code.filepath`, `code.lineno` (when present)
- Marimo provenance: `oracle.notebook_id`, `oracle.cell_id`
