## v1.3.0 - Publication Integrity & Contributor Onboarding

This release contains no schema or vocabulary changes. It closes first-impression integrity gaps and improves the external contribution path for a standards-adjacent glossary.

### Fixed

- README now reports the generated 563-term quality posture instead of the stale 534-term count.
- Added a CI guard that fails when README quality posture drifts from `generated/json/governance-quality-report.json`.
- Updated GitHub Pages configuration to match the canonical `trustoverip/ctwg-main-glossary` repository.
- Removed the duplicated `docs/governance/` mirror; `governance/` is the single maintainer-authored source.
- Removed legacy spec-up workflow, script, and backup files while preserving `spec/terms-definitions/` as repository-local source evidence.

### Added

- `CODEOWNERS`, `CODE_OF_CONDUCT.md`, and `CITATION.cff`.
- Issue templates for term proposals and generated quality findings.
- Pull request template aligned with source, generated artifact, and downstream-impact checks.
- README badges and a downstream consumer quickstart for generated JSON and JSON-LD artifacts.

### Compatibility

No terms were renamed, removed, or reshaped. No schema changes were made. Downstream JSON and JSON-LD consumers remain compatible.
