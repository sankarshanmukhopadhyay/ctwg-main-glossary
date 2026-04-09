# ToIP Main Glossary

The ToIP Main Glossary is published as a **GitHub Pages** site using **Jekyll** and **Just the Docs**, with a structured **governance-executable** source layer that produces reader-facing pages and machine-readable artifacts from the same repository.

## Repository operating model

This repository is now organized around a clear source-to-generated publication pipeline.

| Layer | Role | Authority |
|---|---|---|
| `glossary/terms/` | Structured YAML term artifacts | **Authoritative source** for executable term metadata and generated term pages |
| `glossary/overlays/` | Generated and curated governance overlays | Mixed layer. Generated files must remain reproducible from source |
| `_terms/` | Generated Jekyll term pages | **Generated output only** |
| `generated/json/` | Machine-readable bundles and inventories | **Generated output only** |
| `generated/markdown/` | Generated markdown bundles and inventory views | **Generated output only** |
| `governance/` | Maintainer and publication documentation | Maintainer-authored documentation |
| `tools/` | Validation and generation utilities | Operational control plane for publication |

## Source-of-truth policy

The repository treats `glossary/terms/` as the operational source of truth for generated glossary pages and bundle artifacts.

Generated directories must not be edited manually except when the corresponding generator logic is being changed and the outputs are immediately regenerated in the same change set.

**Generated-only paths:**

- `_terms/`
- `generated/json/`
- `generated/markdown/`
- `terms-index.md`
- `terms/*/index.md`
- `glossary/overlays/governance/inventory.json`
- `glossary/overlays/governance/core-operational-terms.md`

## Publication workflow

1. Validate structured term artifacts.
2. Generate machine-readable bundles and governance inventories.
3. Generate Jekyll pages and navigation indexes.
4. Build and publish the GitHub Pages site.

## Local maintainer workflow

```bash
python tools/validate_governance_glossary.py
python tools/build_governance_glossary.py
python tools/build_jekyll_site.py
bundle install
bundle exec jekyll serve
```

## What the generated layer now provides

- per-term Jekyll pages under `_terms/`
- aggregate JSON and JSON-LD bundles under `generated/json/`
- generated markdown inventory views under `generated/markdown/`
- governance inventory overlays for authority, delegation, revocation, lifecycle, evidence, and control-plane analysis
- deterministic site indexes for `terms-index.md` and `terms/<letter>/index.md`

## Contribution guidance

1. Edit or add the relevant YAML file under `glossary/terms/`.
2. Run validation and rebuild scripts locally.
3. Review diffs in generated output.
4. Update maintainer or governance documentation when semantics, workflow, or artifact expectations change.
5. Submit a change set that keeps source, generated output, and documentation in sync.

See also:

- [Contributing](Contributing.md)
- [Repository Operating Model](governance/repository-operating-model.md)
- [Governance Documentation](governance/index.md)

## Design intent

The objective is to make glossary content easier to publish, easier to maintain, and more useful as machine-verifiable governance infrastructure. Markdown remains first-class for readers. Structured term artifacts remain first-class for assurance, interoperability, downstream indexing, and automation workflows.
