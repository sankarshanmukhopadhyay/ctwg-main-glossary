# ToIP Main Glossary

The ToIP Main Glossary is a **governance-executable terminology repository**. It publishes a human-readable GitHub Pages glossary while also producing machine-readable artifacts that describe authority, delegation, revocation, lifecycle state, evidence, auditability, and control-plane relevance for each structured term.

Version `v1.1.0` advances the repository from a structured glossary into **assurance-ready governance glossary infrastructure**. The core operating principle is simple: the authoritative term layer must be validated, reproducible, inspectable, and useful to downstream systems that need more than prose.

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

## What the generated layer provides

- per-term Jekyll pages under `_terms/`
- aggregate JSON and JSON-LD bundles under `generated/json/`
- a lightweight catalog for downstream discovery
- a machine-readable artifact manifest
- generated markdown exports under `generated/markdown/`
- governance inventory overlays for authority, delegation, revocation, lifecycle, evidence, and control-plane analysis
- a governance quality report for attribution, cross-reference, evidence, revocation, and assurance-readiness review
- deterministic site indexes for `terms-index.md` and `terms/<letter>/index.md`

## Local maintainer workflow

Install Python dependencies:

```bash
pip install pyyaml jsonschema
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
- [Repository Operating Model](governance/repository-operating-model.md)
- [Term Authoring Guide](governance/term-authoring-guide.md)
- [Assurance Model](governance/assurance-model.md)
- [Governance Quality Report](governance/quality-report.md)
- [Machine-readable Artifacts](artifacts.md)

## Design intent

The objective is to make glossary content easier to publish, easier to maintain, and more useful as machine-verifiable governance infrastructure. Markdown remains first-class for readers. Structured term artifacts remain first-class for assurance, interoperability, downstream indexing, conformance tooling, and automation workflows.

The glossary is not a certification authority and does not certify implementations. It provides a controlled vocabulary and evidence-aware semantic layer that downstream governance, conformance, and assurance systems can use as an inspectable reference.
