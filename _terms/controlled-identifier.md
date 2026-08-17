---
title: "controlled-identifier"
---

# controlled-identifier

An identifier whose controller can be discovered through an associated controlled identifier document containing verification material and service endpoints.

## Formal definition
An identifier whose controller can be discovered through an associated controlled identifier document containing verification material and service endpoints.

## Why this concept matters
This concept is provided as a controlled glossary entry for standards, governance, and implementation review.

Use this concept consistently when mapping authority, evidence, reliance, and auditability across governance and implementation artifacts.

## Names and relationships

### Alternative designations
- **controlled identifier** (`en`, `alternative`)

### Related concepts
- [decentralized-identifier]({{ '/terms/decentralized-identifier/' | relative_url }})
- [did-document]({{ '/terms/did-document/' | relative_url }})
- [controller]({{ '/terms/controller/' | relative_url }})
- [cryptographic-key]({{ '/terms/cryptographic-key/' | relative_url }})

### Semantic relations
- **related**: `urn:tig:concept:decentralized-identifier`
- **related**: `urn:tig:concept:did-document`
- **related**: `urn:tig:concept:controller`
- **related**: `urn:tig:concept:cryptographic-key`

### Cross-vocabulary mappings
Not specified

## Provenance and identity
- **Concept ID**: `urn:tig:concept:controlled-identifier`
- **Editorial status**: `stable`
- **Provenance classification**: `locally_defined`
- **Source corpus**: Trust Infrastructure Glossary

### Standards and source references
- [Controlled Identifiers v1.0](https://www.w3.org/TR/cid/) (W3C; Recommendation; 1.0; 2025-05-15) — normative

<details markdown="1">
<summary><strong>Implementation and governance metadata</strong></summary>

### Legacy aliases
controlled identifier

### Governance profile
- **Authority scope**: verification_and_reliance, delegation_and_scope
- **Delegation mode**: direct_or_constrained
- **Revocation supported**: False
- **Lifecycle states**: proposed, active, retired
- **Execution role**: hybrid
- **Control-plane role**: decision_plane_component

### Enforcement points
- reliance_decision
- delegation_grant

### Assurance
**Evidence artifacts**
- verification_log
- delegation_record
- audit_log

- **Assurance level hint**: AL2+
- **Auditability**: high

### Control plane
**Decision points**
- reliance_decision
- delegation_grant

- **Accountable entity**: glossary_maintainers

**Evidence produced**
- verification_log
- delegation_record
- audit_log

### Notes
Not specified

### Supporting definitions
Not specified

### Mental models
Not specified

### Crosswalk references
- **W3C**: Controlled Identifiers v1.0, DID Core

</details>

---

*Generated from `glossary/terms/controlled-identifier.yaml`. Edit the source concept and regenerate rather than editing this page directly.*
