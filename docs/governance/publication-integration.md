---
title: "Publication Integration"
parent: Governance Documentation
nav_order: 15
---

# Publication Integration

The repository publishes a GitHub Pages site from a governance-executable source layer.

## Publication sequence

1. validate `glossary/terms/*.yaml`
2. generate machine-readable bundles and governance inventories
3. generate Jekyll pages and term indexes
4. build the site with Jekyll and Just the Docs

## Integration rules

- `glossary/terms/*.yaml` is the authoritative structured term layer
- generated bundles under `generated/` are publication artifacts
- generated term pages under `_terms/` are publication artifacts
- governance overlays may be generated or curated, but generated overlays must remain reproducible from source

## Integrity expectation

CI should fail when generated artifacts are not in sync with source. This keeps the repository publishable from the checked-in state and reduces silent drift between authored and rendered content.

## Reader-facing outcomes

The site provides:

- a browsable glossary term collection
- governance documentation for maintainers and adopters
- downloadable JSON and markdown artifacts
- generated inventory views for authority, delegation, revocation, lifecycle, evidence, and control-plane analysis
