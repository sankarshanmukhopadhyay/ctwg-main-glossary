# v1.5.0 — Reader Comprehension, Information Architecture, and Portfolio Vocabulary

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
