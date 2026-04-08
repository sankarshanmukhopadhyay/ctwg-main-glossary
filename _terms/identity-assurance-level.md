---
title: "identity-assurance-level"
---

# identity-assurance-level

## Definition
A category that conveys the degree of confidence that a person’s claimed identity is their real identity, for example as defined in NIST SP 800-63-3 in terms of three levels: IAL 1 (Some confidence), IAL 2 (High confidence), IAL 3 (Very high confidence).

## Aliases
identity assurance level, identity assurance levels, IAL, IALs

## Governance Profile
- **Authority scope**: credential_issuance, assurance_and_audit
- **Delegation mode**: direct
- **Revocation supported**: False
- **Lifecycle states**: documented, active, deprecated
- **Execution role**: design
- **Control-plane role**: decision_plane_component

## Enforcement Points
- issuance_decision

## Assurance
**Evidence artifacts**
- issuance_log
- attestation

- **Assurance level hint**: AL1+
- **Auditability**: moderate

## Control Plane
**Decision points**
- issuance_decision

- **Accountable entity**: glossary_maintainers

**Evidence produced**
- issuance_log
- attestation

## Notes
Not specified

## Supporting Definitions
Not specified

## Mental Models
Not specified

## See Also
- authenticator assurance level
- federation assurance level.

## Crosswalk References
Not specified
