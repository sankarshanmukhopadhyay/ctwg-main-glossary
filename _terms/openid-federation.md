---
title: "openid-federation"
---

# openid-federation

A federation framework for establishing trust among OpenID participants using entity statements, trust chains, and federation metadata.

## Formal definition
A federation framework for establishing trust among OpenID participants using entity statements, trust chains, and federation metadata.

## Why this concept matters
This concept is provided as a controlled glossary entry for standards, governance, and implementation review.

Use this concept consistently when mapping authority, evidence, reliance, and auditability across governance and implementation artifacts.

## Names and relationships

### Alternative designations
- **OpenID Federation** (`en`, `alternative`)

### Related concepts
- [federation]({{ '/terms/federation/' | relative_url }})
- [trust-chain]({{ '/terms/trust-chain/' | relative_url }})
- [entity-statement]({{ '/terms/entity-statement/' | relative_url }})
- [trust-anchor]({{ '/terms/trust-anchor/' | relative_url }})

### Semantic relations
- **related**: `urn:tig:concept:federation`
- **related**: `urn:tig:concept:trust-chain`
- **related**: `urn:tig:concept:entity-statement`
- **related**: `urn:tig:concept:trust-anchor`

### Cross-vocabulary mappings
Not specified

## Provenance and identity
- **Concept ID**: `urn:tig:concept:openid-federation`
- **Editorial status**: `stable`
- **Provenance classification**: `locally_defined`
- **Source corpus**: Trust Infrastructure Glossary

### Standards and source references
- [OpenID Federation 1.0](https://openid.net/specs/openid-federation-1_0.html) (OpenID Foundation; Final Specification; 1.0; 2026-02-17) — normative

<details markdown="1">
<summary><strong>Implementation and governance metadata</strong></summary>

### Legacy aliases
OpenID Federation

### Governance profile
- **Authority scope**: governance_recognition, registry_management, verification_and_reliance
- **Delegation mode**: direct
- **Revocation supported**: False
- **Lifecycle states**: proposed, active, retired
- **Execution role**: hybrid
- **Control-plane role**: decision_plane_component

### Enforcement points
- registration_decision
- reliance_decision

### Assurance
**Evidence artifacts**
- registry_entry
- verification_log
- audit_log
- policy_document

- **Assurance level hint**: AL2+
- **Auditability**: high

### Control plane
**Decision points**
- registration_decision
- reliance_decision

- **Accountable entity**: glossary_maintainers

**Evidence produced**
- registry_entry
- verification_log
- audit_log
- policy_document

### Notes
Not specified

### Supporting definitions
Not specified

### Mental models
Not specified

### Crosswalk references
- **OPENID**: OpenID Federation 1.0

</details>

---

*Generated from `glossary/terms/openid-federation.yaml`. Edit the source concept and regenerate rather than editing this page directly.*
