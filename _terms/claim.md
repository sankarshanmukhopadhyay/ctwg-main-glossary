---
title: "claim"
---

# claim

A simple-English summary has not yet been added for this concept.

## Formal definition
An assertion about a subject, typically expressed as an attribute or property of the subject. It is called a “claim” because the assertion is always made by some party, called the issuer of the claim, and the validity of the claim must be judged by the verifier.

## Why this concept matters
This concept is provided as a controlled glossary entry for standards, governance, and implementation review.

Use this concept consistently when mapping authority, evidence, reliance, and auditability across governance and implementation artifacts.

## Names and relationships

### Alternative designations
- **claims** (`en`, `alternative`)
- **claimed** (`en`, `alternative`)
- **claiming** (`en`, `alternative`)

### Related concepts
- [credential]({{ '/terms/credential/' | relative_url }})
- [issuer]({{ '/terms/issuer/' | relative_url }})
- [issuance]({{ '/terms/issuance/' | relative_url }})
- [verifiable-credential]({{ '/terms/verifiable-credential/' | relative_url }})
- [verification]({{ '/terms/verification/' | relative_url }})
- [verifier]({{ '/terms/verifier/' | relative_url }})

### Semantic relations
- **related**: `urn:tig:concept:credential`
- **related**: `urn:tig:concept:issuer`
- **related**: `urn:tig:concept:issuance`
- **related**: `urn:tig:concept:verifiable-credential`
- **related**: `urn:tig:concept:verification`
- **related**: `urn:tig:concept:verifier`

### Cross-vocabulary mappings
Not specified

## Provenance and identity
- **Concept ID**: `urn:tig:concept:claim`
- **Editorial status**: `stable`
- **Provenance classification**: `adapted`
- **Source corpus**: Trust over IP Main Glossary

### Standards and source references
- ToIP CTWG maintained glossary source: `spec/terms-definitions/claim.md`

<details markdown="1">
<summary><strong>Implementation and governance metadata</strong></summary>

### Legacy aliases
claim, claims, claimed, claiming

### Governance profile
- **Authority scope**: credential_issuance, verification_and_reliance
- **Delegation mode**: direct
- **Revocation supported**: False
- **Lifecycle states**: documented, active, deprecated
- **Execution role**: runtime
- **Control-plane role**: decision_plane_component

### Enforcement points
- reliance_decision
- issuance_decision

### Assurance
**Evidence artifacts**
- issuance_log
- verification_log

- **Assurance level hint**: AL2+
- **Auditability**: high

### Control plane
**Decision points**
- reliance_decision
- issuance_decision

- **Accountable entity**: issuer_operator

**Evidence produced**
- issuance_log
- verification_log

### Notes
- If the issuer of the claim is also the subject of the claim, the claim is self-asserted.

### Supporting definitions
- [W3C VC](https://www.w3.org/TR/vc-data-model/#terminology): An assertion made about a [subject](https://www.w3.org/TR/vc-data-model/#dfn-subjects).
- [Wikipedia](https://en.wikipedia.org/wiki/Claims-based_identity): A claim is a statement that one subject, such as a person or organization, makes about itself or another subject. For example, the statement can be about a name, group, buying preference, ethnicity, privilege, association or capability.

### Mental models
Not specified

### Crosswalk references
Not specified

</details>

---

*Generated from `glossary/terms/claim.yaml`. Edit the source concept and regenerate rather than editing this page directly.*
