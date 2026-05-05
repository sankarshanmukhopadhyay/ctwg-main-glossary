# Changelog

## v1.1.0 — Assurance-Ready Governance Glossary Infrastructure

This release advances the glossary from a structured publication into assurance-ready governance infrastructure.

### Added

- Controlled vocabulary file at `schemas/governance-vocabularies.yaml`.
- Schema-aligned examples under `examples/governance-term/`.
- Governance quality report generator: `tools/build_quality_report.py`.
- Generated quality report artifacts:
  - `generated/json/governance-quality-report.json`
  - `generated/markdown/governance-quality-report.md`
  - `governance/quality-report.md`
- Generated artifact manifest:
  - `generated/json/artifact-manifest.json`
  - `generated/markdown/artifact-manifest.md`
- Term authoring guide.
- Assurance model documentation.
- Downstream consumption guidance.

### Changed

- Strengthened `schemas/governance-term.schema.json` with controlled enums, minimum lengths, and array uniqueness constraints.
- Updated validation to use JSON Schema plus repository-specific integrity checks.
- Updated CI workflows to install `jsonschema`, build the quality report, and fail on generated drift.
- Refreshed README, artifact documentation, governance docs, publication docs, quality rubric, and roadmap.
- Deprecated old reduced-shape governance-profile examples in favor of schema-aligned term examples.

### Validation

- Validates all structured term files under `glossary/terms/`.
- Confirms schema and controlled vocabulary alignment.
- Regenerates JSON, JSON-LD, markdown, inventory, quality-report, manifest, Jekyll term pages, and term indexes.
- Preserves GitHub Pages compatibility with Jekyll and Just the Docs.
