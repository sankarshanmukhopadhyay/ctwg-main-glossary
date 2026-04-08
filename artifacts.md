---
title: Machine-readable Artifacts
nav_order: 4
---

# Machine-readable Artifacts

The following generated artifacts are maintained in this repository and can be consumed directly by external tooling.

## Core bundles

- `generated/json/governance-executable-glossary.json`
- `generated/json/governance-executable-glossary.jsonld`
- `generated/json/governance-executable-glossary.catalog.json`
- `generated/markdown/governance-executable-glossary.md`

## Governance overlay artifacts

- `glossary/overlays/governance/inventory.json`
- `glossary/overlays/assurance/evidence-patterns.json`

## Generation workflow

Run the following before publication:

```bash
python tools/validate_governance_glossary.py
python tools/build_governance_glossary.py
python tools/build_jekyll_site.py
```

The GitHub Pages workflow also runs these generation steps before the site is deployed.
