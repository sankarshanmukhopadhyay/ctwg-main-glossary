# Changelog

## v2.0.0 — Trust Infrastructure Glossary independence and concept model

v2.0.0 establishes the Trust Infrastructure Glossary as an independent project with its own semantic authority, source-intake governance, stable concept identifiers, concept/designation separation, provenance classifications, SKOS-aligned relations and mappings, vocabulary profiles, and canonical JSON/JSON-LD/Turtle artifacts.

### Added

- stable `urn:tig:concept:*` identifiers across all 612 concepts
- language-tagged designation objects and editorial maturity
- adopted/adapted/locally-defined/mapped provenance model
- semantic relation and cross-vocabulary mapping structures
- source-intake, lineage, semantic-model, and profile governance
- SKOS-compatible Turtle generation
- canonical TIG JSON and JSON-LD bundles
- three validated vocabulary profiles
- v2 migration guide

### Changed

- reorganized GitHub Pages around reader tasks: Explore Concepts, Use TIG, Govern TIG, and Project
- grouped governance documentation into semantic authoring, assurance/quality, and operations/evolution
- changed generated concept pages to present meaning and relationships before implementation metadata
- moved detailed governance, assurance, control-plane, evidence, and crosswalk metadata into progressive disclosure
- added profile and section landing pages so navigation no longer mirrors repository folders
- project identity from ToIP Main Glossary fork to Trust Infrastructure Glossary
- ToIP from governing upstream to attributed source corpus
- generated concept pages to expose identity, designations, provenance, relations, and mappings
- Pages, package, citation, README, and contribution metadata for the new repository identity
- `term` and `aliases` retained only as compatibility fields alongside the authoritative v2 concept/designation model

### Removed

- upstream drift monitor and synchronization workflows
- upstream checkpoint state, templates, and policy validator
- obsolete Spec-Up runtime scaffolding no longer used by the Jekyll/Python publication pipeline

### Compatibility

v2 is a breaking semantic-contract release. Legacy artifact filenames remain generated in v2.0.0 to support staged consumer migration.


## v1.5.0 — Reader Comprehension, Information Architecture, and Portfolio Vocabulary

v1.5.0 makes the governance-executable glossary substantially easier to enter and use without weakening its precise or machine-readable semantics.

## Added

- Added optional `simple_definition` to the term schema as a curated plain-English comprehension layer.
- Updated generated term pages to show **In Simple English** before the formal definition.
- Added `start-here.md` as a task-oriented entry point.
- Added `concepts.md` to browse terminology by authority/governance, agents/delegation, assurance/interoperability, risk/harms/redress, and recognition/registries.
- Added `governance/plain-language-guide.md` with editorial rules and an incremental migration strategy.
- Added 13 cross-project terms identified from active portfolio work: `conformance`, `interoperability`, `redress`, `recognition`, `assurance boundary`, `governance legitimacy`, `agent registry`, `authority control plane`, `policy enforcement`, `human harm`, `pressure test`, `portable assurance pattern`, and `governed action`.
- Added curated simple-English summaries for high-value existing terms, and reused already-short definitions where they are suitable as an initial comprehension layer.

## Changed

- Reworked top-level navigation so readers can start by task or topic before entering the alphabetic index.
- Increased the structured glossary from 599 to 612 terms.
- Updated README release framing and reader navigation.
- Updated `package.json` version metadata to match the repository release line.
- Regenerated JSON, JSON-LD, Markdown, governance inventories, quality reports, Jekyll term pages, and indexes.

## Compatibility

This is an additive minor release. Existing `definition` values and artifact shapes remain valid. Consumers that ignore `simple_definition` require no migration. Consumers may use the new field when they want a short reader-facing explanation while retaining `definition` as the precision layer.

## Portfolio review basis

The vocabulary review considered current terminology patterns across the maintainer's active trust-infrastructure portfolio, with particular emphasis on Agent Registry Protocol, RAHP Toolkit, PolicyMesh, Open National Digital Trust Framework, TSMM/TIS, DTG work, and related assurance/conformance projects. Project-specific terms were only promoted when they represented reusable concepts rather than product names or local implementation details.


## v1.4.1 — Publication Navigation and Term-Casing Integrity

This maintenance release restores a single authoritative GitHub Pages navigation tree and normalizes glossary display terms to the repository-wide lowercase convention.

### Fixed

- Removed the mirrored `docs/governance/` publication tree that caused Just the Docs to render governance pages twice.
- Added a defensive Jekyll exclusion for `docs/governance/` so a future mirror cannot re-enter the published navigation.
- Corrected the Pages `url` and repository link for the `sankarshanmukhopadhyay/ctwg-main-glossary` deployment.
- Normalized the 36 cross-repository terms introduced in v1.4.0 from title or sentence capitalization to lowercase display casing.

### Added

- Added a validator rule requiring the authoritative `term` field to use lowercase display casing.
- Added `tools/validate_jekyll_navigation.py` to reject duplicate publishable `title` and `parent` navigation identities.
- Added the navigation-integrity check to both validation and Pages workflows.

### Validation

- Validated all 599 structured glossary term files.
- Regenerated all JSON, JSON-LD, Markdown, inventory, quality-report, and Jekyll outputs.
- Confirmed 599 terms use the same lowercase display convention.
- Confirmed the publishable Jekyll navigation contains no duplicate title-parent identities.
- Confirmed the generated governance quality report remains at 100.0 / 100 with zero findings.

## v1.4.0 — Cross-Repository Runtime Governance Vocabulary

This release aligns the CTWG Main Glossary with terminology emerging across TSMM, TIS, TGA, and the DTG ZKP Task Force workspace, while improving the rendered GitHub Pages information architecture.

### Added

- Added 36 structured, cross-repository terms covering runtime interaction governance, authority and delegation lineage, executable evidence, legitimacy analysis, and privacy-preserving proofs.
- Added `governance/cross-repository-terminology-review.md` to document scope, inclusion criteria, exclusions, and assurance implications.
- Added ordered alphabet pages as visible children beneath the generated Glossary Terms navigation node.

### Changed

- Updated the generated glossary count from 563 to 599 terms.
- Changed the Glossary Terms page to a foldable parent and assigned deterministic navigation order to alphabet pages.
- Refreshed generated JSON, JSON-LD, Markdown, Jekyll term pages, inventories, manifests, and quality reports.
- Updated README release posture and generated assurance metrics.

### Validation

- Validated 599 structured term files.
- Checked 1,155 aliases for collisions.
- Checked 80 structured source citations.
- Rebuilt all generated artifacts with 0 quality findings and a 100.0 / 100 quality score.
- Built the Jekyll site to verify GitHub Pages compatibility.

## v1.3.0 — Publication Integrity and Contributor Onboarding

This release keeps the glossary vocabulary and schema stable while improving publication integrity, repository hygiene, and external contribution mechanics.

### Added

- Added `CODEOWNERS`, `CODE_OF_CONDUCT.md`, and `CITATION.cff`.
- Added issue templates for term proposals and generated quality-report findings.
- Added a pull request template aligned with source, generated artifact, and downstream-impact checks.
- Added README badges and a downstream consumer quickstart for generated JSON and JSON-LD artifacts.
- Added `tools/check_readme_quality_posture.py` and CI execution to prevent README quality posture drift from the generated report.

### Changed

- Updated README release framing to v1.3.0.
- Updated GitHub Pages `url` to the canonical Trust Over IP Pages origin.
- Made `governance/` the single maintainer-authored governance documentation source.
- Tightened CI generated-artifact drift detection now that the duplicated docs mirror has been removed.

### Fixed

- Corrected README quality posture from 534 terms to the generated 563-term report.
- Corrected revocation-supported coverage from 108 to the generated 113 value.
- Removed legacy spec-up-era workflow, script, and backup files while preserving `spec/terms-definitions/` as repository-local source evidence.

### Validation

- README quality posture is checked against `generated/json/governance-quality-report.json`.
- Generated report remains at 563 terms, 0 findings, and 100.0 / 100 quality score.

## v1.2.0 — Standards-Linked Glossary Refresh

This release modernizes the ToIP Main Glossary for current digital trust, verifiable credential, wallet, provenance, federation, and assurance terminology while preserving the repository's governance-executable source model.

### Added

- Added structured citation support for standards and specifications in `sources`.
- Added standards-backed terms for VC 2.0, Bitstring Status List, Data Integrity proofs, Controlled Identifiers, secured verifiable credentials, OpenID4VCI, OpenID4VP, VP Token, DCQL, SD-JWT VC, Key Binding JWT, status providers, issuer metadata, wallet attestation, OpenID Federation, entity statements, EUDI Wallet, PID, qualified electronic attestations of attributes, C2PA manifests, claim generators, manifest consumers, content credentials, DPoP, sender-constrained tokens, selective disclosure, status records, provenance, and verifiable presentations.
- Added `requirements.txt` for local and CI dependency bootstrap.

### Changed

- Refreshed key anchor terms including `verifiable-credential`, `w3c-verifiable-credentials-data-model-specification`, `trust-chain`, `aal`, `ial`, and `fal`.
- Improved generated term pages with reader notes, implementation relevance, linked related terms, and standards/source reference sections.
- Updated validation to check structured citation objects, resolvable `see_also` entries, and malformed internal reference markers.
- Updated CI dependency installation to use `requirements.txt`.
- Synchronized duplicated governance documentation under `docs/governance/`.

### Validation

- Validated 563 governance term files using repository integrity checks.
- Checked 1,086 aliases for collisions.
- Checked 41 structured source citations.
- Rebuilt governance bundles and inventories for 563 terms.
- Rebuilt the governance quality report with 0 findings.
- Regenerated 563 Jekyll term pages.

Note: the local workspace package index did not expose `jsonschema`, so the validator used its built-in fallback for required-field and repository integrity checks. CI remains configured to install full schema-validation dependencies from `requirements.txt`.

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
