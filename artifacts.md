---
title: Machine-readable Artifacts
nav_order: 4
---

# Machine-readable Artifacts

The repository publishes generated artifacts for downstream systems that need glossary terms as structured governance inputs rather than static prose. These artifacts are regenerated from `glossary/terms/` and must remain synchronized with the source layer.

## Core bundles

- `generated/json/governance-executable-glossary.json`
- `generated/json/governance-executable-glossary.jsonld`
- `generated/json/governance-executable-glossary.catalog.json`
- `generated/markdown/governance-executable-glossary.md`

## Inventory and assurance-readiness artifacts

- `generated/json/governance-inventory.json`
- `generated/markdown/governance-inventory.md`
- `generated/json/governance-quality-report.json`
- `generated/markdown/governance-quality-report.md`
- `governance/generated-inventories.md`
- `governance/quality-report.md`

## Artifact manifest

- `generated/json/artifact-manifest.json`
- `generated/markdown/artifact-manifest.md`

The manifest identifies each major generated artifact, its source inputs, generator, consumer use case, and stability expectation.

## Governance overlay artifacts

- `glossary/overlays/governance/inventory.json`
- `glossary/overlays/governance/core-operational-terms.md`
- `glossary/overlays/assurance/evidence-patterns.json`

## Generated inventory views

The inventory bundle and markdown view classify terms across several operational dimensions:

- authority-bearing terms
- delegation-sensitive terms
- revocation-sensitive terms
- lifecycle-sensitive terms
- evidence-producing terms
- control-plane terms
- assurance level hints
- governance profile groupings

## Quality report interpretation

The quality report is a maintainer and adopter signal. It identifies where terms may need stronger sources, better cross-references, more specific evidence artifacts, clearer revocation evidence, or a stronger assurance hint.

The report is not a pass/fail certification. It is a machine-readable evidence-quality backlog that supports review, prioritization, and continuous improvement.

## Generation workflow

Run the following before publication:

```bash
python tools/validate_governance_glossary.py
python tools/build_governance_glossary.py
python tools/build_quality_report.py
python tools/build_jekyll_site.py
```

GitHub Actions run the same generation steps and fail if committed generated artifacts are out of sync with the authoritative source layer.
