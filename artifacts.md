---
title: Machine-readable Artifacts
nav_order: 6
---

# Machine-readable Artifacts

TIG publishes generated artifacts for downstream systems that need stable concept semantics rather than static prose. All generated artifacts are derived from `glossary/terms/`.

## Canonical v2 bundles

- `generated/json/trust-infrastructure-glossary.json`
- `generated/json/trust-infrastructure-glossary.jsonld`
- `generated/rdf/trust-infrastructure-glossary.ttl`
- `generated/json/trust-infrastructure-glossary.catalog.json`

The JSON-LD and Turtle representations use SKOS-aligned concept, label, relation, and mapping semantics.

## v1 compatibility bundles

The following filenames remain generated during the v2 migration window:

- `generated/json/governance-executable-glossary.json`
- `generated/json/governance-executable-glossary.jsonld`
- `generated/json/governance-executable-glossary.catalog.json`
- `generated/markdown/governance-executable-glossary.md`

Consumers should migrate to the canonical TIG filenames.

## Profiles

Reusable selection profiles live under `profiles/` and are validated against stable `concept_id` values.

## Inventory and assurance-readiness artifacts

- `generated/json/governance-inventory.json`
- `generated/markdown/governance-inventory.md`
- `generated/json/governance-quality-report.json`
- `generated/markdown/governance-quality-report.md`

## Artifact manifest

- `generated/json/artifact-manifest.json`
- `generated/markdown/artifact-manifest.md`

The manifest identifies source inputs, generators, intended consumer use, and stability expectations.

## Generation workflow

```bash
python tools/validate_governance_glossary.py
python tools/validate_profiles.py
python tools/build_governance_glossary.py
python tools/build_quality_report.py
python tools/build_jekyll_site.py
```

GitHub Actions run the same steps and fail when generated output drifts from authoritative source.
