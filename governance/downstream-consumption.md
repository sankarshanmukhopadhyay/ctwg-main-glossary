---
title: "Downstream Consumption"
parent: Governance Documentation
nav_order: 27
---

# Downstream Consumption

The generated artifacts are designed for systems that need glossary terms as structured governance inputs.

## Consumer patterns

| Consumer | Useful artifacts | Typical use |
|---|---|---|
| Trust registries | catalog, JSON bundle, inventory | Align registry roles, authority scope, lifecycle state, and evidence terms. |
| Policy engines | JSON bundle, vocabularies | Map policy terms to controlled vocabulary values and decision points. |
| Conformance suites | schema, inventory, quality report | Test whether implementations produce evidence for relevant governance concepts. |
| Assurance dashboards | inventory, quality report, artifact manifest | Track term coverage, assurance-readiness findings, and generated artifact health. |
| Standards authors | markdown exports, generated pages | Reuse consistent definitions and identify governance semantics. |
| Documentation portals | Jekyll pages, markdown bundle | Publish human-readable terms with operational metadata. |

## Stability expectations

- `glossary/terms/*.yaml` is the source model.
- `schemas/governance-term.schema.json` is the validation contract.
- `generated/json/governance-executable-glossary.catalog.json` is the lightweight discovery surface.
- `generated/json/governance-executable-glossary.json` is the full structured corpus.
- `generated/json/governance-quality-report.json` is a review artifact and may change as quality rules evolve.

## Integration caution

Consumers should not infer certification, compliance, or legal authority from a term artifact. The glossary provides shared semantics and evidence expectations. External systems remain responsible for their own policies, conformance rules, and assurance decisions.
