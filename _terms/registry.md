---
title: "registry"
---

# registry

A maintained collection of records used to look up information about defined subjects or relationships.

## Formal definition
A specialized database of records that serves as an authoritative source of information about entities.

## Why this concept matters
This concept is provided as a controlled glossary entry for standards, governance, and implementation review.

Use this concept consistently when mapping authority, evidence, reliance, and auditability across governance and implementation artifacts.

## Names and relationships

### Alternative designations
- **registries** (`en`, `alternative`)

### Related concepts
- [trust registry]({{ '/terms/trust-registry/' | relative_url }})

### Semantic relations
- **related**: `urn:tig:concept:trust-registry`

### Cross-vocabulary mappings
Not specified

## Provenance and identity
- **Concept ID**: `urn:tig:concept:registry`
- **Editorial status**: `stable`
- **Provenance classification**: `adapted`
- **Source corpus**: Trust over IP Main Glossary

### Standards and source references
- ToIP CTWG maintained glossary source: `spec/terms-definitions/registry.md`

<details markdown="1">
<summary><strong>Implementation and governance metadata</strong></summary>

### Legacy aliases
registry, registries

### Governance profile
- **Authority scope**: registry_management, governance_recognition
- **Delegation mode**: direct
- **Revocation supported**: True
- **Lifecycle states**: proposed, active, suspended, revoked, retired
- **Execution role**: runtime
- **Control-plane role**: decision_plane_component

### Enforcement points
- registration_decision
- revocation_decision

### Assurance
**Evidence artifacts**
- registry_entry

- **Assurance level hint**: AL2+
- **Auditability**: high

### Control plane
**Decision points**
- registration_decision
- revocation_decision

- **Accountable entity**: registry_operator

**Evidence produced**
- registry_entry

### Notes
Not specified

### Supporting definitions
Not specified

### Mental models
Not specified

### Crosswalk references
Not specified

</details>

---

*Generated from `glossary/terms/registry.yaml`. Edit the source concept and regenerate rather than editing this page directly.*
