---
title: "trust-registry"
---

# trust-registry

A simple-English summary has not yet been added for this concept.

## Formal definition
A registry that serves as an authoritative source for trust graphs or other governed information describing one or more trust communities. A trust registry is typically authorized by a governance framework.

## Why this concept matters
This concept is provided as a controlled glossary entry for standards, governance, and implementation review.

Use this concept consistently when mapping authority, evidence, reliance, and auditability across governance and implementation artifacts.

## Names and relationships

### Alternative designations
- **trust registry** (`en`, `alternative`)
- **trust registries** (`en`, `alternative`)

### Related concepts
- [trust list]({{ '/terms/trust-list/' | relative_url }})
- [verifiable data registry]({{ '/terms/verifiable-data-registry/' | relative_url }})

### Semantic relations
- **related**: `urn:tig:concept:trust-list`
- **related**: `urn:tig:concept:verifiable-data-registry`

### Cross-vocabulary mappings
Not specified

## Provenance and identity
- **Concept ID**: `urn:tig:concept:trust-registry`
- **Editorial status**: `stable`
- **Provenance classification**: `adapted`
- **Source corpus**: Trust over IP Main Glossary

### Standards and source references
- ToIP CTWG maintained glossary source: `spec/terms-definitions/trust-registry.md`

<details markdown="1">
<summary><strong>Implementation and governance metadata</strong></summary>

### Legacy aliases
trust registry, trust registries

### Governance profile
- **Authority scope**: policy_definition, registry_management, governance_recognition
- **Delegation mode**: direct
- **Revocation supported**: True
- **Lifecycle states**: proposed, active, suspended, revoked, retired
- **Execution role**: runtime
- **Control-plane role**: decision_plane_component

### Enforcement points
- policy_approval
- registration_decision
- revocation_decision

### Assurance
**Evidence artifacts**
- policy_document
- registry_entry
- status_record

- **Assurance level hint**: AL2+
- **Auditability**: high

### Control plane
**Decision points**
- policy_approval
- registration_decision
- revocation_decision

- **Accountable entity**: governance_authority

**Evidence produced**
- policy_document
- registry_entry
- status_record

### Notes
- In operational terms, a trust registry often functions as a governance decision-plane component because its published information may be used to determine recognition, admission, status, or reliance.

### Supporting definitions
Not specified

### Mental models
Not specified

### Crosswalk references
- **NIST**: CA-3
- **ISO**: ISO/IEC 27001 A.5.19

</details>

---

*Generated from `glossary/terms/trust-registry.yaml`. Edit the source concept and regenerate rather than editing this page directly.*
