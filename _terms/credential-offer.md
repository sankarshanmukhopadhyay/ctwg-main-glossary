---
title: "credential-offer"
---

# credential-offer

A simple-English summary has not yet been added for this concept.

## Formal definition
A protocol request invoked by an issuer to offer to issue a digital credential to the  holder of a digital wallet. If the request is invoked by the holder, it is called an issuance request.

## Why this concept matters
This concept is provided as a controlled glossary entry for standards, governance, and implementation review.

Use this concept consistently when mapping authority, evidence, reliance, and auditability across governance and implementation artifacts.

## Names and relationships

### Alternative designations
- **credential offer** (`en`, `alternative`)
- **credential offers** (`en`, `alternative`)

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
- **Concept ID**: `urn:tig:concept:credential-offer`
- **Editorial status**: `stable`
- **Provenance classification**: `adapted`
- **Source corpus**: Trust over IP Main Glossary

### Standards and source references
- ToIP CTWG maintained glossary source: `spec/terms-definitions/credential-offer.md`

<details markdown="1">
<summary><strong>Implementation and governance metadata</strong></summary>

### Legacy aliases
credential offer, credential offers

### Governance profile
- **Authority scope**: credential_issuance
- **Delegation mode**: direct
- **Revocation supported**: True
- **Lifecycle states**: proposed, active, suspended, revoked, retired
- **Execution role**: runtime
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

- **Accountable entity**: issuer_operator

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

*Generated from `glossary/terms/credential-offer.yaml`. Edit the source concept and regenerate rather than editing this page directly.*
