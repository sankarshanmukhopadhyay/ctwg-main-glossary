---
title: "Cross-Repository Terminology Review"
parent: "Semantic Model & Authoring"
nav_order: 6
grand_parent: "Govern TIG"
---

# Cross-Repository Terminology Review

## Scope

This review compares the CTWG Main Glossary with terminology used in the Trust Systems Meta-Model (TSMM), Trust Infrastructure Schemas (TIS), Trust Graph Artifacts (TGA), and the DTG ZKP Task Force workspace.

The review applies a reuse threshold: a term is added when it expresses a concept that is likely to be referenced across repositories, specifications, assurance profiles, or implementations. Repository-local filenames and narrowly scoped artifact labels are not automatically promoted into the shared glossary.

## Outcome

The review identified 36 reusable concepts requiring normalized definitions. The additions fall into four groups:

1. **Runtime and interaction governance:** agent class, attention policy, authorization checkpoint, control mode, dynamic authorization, interaction context, interaction task, observability mode, opacity boundary, service descriptor, skill contract, discovery governance, capability negotiation, extension contract, and task evidence lifecycle.
2. **Delegation and authority:** delegation lineage, aggregation amplification, monotonic attenuation, authority boundary, runtime governance envelope, agent mandate envelope, and runtime authority envelope.
3. **Evidence and executable governance:** evidence artifact, decision receipt, evidence bundle, trust task execution receipt, proof-carrying commitment receipt, legitimacy gap, and control-plane shift.
4. **Privacy-preserving proofs:** personhood, nullifier, issuer concealment, unlinkability, and predicate proof.

## Exclusions

Project-specific artifact names were excluded where the underlying concept is already represented by a more reusable term or where the label is not yet stable enough to serve as a cross-community definition.

## Assurance implications

Each new term is represented in the structured source layer and therefore participates in schema validation, generated JSON and JSON-LD bundles, Jekyll page generation, quality reporting, authority-scope inventories, lifecycle review, and evidence mapping.

## Review evidence

The release can be validated by running:

```bash
python tools/validate_governance_glossary.py
python tools/build_governance_glossary.py
python tools/build_quality_report.py
python tools/build_jekyll_site.py
bundle exec jekyll build
```
