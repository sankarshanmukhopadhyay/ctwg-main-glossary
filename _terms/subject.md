---
title: "subject"
---

# subject

The entity described by one or more claims, particularly in the context of credentials.

## Formal definition
The entity described by one or more claims, particularly in the context of credentials.

## Why this concept matters
This concept is provided as a controlled glossary entry for standards, governance, and implementation review.

Use this concept consistently when mapping authority, evidence, reliance, and auditability across governance and implementation artifacts.

## Names and relationships

### Alternative designations
- **subjects** (`en`, `alternative`)

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
- **Concept ID**: `urn:tig:concept:subject`
- **Editorial status**: `stable`
- **Provenance classification**: `adapted`
- **Source corpus**: Trust over IP Main Glossary

### Standards and source references
- ToIP CTWG maintained glossary source: `spec/terms-definitions/subject.md`

<details markdown="1">
<summary><strong>Implementation and governance metadata</strong></summary>

### Legacy aliases
subject, subjects

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
- [W3C VC](https://www.w3.org/TR/vc-data-model/#terminology): A thing about which [claims](https://www.w3.org/TR/vc-data-model/#dfn-claims) are made.
- [eSSIF-Lab:](https://essif-lab.github.io/framework/docs/essifLab-glossary#subject) the (single) [[ref: entity]] to which a given set of coherent [[ref: data]] relates/pertains. Examples of such sets include attributes, [[ref: Claims]]/Assertions, files/dossiers, [[ref: verifiable credentials]], [(partial) identities](https://essif-lab.github.io/framework/docs/terms/partial-identity), [employment contracts](https://essif-lab.github.io/framework/docs/terms/employment-contract), etc.

### Mental models
Not specified

### Crosswalk references
Not specified

</details>

---

*Generated from `glossary/terms/subject.yaml`. Edit the source concept and regenerate rather than editing this page directly.*
