# ToIP Main Glossary

The ToIP Main Glossary is the canonical terminology baseline for decentralized digital trust infrastructure work across Trust over IP working groups, adjacent specifications, and ecosystem implementations.

This repository now includes a **Governance-Executable Glossary** layer so that glossary terms can be consumed not only as prose but also as machine-readable governance primitives.

## Repository structure

- `spec/` — source markdown for glossary terms and publication content
- `glossary/terms/` — canonical structured term artifacts with governance metadata
- `glossary/overlays/` — inventories, evidence patterns, and crosswalk guidance
- `generated/` — generated markdown and machine-readable bundles
- `docs/` — governance notes and published site artifacts
- `schemas/` — schema artifacts for structured term validation
- `tools/` — build and validation utilities

## Governance-executable model

Each term now has a structured representation that can express:

- authority scope
- delegation mode
- revocation support
- lifecycle states
- execution role
- evidence artifacts
- control-plane decision points
- optional crosswalk references

This makes the glossary more useful for assurance tooling, policy automation, runtime governance systems, and audit-oriented implementations.

## Build and validation

```bash
npm install
npm run render
python tools/validate_governance_glossary.py
python tools/build_governance_glossary.py
```

## Generated artifacts

- `generated/json/governance-executable-glossary.json`
- `generated/json/governance-executable-glossary.jsonld`
- `generated/markdown/governance-executable-glossary.md`
- `glossary/overlays/governance/inventory.json`

## Maintainer guidance

1. Update the markdown definition in `spec/terms-definitions/`
2. Regenerate or revise the corresponding `glossary/terms/<term>.yaml`
3. Validate the structured layer
4. Publish the updated site and machine-readable bundles

## Design intent

The objective is to preserve the glossary as a public editorial asset while making it usable as executable governance infrastructure. That means shifting from definitions that are only descriptive to terms that can support evidence, auditability, enforcement, and change control.
