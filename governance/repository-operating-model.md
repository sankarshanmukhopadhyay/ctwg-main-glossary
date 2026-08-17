---
title: "Repository Operating Model"
parent: Governance Documentation
nav_order: 5
---

# Repository Operating Model

## Purpose

TIG is operated as a controlled semantic publishing system. The model keeps semantic authority, provenance, deterministic validation, generated representations, and review evidence aligned.

## Authority model

| Area | Authoritative layer | Derived layer |
|---|---|---|
| Concept semantics | `glossary/terms/*.yaml` | `_terms/*.md`, generated bundles and indexes |
| Validation contract | `schemas/governance-term.schema.json`, controlled vocabularies | CI outcomes |
| Vocabulary selections | `profiles/*.yaml` | downstream profile consumption |
| Publication controls | `tools/*.py`, workflow files | generated build summaries |
| Maintainer governance | `governance/*.md`, `README.md`, `Contributing.md` | generated reports |

## Semantic authority

The project governs TIG concepts independently. Source provenance records where concepts came from or what influenced them; it does not transfer ongoing editorial authority to the source corpus.

## Source and generated layers

### Authoritative

- `glossary/terms/`
- `schemas/`
- `profiles/`
- `tools/`
- `governance/`
- top-level maintainer documentation

### Generated

- `_terms/`
- `generated/json/`
- `generated/rdf/`
- `generated/markdown/`
- `terms-index.md`
- `terms/*/index.md`
- generated governance overlays and reports

### Historical provenance

`spec/terms-definitions/` is retained to support source references from the ToIP-derived corpus. It is not the v2 authority layer.

## Maintainer rules

1. **Edit source, not renderings.**
2. **Never silently reassign a published `concept_id`.**
3. **Treat mapping strength as a semantic assertion requiring review.**
4. **Preserve source provenance and licensing obligations.**
5. **Keep schema, examples, profiles, generators, and documentation aligned.**
6. **Treat generated diffs as review evidence.**
7. **Do not overstate assurance:** glossary metadata does not certify systems or implementations.

## CI enforcement

CI:

1. validates all concept artifacts against the v2 JSON Schema;
2. verifies stable identifier and designation invariants;
3. validates vocabulary profiles against the live corpus;
4. runs repository-specific reference and evidence checks;
5. regenerates machine-readable and Jekyll artifacts; and
6. fails when committed generated output drifts from authoritative source.

## Maintainer workflow

```bash
python tools/validate_governance_glossary.py
python tools/validate_profiles.py
python tools/build_governance_glossary.py
python tools/build_quality_report.py
python tools/build_jekyll_site.py
python tools/validate_jekyll_navigation.py
```
