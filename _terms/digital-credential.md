---
title: "digital-credential"
---

# digital-credential

A simple-English summary has not yet been added for this concept.

## Formal definition
A credential in digital form that is signed with a digital signature and held in a digital wallet. A digital credential is issued to a holder by an issuer; a proof of the credential is presented by the holder to a verifier.

## Why this concept matters
This concept is provided as a controlled glossary entry for standards, governance, and implementation review.

Use this concept consistently when mapping authority, evidence, reliance, and auditability across governance and implementation artifacts.

## Names and relationships

### Alternative designations
- **digital credential** (`en`, `alternative`)
- **digital credentials** (`en`, `alternative`)

### Related concepts
- [issuance request]({{ '/terms/issuance-request/' | relative_url }})
- [presentation request]({{ '/terms/presentation-request/' | relative_url }})
- [verifiable credential]({{ '/terms/verifiable-credential/' | relative_url }})

### Semantic relations
- **related**: `urn:tig:concept:issuance-request`
- **related**: `urn:tig:concept:presentation-request`
- **related**: `urn:tig:concept:verifiable-credential`

### Cross-vocabulary mappings
Not specified

## Provenance and identity
- **Concept ID**: `urn:tig:concept:digital-credential`
- **Editorial status**: `stable`
- **Provenance classification**: `adapted`
- **Source corpus**: Trust over IP Main Glossary

### Standards and source references
- ToIP CTWG maintained glossary source: `spec/terms-definitions/digital-credential.md`

<details markdown="1">
<summary><strong>Implementation and governance metadata</strong></summary>

### Legacy aliases
digital credential, digital credentials

### Governance profile
- **Authority scope**: credential_issuance, verification_and_reliance
- **Delegation mode**: direct
- **Revocation supported**: True
- **Lifecycle states**: proposed, active, suspended, revoked, retired
- **Execution role**: runtime
- **Control-plane role**: decision_plane_component

### Enforcement points
- reliance_decision
- issuance_decision
- revocation_decision

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
- revocation_decision

- **Accountable entity**: issuer_operator

**Evidence produced**
- issuance_log
- verification_log

### Notes
Not specified

### Supporting definitions
- Contrast with: [[ref: physical credential]].
- [Wikipedia](https://en.wikipedia.org/wiki/Digital_credential): Digital credentials are the digital equivalent of paper-based [credentials](https://en.wikipedia.org/wiki/Credentials). Just as a paper-based credential could be a [passport](https://en.wikipedia.org/wiki/Passport), a [driver's license](https://en.wikipedia.org/wiki/Driver%27s_license), a membership certificate or some kind of ticket to obtain some service, such as a cinema ticket or a public transport ticket, a digital credential is a proof of qualification, competence, or clearance that is attached to a person.

### Mental models
Not specified

### Crosswalk references
Not specified

</details>

---

*Generated from `glossary/terms/digital-credential.yaml`. Edit the source concept and regenerate rather than editing this page directly.*
