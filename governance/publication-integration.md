---
title: "Publication Integration"
parent: Governance Documentation
nav_order: 15
---

# Publication Integration

The repository publishes a GitHub Pages site from the same source layer that produces machine-readable governance artifacts.

## Publication sequence

1. Validate `glossary/terms/*.yaml`.
2. Generate machine-readable bundles, catalogs, inventories, and artifact manifest.
3. Generate the governance quality report.
4. Generate Jekyll pages and term indexes.
5. Verify generated artifacts are in sync.
6. Build the site with Jekyll and Just the Docs.
7. Deploy through GitHub Pages.

## Integration rules

- `glossary/terms/*.yaml` is the authoritative structured term layer.
- `schemas/` defines the validation contract.
- `tools/` define the generation and reporting behavior.
- generated bundles under `generated/` are publication artifacts.
- generated term pages under `_terms/` are publication artifacts.
- governance overlays may be generated or curated, but generated overlays must remain reproducible from source.

## Integrity expectation

CI must fail when generated artifacts are not in sync with source. This keeps the repository publishable from the checked-in state and reduces silent drift between authored content and rendered content.

## Reader-facing outcomes

The site provides:

- a browsable glossary term collection;
- governance documentation for maintainers and adopters;
- downloadable JSON, JSON-LD, and markdown artifacts;
- generated inventory views for authority, delegation, revocation, lifecycle, evidence, and control-plane analysis; and
- a governance quality report for assurance-readiness review.
