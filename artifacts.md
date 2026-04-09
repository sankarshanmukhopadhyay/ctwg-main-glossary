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
- `generated/json/governance-inventory.json`
- `generated/markdown/governance-executable-glossary.md`
- `generated/markdown/governance-inventory.md`

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

## Generation workflow

Run the following before publication:

```bash
python tools/validate_governance_glossary.py
python tools/build_governance_glossary.py
python tools/build_jekyll_site.py
```

The GitHub Actions workflows also run these generation steps and now fail if committed generated artifacts are out of sync with the authoritative source layer.
