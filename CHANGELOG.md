# Changelog

## v1.1.1 — Governance Quality Closure and Evidence Coverage Hardening

This maintenance increment uses the v1.1.0 governance quality report as an executable backlog and closes all reported assurance-readiness findings.

### Changed

- Updated 491 structured term artifacts under `glossary/terms/` to improve evidence specificity, provenance coverage, cross-reference coverage, revocation inspectability, and assurance hint alignment.
- Added provenance source notes for terms that had no explicit source references, using the corresponding maintained source definition file as the traceable repository-local authority.
- Added `see_also` relationships for terms that lacked cross-reference coverage, using authority scope, decision point, and domain-specific term relationships.
- Added operational evidence artifacts for governance-supporting and core-operational terms that previously only referenced `definition_change_record`.
- Added revocation-relevant evidence artifacts, including `status_record`, `audit_log`, `verification_log`, and `registry_entry`, for revocation-sensitive terms.
- Raised high-impact informative terms to assurance hints that better reflect their decision relevance.
- Regenerated machine-readable bundles, markdown outputs, Jekyll term pages, term indexes, governance inventory, artifact manifest, and quality report.

### Validation

- Validated 534 governance term files.
- Checked 1034 aliases for collisions.
- Confirmed schema and controlled vocabulary alignment.
- Rebuilt governance bundles and inventories for 534 terms.
- Rebuilt the governance quality report with 0 findings.
- Regenerated 534 Jekyll term pages.
- Confirmed generated JSON artifacts parse successfully.
- Confirmed Python tooling compiles successfully.

### Quality report closure

The quality score improved from `85.6 / 100` to `100.0 / 100` under the current repository quality-report rules. The finding count moved from 987 total findings to 0 total findings.

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
