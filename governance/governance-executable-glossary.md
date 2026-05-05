---
title: "Governance-Executable Glossary"
parent: Governance Documentation
nav_order: 10
---

# Governance-Executable Glossary

A governance-executable glossary is a glossary whose terms can be validated, regenerated, inventoried, and reused as structured governance artifacts.

This repository does not treat terms only as prose. Each structured term can carry metadata for authority, delegation, revocation, lifecycle state, execution role, evidence, auditability, decision points, accountable entity, and crosswalk references.

## What the executable layer captures

| Dimension | Purpose |
|---|---|
| `governance_profile` | Classifies whether the term is descriptive, governance-supporting, or core-operational. |
| `authority_scope` | Identifies the governance domain where the term can affect rights, recognition, reliance, issuance, access, or policy. |
| `delegation_mode` | Indicates whether authority is direct or constrained/delegated. |
| `revocation_supported` | States whether revocation semantics apply. |
| `lifecycle_states` | Lists states relevant to operation or governance. |
| `execution_role` | Indicates whether the term matters primarily at design time, runtime, or both. |
| `control_plane_role` | Distinguishes reference terms from decision-plane components. |
| `enforcement_points` | Names where policy or governance is enforced. |
| `evidence_artifacts` | Names records, logs, attestations, policy documents, or status artifacts that support assurance. |
| `decision_points` | Names decisions affected by the term. |
| `accountable_entity` | Identifies the responsible role or function. |

## Assurance value

The executable layer makes glossary semantics inspectable and reusable. It helps downstream systems ask practical questions:

- Does this term affect authority?
- Can authority be delegated?
- Can the relevant state be revoked?
- What evidence should exist?
- Who is accountable?
- Where does enforcement happen?
- Is the term only descriptive, or does it affect a decision path?

## Boundaries

The glossary does not certify conformance. It provides structured terminology that conformance suites, trust registries, standards authors, and governance tooling can consume.

## Generated outputs

- `generated/json/governance-executable-glossary.json`
- `generated/json/governance-executable-glossary.catalog.json`
- `generated/json/governance-executable-glossary.jsonld`
- `generated/json/governance-inventory.json`
- `generated/json/governance-quality-report.json`
- `generated/json/artifact-manifest.json`
- `generated/markdown/*.md`
