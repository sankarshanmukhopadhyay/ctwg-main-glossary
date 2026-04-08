---
title: "Governance-Executable Glossary"
parent: Governance Documentation
nav_order: 10
---

# Governance-Executable Glossary

This repository now carries a parallel **governance-executable representation** of the glossary.

## What has changed

- all **534** term definitions under `spec/terms-definitions/` now have a corresponding structured artifact under `glossary/terms/`
- governance-sensitive metadata is generated for every term, with stronger operational semantics for authority, delegation, lifecycle, registry, policy, credential, and assurance related terms
- downloadable machine-readable bundles are produced under `generated/json/`
- governance inventories and evidence patterns are published under `glossary/overlays/`

## Operating model

The governance-executable YAML layer now acts as the publication source for generated glossary pages, while markdown remains the reader-facing rendering layer. It adds:

- authority and scope hints
- delegation and lifecycle handling
- revocation capability flags
- evidence and auditability patterns
- control-plane decision points
- optional crosswalk references for downstream tooling

## Assurance posture

This does not claim normative status for all generated metadata. Instead it establishes a machine-verifiable substrate that can be refined incrementally while preserving the current editorial workflow.

## Core generated artifacts

- `glossary/terms/*.yaml`
- `glossary/overlays/governance/inventory.json`
- `generated/json/governance-executable-glossary.json`
- `generated/json/governance-executable-glossary.jsonld`

## Validation

Run:

```bash
python tools/validate_governance_glossary.py
python tools/build_governance_glossary.py
```
