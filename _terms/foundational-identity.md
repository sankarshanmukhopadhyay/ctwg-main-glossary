---
title: "foundational-identity"
---

> Generated file. Update `glossary/terms/foundational-identity.yaml` and regenerate artifacts instead of editing this page directly.

# foundational-identity

## In Simple English
A simple-English summary has not yet been added for this term.

## Definition
A set of identity data, such as a credential, issued by an authoritative source for the legal identity of the subject. Birth certificates, passports, driving licenses, and other forms of government ID documents are considered foundational identity documents. Foundational identities are often used to provide identity binding for functional identities.

## Reader Note
This term is provided as a controlled glossary entry for standards, governance, and implementation review.

## Implementation Relevance
Use this term consistently when mapping authority, evidence, reliance, and auditability across governance and implementation artifacts.

## Aliases
foundational identity, foundational identities

## See Also
- [credential]({{ '/terms/credential/' | relative_url }})
- [issuer]({{ '/terms/issuer/' | relative_url }})
- [issuance]({{ '/terms/issuance/' | relative_url }})
- [verifiable-credential]({{ '/terms/verifiable-credential/' | relative_url }})
- [governance]({{ '/terms/governance/' | relative_url }})
- [governance-framework]({{ '/terms/governance-framework/' | relative_url }})

## Standards and Source References
- ToIP CTWG maintained glossary source: `spec/terms-definitions/foundational-identity.md`

## Governance Profile
- **Authority scope**: credential_issuance, governance_recognition
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
- Contrast with: [[ref: functional identity]].

## Mental Models
Not specified

## Crosswalk References
Not specified
