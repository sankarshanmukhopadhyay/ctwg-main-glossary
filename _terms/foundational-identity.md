---
title: "foundational-identity"
---

# foundational-identity

## Definition
A set of identity data, such as a credential, issued by an authoritative source for the legal identity of the subject. Birth certificates, passports, driving licenses, and other forms of government ID documents are considered foundational identity documents. Foundational identities are often used to provide identity binding for functional identities.

## Aliases
foundational identity, foundational identities

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

- **Assurance level hint**: AL2+
- **Auditability**: high

## Control Plane
**Decision points**
- issuance_decision
- revocation_decision

- **Accountable entity**: glossary_maintainers

**Evidence produced**
- issuance_log

## Notes
Not specified

## Supporting Definitions
- Contrast with: [[ref: functional identity]].

## Mental Models
Not specified

## See Also
Not specified

## Crosswalk References
Not specified
