---
title: "digital-credential"
---

> Generated file. Update `glossary/terms/digital-credential.yaml` and regenerate artifacts instead of editing this page directly.

# digital-credential

## Concept Identity
- **Concept ID**: `urn:tig:concept:digital-credential`
- **Editorial status**: `stable`
- **Provenance classification**: `adapted`
- **Source corpus**: Trust over IP Main Glossary

## In Simple English
A simple-English summary has not yet been added for this term.

## Definition
A credential in digital form that is signed with a digital signature and held in a digital wallet. A digital credential is issued to a holder by an issuer; a proof of the credential is presented by the holder to a verifier.

## Reader Note
This term is provided as a controlled glossary entry for standards, governance, and implementation review.

## Implementation Relevance
Use this term consistently when mapping authority, evidence, reliance, and auditability across governance and implementation artifacts.

## Alternative Designations
- **digital credential** (`en`, `alternative`)
- **digital credentials** (`en`, `alternative`)

## Legacy Aliases
digital credential, digital credentials

## Semantic Relations
- **related**: `urn:tig:concept:issuance-request`
- **related**: `urn:tig:concept:presentation-request`
- **related**: `urn:tig:concept:verifiable-credential`

## Cross-Vocabulary Mappings
Not specified

## See Also
- [issuance request]({{ '/terms/issuance-request/' | relative_url }})
- [presentation request]({{ '/terms/presentation-request/' | relative_url }})
- [verifiable credential]({{ '/terms/verifiable-credential/' | relative_url }})

## Standards and Source References
- ToIP CTWG maintained glossary source: `spec/terms-definitions/digital-credential.md`

## Governance Profile
- **Authority scope**: credential_issuance, verification_and_reliance
- **Delegation mode**: direct
- **Revocation supported**: True
- **Lifecycle states**: proposed, active, suspended, revoked, retired
- **Execution role**: runtime
- **Control-plane role**: decision_plane_component

## Enforcement Points
- reliance_decision
- issuance_decision
- revocation_decision

## Assurance
**Evidence artifacts**
- issuance_log
- verification_log

- **Assurance level hint**: AL2+
- **Auditability**: high

## Control Plane
**Decision points**
- reliance_decision
- issuance_decision
- revocation_decision

- **Accountable entity**: issuer_operator

**Evidence produced**
- issuance_log
- verification_log

## Notes
Not specified

## Supporting Definitions
- Contrast with: [[ref: physical credential]].
- [Wikipedia](https://en.wikipedia.org/wiki/Digital_credential): Digital credentials are the digital equivalent of paper-based [credentials](https://en.wikipedia.org/wiki/Credentials). Just as a paper-based credential could be a [passport](https://en.wikipedia.org/wiki/Passport), a [driver's license](https://en.wikipedia.org/wiki/Driver%27s_license), a membership certificate or some kind of ticket to obtain some service, such as a cinema ticket or a public transport ticket, a digital credential is a proof of qualification, competence, or clearance that is attached to a person.

## Mental Models
Not specified

## Crosswalk References
Not specified
