---
title: "cryptographically-verifiable"
---

> Generated file. Update `glossary/terms/cryptographically-verifiable.yaml` and regenerate artifacts instead of editing this page directly.

# cryptographically-verifiable

## Concept Identity
- **Concept ID**: `urn:tig:concept:cryptographically-verifiable`
- **Editorial status**: `stable`
- **Provenance classification**: `adapted`
- **Source corpus**: Trust over IP Main Glossary

## In Simple English
A simple-English summary has not yet been added for this term.

## Definition
A property of a data structure that has been digitally signed using a private key such that the digital signature can be verified using the public key. Verifiable data, verifiable messages, verifiable credentials, and verifiable data registries are all cryptographically verifiable. Cryptographic verifiability is a primary goal of the ToIP Technology Stack.

## Reader Note
This term is provided as a controlled glossary entry for standards, governance, and implementation review.

## Implementation Relevance
Use this term consistently when mapping authority, evidence, reliance, and auditability across governance and implementation artifacts.

## Alternative Designations
- **cryptographically verifiable** (`en`, `alternative`)
- **cryptographically verified** (`en`, `alternative`)

## Legacy Aliases
cryptographically verifiable, cryptographically verified

## Semantic Relations
- **related**: `urn:tig:concept:tamper-evident`
- **related**: `urn:tig:concept:tamper-resistant`

## Cross-Vocabulary Mappings
Not specified

## See Also
- [tamper evident]({{ '/terms/tamper-evident/' | relative_url }})
- [tamper resistant]({{ '/terms/tamper-resistant/' | relative_url }})

## Standards and Source References
- ToIP CTWG maintained glossary source: `spec/terms-definitions/cryptographically-verifiable.md`

## Governance Profile
- **Authority scope**: credential_issuance
- **Delegation mode**: direct
- **Revocation supported**: True
- **Lifecycle states**: proposed, active, suspended, revoked, retired
- **Execution role**: design
- **Control-plane role**: decision_plane_component

## Enforcement Points
- issuance_decision
- revocation_decision

## Assurance
**Evidence artifacts**
- issuance_log
- registry_entry
- status_record
- audit_log
- verification_log

- **Assurance level hint**: AL2+
- **Auditability**: high

## Control Plane
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

## Notes
Not specified

## Supporting Definitions
- Contrast with: [[ref: human auditable]].

## Mental Models
Not specified

## Crosswalk References
Not specified
