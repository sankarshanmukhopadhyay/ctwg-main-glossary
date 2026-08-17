---
title: "dead-drop"
---

# dead-drop

A simple-English summary has not yet been added for this concept.

## Formal definition
In cybersecurity or digital privacy scenarios, the term "dead drop" refers to encrypted or secure virtual spaces where information can be deposited or retrieved anonymously. In the credentials field, the presenter controls the disclosure, so you can't re-identify the data.

## Why this concept matters
This concept is provided as a controlled glossary entry for standards, governance, and implementation review.

Use this concept consistently when mapping authority, evidence, reliance, and auditability across governance and implementation artifacts.

## Names and relationships

### Alternative designations
- **dead drop** (`en`, `alternative`)

### Related concepts
- [credential]({{ '/terms/credential/' | relative_url }})
- [issuer]({{ '/terms/issuer/' | relative_url }})
- [issuance]({{ '/terms/issuance/' | relative_url }})
- [verifiable-credential]({{ '/terms/verifiable-credential/' | relative_url }})

### Semantic relations
- **related**: `urn:tig:concept:credential`
- **related**: `urn:tig:concept:issuer`
- **related**: `urn:tig:concept:issuance`
- **related**: `urn:tig:concept:verifiable-credential`

### Cross-vocabulary mappings
Not specified

## Provenance and identity
- **Concept ID**: `urn:tig:concept:dead-drop`
- **Editorial status**: `stable`
- **Provenance classification**: `locally_defined`
- **Source corpus**: Trust Infrastructure Glossary

### Standards and source references
- Discussed in tech meet KERI [recording](https://hackmd.io/-soUScAqQEaSw5MJ71899w#2023-06-27), date June 27 2023.

<details markdown="1">
<summary><strong>Implementation and governance metadata</strong></summary>

### Legacy aliases
dead-drop, dead drop

### Governance profile
- **Authority scope**: credential_issuance
- **Delegation mode**: direct
- **Revocation supported**: True
- **Lifecycle states**: proposed, active, suspended, revoked, retired
- **Execution role**: design
- **Control-plane role**: decision_plane_component

### Enforcement points
- issuance_decision
- revocation_decision

### Assurance
**Evidence artifacts**
- issuance_log
- registry_entry
- status_record
- audit_log
- verification_log

- **Assurance level hint**: AL2+
- **Auditability**: high

### Control plane
**Decision points**
- issuance_decision
- revocation_decision

- **Accountable entity**: glossary_maintainers

**Evidence produced**
- issuance_log
- registry_entry
- status_record
- audit_log
- verification_log

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

*Generated from `glossary/terms/dead-drop.yaml`. Edit the source concept and regenerate rather than editing this page directly.*
