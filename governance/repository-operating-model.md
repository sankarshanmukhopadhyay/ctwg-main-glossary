---
title: "Repository Operating Model"
parent: Governance Documentation
nav_order: 5
---

# Repository Operating Model

## Purpose

This repository is operated as a controlled publishing system for glossary content with executable governance semantics.

The operating model keeps three things aligned:

1. **authority** over what may be changed;
2. **enforcement** through deterministic validation and generation; and
3. **evidence** that generated outputs match the authoritative source layer.

## Authority model

| Area | Authoritative layer | Generated or derived layer |
|---|---|---|
| Term semantics | `glossary/terms/*.yaml` | `_terms/*.md`, generated bundles, generated indexes |
| Validation contract | `schemas/governance-term.schema.json` and `schemas/governance-vocabularies.yaml` | CI validation outcomes |
| Publication controls | `tools/*.py` and workflow files | generated build summaries and drift checks |
| Maintainer guidance | `governance/*.md`, `README.md`, `Contributing.md` | generated inventory and quality report pages |

## Source and generated layers

### Authoritative source layer

- `glossary/terms/`
- `schemas/`
- `tools/`
- `governance/`
- top-level maintainer documentation

### Generated publication layer

- `_terms/`
- `generated/json/`
- `generated/markdown/`
- `terms-index.md`
- `terms/*/index.md`
- generated governance overlays
- generated governance inventory and quality report pages

## Maintainer rules

### Rule 1: edit source, not renderings

Change `glossary/terms/*.yaml` rather than `_terms/*.md` or generated JSON/markdown artifacts.

### Rule 2: validate before publishing

Run:

```bash
python tools/validate_governance_glossary.py
python tools/build_governance_glossary.py
python tools/build_quality_report.py
python tools/build_jekyll_site.py
```

### Rule 3: keep schema and vocabulary aligned

When adding a new controlled value, update both:

- `schemas/governance-vocabularies.yaml`
- `schemas/governance-term.schema.json`

The validator checks that the two remain aligned.

### Rule 4: treat generated diffs as evidence

Generated diffs are not noise. They show the operational effect of source-layer changes. Review them before merging.

### Rule 5: do not overstate assurance

Assurance hints are glossary-level indicators. They do not certify implementations, systems, organizations, or governance frameworks.

## CI enforcement

CI performs four control-plane functions:

1. validates source term artifacts against the JSON Schema and controlled vocabularies;
2. performs repository-specific integrity checks for slugs, aliases, source-file references, revocation states, and evidence alignment;
3. regenerates machine-readable and publication artifacts; and
4. fails on generated artifact drift.

## Evidence produced

The repository produces evidence through:

- validation command output;
- generated `build-summary.json`;
- generated inventory artifacts;
- generated quality report artifacts;
- deterministic Jekyll term pages; and
- GitHub Actions execution logs.
