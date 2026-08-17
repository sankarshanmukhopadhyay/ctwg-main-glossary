---
title: "claim"
---

> Generated file. Update `glossary/terms/claim.yaml` and regenerate artifacts instead of editing this page directly.

# claim

## In Simple English
A simple-English summary has not yet been added for this term.

## Definition
An assertion about a subject, typically expressed as an attribute or property of the subject. It is called a “claim” because the assertion is always made by some party, called the issuer of the claim, and the validity of the claim must be judged by the verifier.

## Reader Note
This term is provided as a controlled glossary entry for standards, governance, and implementation review.

## Implementation Relevance
Use this term consistently when mapping authority, evidence, reliance, and auditability across governance and implementation artifacts.

## Aliases
claim, claims, claimed, claiming

## See Also
- [credential]({{ '/terms/credential/' | relative_url }})
- [issuer]({{ '/terms/issuer/' | relative_url }})
- [issuance]({{ '/terms/issuance/' | relative_url }})
- [verifiable-credential]({{ '/terms/verifiable-credential/' | relative_url }})
- [verification]({{ '/terms/verification/' | relative_url }})
- [verifier]({{ '/terms/verifier/' | relative_url }})

## Standards and Source References
- ToIP CTWG maintained glossary source: `spec/terms-definitions/claim.md`

## Governance Profile
- **Authority scope**: credential_issuance, verification_and_reliance
- **Delegation mode**: direct
- **Revocation supported**: False
- **Lifecycle states**: documented, active, deprecated
- **Execution role**: runtime
- **Control-plane role**: decision_plane_component

## Enforcement Points
- reliance_decision
- issuance_decision

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

- **Accountable entity**: issuer_operator

**Evidence produced**
- issuance_log
- verification_log

## Notes
- If the issuer of the claim is also the subject of the claim, the claim is self-asserted.

## Supporting Definitions
- [W3C VC](https://www.w3.org/TR/vc-data-model/#terminology): An assertion made about a [subject](https://www.w3.org/TR/vc-data-model/#dfn-subjects).
- [Wikipedia](https://en.wikipedia.org/wiki/Claims-based_identity): A claim is a statement that one subject, such as a person or organization, makes about itself or another subject. For example, the statement can be about a name, group, buying preference, ethnicity, privilege, association or capability.

## Mental Models
Not specified

## Crosswalk References
Not specified
