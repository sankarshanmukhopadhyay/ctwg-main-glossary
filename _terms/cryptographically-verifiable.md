---
title: "cryptographically-verifiable"
---

# cryptographically-verifiable

A simple-English summary has not yet been added for this concept.

## Formal definition
A property of a data structure that has been digitally signed using a private key such that the digital signature can be verified using the public key. Verifiable data, verifiable messages, verifiable credentials, and verifiable data registries are all cryptographically verifiable. Cryptographic verifiability is a primary goal of the ToIP Technology Stack.

## Why this concept matters
This concept is provided as a controlled glossary entry for standards, governance, and implementation review.

Use this concept consistently when mapping authority, evidence, reliance, and auditability across governance and implementation artifacts.

## Names and relationships

### Alternative designations
- **cryptographically verifiable** (`en`, `alternative`)
- **cryptographically verified** (`en`, `alternative`)

### Related concepts
- [tamper evident]({{ '/terms/tamper-evident/' | relative_url }})
- [tamper resistant]({{ '/terms/tamper-resistant/' | relative_url }})

### Semantic relations
- **related**: `urn:tig:concept:tamper-evident`
- **related**: `urn:tig:concept:tamper-resistant`

### Cross-vocabulary mappings
Not specified

## Provenance and identity
- **Concept ID**: `urn:tig:concept:cryptographically-verifiable`
- **Editorial status**: `stable`
- **Provenance classification**: `adapted`
- **Source corpus**: Trust over IP Main Glossary

### Standards and source references
- ToIP CTWG maintained glossary source: `spec/terms-definitions/cryptographically-verifiable.md`

<details markdown="1">
<summary><strong>Implementation and governance metadata</strong></summary>

### Legacy aliases
cryptographically verifiable, cryptographically verified

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
- Contrast with: [[ref: human auditable]].

### Mental models
Not specified

### Crosswalk references
Not specified

</details>

---

*Generated from `glossary/terms/cryptographically-verifiable.yaml`. Edit the source concept and regenerate rather than editing this page directly.*
