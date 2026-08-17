# ToIP Main Glossary

[![Validate Governance-Executable Glossary](https://github.com/sankarshanmukhopadhyay/ctwg-main-glossary/actions/workflows/validate-governance-glossary.yml/badge.svg)](https://github.com/sankarshanmukhopadhyay/ctwg-main-glossary/actions/workflows/validate-governance-glossary.yml)
[![Pages](https://github.com/sankarshanmukhopadhyay/ctwg-main-glossary/actions/workflows/pages.yml/badge.svg)](https://github.com/sankarshanmukhopadhyay/ctwg-main-glossary/actions/workflows/pages.yml)
![Terms](https://img.shields.io/badge/terms-612-blue)
![Quality](https://img.shields.io/badge/quality-100.0%2F100-brightgreen)
![License](https://img.shields.io/badge/license-OWFa%201.0-blue)

The ToIP Main Glossary is a **governance-executable terminology repository**. It publishes a human-readable GitHub Pages glossary while also producing machine-readable artifacts that describe authority, delegation, revocation, lifecycle state, evidence, auditability, and control-plane relevance for each structured term.

Version `v1.5.0` adds a plain-English comprehension layer, topic-based navigation, and cross-project vocabulary for agent governance, assurance, interoperability, harms, recognition, redress, and executable policy.


## Reader-first navigation

- [Start Here](start-here.md) routes readers by task.
- [Concepts by Topic](concepts.md) groups high-value vocabulary by the problems readers are trying to solve.
- Generated term pages show **In Simple English** before the formal definition when a curated `simple_definition` is available.
- [Plain-English Authoring Guide](governance/plain-language-guide.md) defines the editorial standard and migration approach.

## Repository operating model

| Layer | Role | Authority |
|---|---|---|
| `glossary/terms/` | Structured YAML term artifacts | **Authoritative source** for executable term metadata and generated term pages |
| `schemas/` | JSON Schema and controlled vocabularies | **Validation contract** for machine-readable term artifacts |
| `tools/` | Validation, generation, and quality-report utilities | Operational control plane for publication integrity |
| `governance/` | Maintainer, contributor, assurance, and publication documentation | Maintainer-authored documentation |
| `examples/governance-term/` | Schema-aligned examples | Contributor enablement layer |
| `_terms/` | Generated Jekyll term pages | **Generated output only** |
| `generated/json/` | Machine-readable bundles, inventories, manifest, and quality report | **Generated output only** |
| `generated/markdown/` | Human-readable generated bundles, inventory, manifest, and quality report | **Generated output only** |
| `glossary/overlays/` | Generated and curated governance overlays | Mixed layer. Generated overlays must remain reproducible from source |

## Source-of-truth policy

The repository treats `glossary/terms/` as the authoritative operational source for generated glossary pages and bundle artifacts.

Generated directories must not be edited manually unless the corresponding generator logic is being changed and the outputs are immediately regenerated in the same change set.

**Generated-only paths:**

- `_terms/`
- `generated/json/`
- `generated/markdown/`
- `terms-index.md`
- `terms/*/index.md`
- `glossary/overlays/governance/inventory.json`
- `glossary/overlays/governance/core-operational-terms.md`
- `governance/generated-inventories.md`
- `governance/quality-report.md`

## Using the glossary in your project

Most downstream consumers do not need the maintainer build pipeline. Use the generated artifacts directly and pin to a release tag when reproducibility matters.

Fetch the JSON bundle:

```bash
curl -L -o governance-glossary.json \
  https://raw.githubusercontent.com/sankarshanmukhopadhyay/ctwg-main-glossary/main/generated/json/governance-executable-glossary.json
```

Fetch the JSON-LD bundle:

```bash
curl -L -o governance-glossary.jsonld \
  https://raw.githubusercontent.com/sankarshanmukhopadhyay/ctwg-main-glossary/main/generated/json/governance-executable-glossary.jsonld
```

Use `generated/json/artifact-manifest.json` to discover the current machine-readable bundle set and `generated/json/governance-quality-report.json` to inspect quality posture.

## What the generated layer provides

- per-term Jekyll pages under `_terms/`
- aggregate JSON and JSON-LD bundles under `generated/json/`
- a lightweight catalog for downstream discovery
- a machine-readable artifact manifest
- generated markdown exports under `generated/markdown/`
- governance inventory overlays for authority, delegation, revocation, lifecycle, evidence, and control-plane analysis
- a governance quality report for attribution, cross-reference, evidence, revocation, and assurance-readiness review
- deterministic site indexes for `terms-index.md` and `terms/<letter>/index.md`


## Current assurance-readiness posture

The current generated quality report evaluates all 612 structured terms and reports:

- quality score: `100.0 / 100`;
- total findings: `0`;
- terms with source coverage: `612`;
- terms with `see_also` coverage: `612`;
- terms with evidence coverage: `612`; and
- revocation-supported terms with revocation-relevant evidence: `149`.

This score is not a certification claim. It means that all checks currently implemented by `tools/build_quality_report.py` have been satisfied and that the glossary has no open generated quality-report findings under the current assurance-readiness rubric.

## Local maintainer workflow

Install Python dependencies:

```bash
pip install -r requirements.txt
```

Run the validation and generation pipeline:

```bash
python tools/validate_governance_glossary.py
python tools/build_governance_glossary.py
python tools/build_quality_report.py
python tools/build_jekyll_site.py
```

Build the site locally:

```bash
bundle install
bundle exec jekyll serve
```

## CI and publication workflow

GitHub Actions validate the source layer, regenerate artifacts, and fail when committed generated files drift from the authoritative source.

Publication sequence:

1. validate `glossary/terms/*.yaml` against the JSON Schema and controlled vocabularies;
2. run repository-specific checks for slugs, aliases, source files, revocation semantics, and evidence alignment;
3. generate machine-readable bundles, catalogs, inventories, and artifact manifest;
4. generate the governance quality report;
5. generate Jekyll term pages and navigation indexes;
6. fail if generated artifacts are not committed; and
7. build and deploy the GitHub Pages site.

## Contribution guidance

1. Edit or add the relevant YAML file under `glossary/terms/`.
2. Use `examples/governance-term/` as the authoring template.
3. Keep values within `schemas/governance-vocabularies.yaml` unless a vocabulary expansion is intentionally part of the change.
4. Run validation and rebuild scripts locally.
5. Review diffs in generated output.
6. Update governance documentation when semantics, workflow, or artifact expectations change.
7. Submit a change set that keeps source, generated output, and documentation in sync.

See also:

- [Contributing](Contributing.md)
- [Code of Conduct](CODE_OF_CONDUCT.md)
- [Repository Operating Model](governance/repository-operating-model.md)
- [Term Authoring Guide](governance/term-authoring-guide.md)
- [Assurance Model](governance/assurance-model.md)
- [Governance Quality Report](governance/quality-report.md)
- [Machine-readable Artifacts](artifacts.md)

## Design intent

The objective is to make glossary content easier to publish, easier to maintain, and more useful as machine-verifiable governance infrastructure. Markdown remains first-class for readers. Structured term artifacts remain first-class for assurance, interoperability, downstream indexing, conformance tooling, and automation workflows.

The glossary is not a certification authority and does not certify implementations. It provides a controlled vocabulary and evidence-aware semantic layer that downstream governance, conformance, and assurance systems can use as an inspectable reference.

## v1.2.0 standards-linked coverage

This release adds or refreshes vocabulary for:

- W3C Verifiable Credentials Data Model v2.0, Data Integrity, Controlled Identifiers, secured credentials, verifiable presentations, and Bitstring Status List;
- OpenID4VCI, OpenID4VP, VP Token, DCQL, issuer metadata, wallet attestation, OpenID Federation, entity statements, and trust chains;
- IETF SD-JWT VC, Key Binding JWT, DPoP, and sender-constrained tokens;
- EUDI Wallet, PID, and qualified electronic attestations of attributes; and
- C2PA manifests, claim generators, manifest consumers, content credentials, and provenance.

Structured source citations are now supported alongside legacy source strings. New standards-backed terms should prefer structured citation objects so downstream tools can inspect publisher, version, status, date, URL, and normative intent.


## Upstream synchronisation

This maintained fork tracks [`trustoverip/ctwg-main-glossary`](https://github.com/trustoverip/ctwg-main-glossary) through a governed, one-way process. Scheduled monitoring raises drift issues here, while maintainers can prepare a draft merge-based synchronisation pull request against this fork. The automation cannot contribute, push, open issues or open pull requests against upstream. See [upstream synchronisation governance](docs/governance/upstream-synchronisation.md).
