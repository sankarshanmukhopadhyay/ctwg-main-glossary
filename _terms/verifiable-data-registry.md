---
title: "verifiable-data-registry"
---

# verifiable-data-registry

A simple-English summary has not yet been added for this concept.

## Formal definition
A registry that facilitates the creation, verification, updating, and/or deactivation of decentralized identifiers and DID documents. A verifiable data registry may also be used for other cryptographically-verifiable data structures such as verifiable credentials.

## Why this concept matters
This concept is provided as a controlled glossary entry for standards, governance, and implementation review.

Use this concept consistently when mapping authority, evidence, reliance, and auditability across governance and implementation artifacts.

## Names and relationships

### Alternative designations
- **verifiable data registry** (`en`, `alternative`)
- **verifiable data registries** (`en`, `alternative`)
- **VDR** (`en`, `alternative`)
- **VDRs** (`en`, `alternative`)

### Related concepts
- [authoritative source]({{ '/terms/authoritative-source/' | relative_url }})
- [trust registry]({{ '/terms/trust-registry/' | relative_url }})
- [system of record]({{ '/terms/system-of-record/' | relative_url }})

### Semantic relations
- **related**: `urn:tig:concept:authoritative-source`
- **related**: `urn:tig:concept:trust-registry`
- **related**: `urn:tig:concept:system-of-record`

### Cross-vocabulary mappings
Not specified

## Provenance and identity
- **Concept ID**: `urn:tig:concept:verifiable-data-registry`
- **Editorial status**: `stable`
- **Provenance classification**: `locally_defined`
- **Source corpus**: Trust Infrastructure Glossary

### Standards and source references
- [W3C DID](https://www.w3.org/TR/did-core/#terminology)

<details markdown="1">
<summary><strong>Implementation and governance metadata</strong></summary>

### Legacy aliases
verifiable data registry, verifiable data registries, VDR, VDRs

### Governance profile
- **Authority scope**: credential_issuance, registry_management
- **Delegation mode**: direct
- **Revocation supported**: True
- **Lifecycle states**: proposed, active, suspended, revoked, retired
- **Execution role**: runtime
- **Control-plane role**: decision_plane_component

### Enforcement points
- registration_decision
- issuance_decision
- revocation_decision

### Assurance
**Evidence artifacts**
- registry_entry
- issuance_log

- **Assurance level hint**: AL2+
- **Auditability**: high

### Control plane
**Decision points**
- registration_decision
- issuance_decision
- revocation_decision

- **Accountable entity**: registry_operator

**Evidence produced**
- registry_entry
- issuance_log

### Notes
- There is an earlier definition in the W3C VC 1.1. glossary that is not as mature as this one (it is not clear about the use of cryptographically verifiable data structures). We do not recommend that definition.

### Supporting definitions
- Also known as: [[ref: VDR]].
- For more information, see: [[ref: W3C Verifiable Credentials Data Model Specification]].

### Mental models
- [W3C Verifiable Credentials Data Model Roles & Information Flows](https://www.w3.org/TR/vc-data-model/#roles)

### Crosswalk references
Not specified

</details>

---

*Generated from `glossary/terms/verifiable-data-registry.yaml`. Edit the source concept and regenerate rather than editing this page directly.*
