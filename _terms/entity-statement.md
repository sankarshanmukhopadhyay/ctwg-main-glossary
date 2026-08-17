---
title: "entity-statement"
---

# entity-statement

A signed statement in OpenID Federation that describes metadata, authority, and trust relationships for a federation entity.

## Formal definition
A signed statement in OpenID Federation that describes metadata, authority, and trust relationships for a federation entity.

## Why this concept matters
This term is part of the v1.2.0 standards-linked refresh and is anchored to active implementation vocabulary.

Use this term when mapping glossary language to implementation profiles, governance controls, conformance checks, or assurance evidence.

## Names and relationships

### Alternative designations
- **entity statement** (`en`, `alternative`)

### Related concepts
- [openid-federation]({{ '/terms/openid-federation/' | relative_url }})
- [federation]({{ '/terms/federation/' | relative_url }})
- [trust-chain]({{ '/terms/trust-chain/' | relative_url }})
- [metadata]({{ '/terms/metadata/' | relative_url }})

### Semantic relations
- **related**: `urn:tig:concept:openid-federation`
- **related**: `urn:tig:concept:federation`
- **related**: `urn:tig:concept:trust-chain`
- **related**: `urn:tig:concept:metadata`

### Cross-vocabulary mappings
Not specified

## Provenance and identity
- **Concept ID**: `urn:tig:concept:entity-statement`
- **Editorial status**: `stable`
- **Provenance classification**: `locally_defined`
- **Source corpus**: Trust Infrastructure Glossary

### Standards and source references
- [OpenID Federation 1.0](https://openid.net/specs/openid-federation-1_0.html) (OpenID Foundation; Final Specification; 1.0; 2026-02-17) — normative

<details markdown="1">
<summary><strong>Implementation and governance metadata</strong></summary>

### Legacy aliases
entity statement

### Governance profile
- **Authority scope**: governance_recognition, registry_management
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

*Generated from `glossary/terms/entity-statement.yaml`. Edit the source concept and regenerate rather than editing this page directly.*
