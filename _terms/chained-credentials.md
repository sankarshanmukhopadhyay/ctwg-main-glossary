---
title: "chained-credentials"
---

# chained-credentials

## Definition
Two or more credentials linked together to create a trust chain between the credentials that is cryptographically verifiable.

## Aliases
chained credentials

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
- ACDCs are a type of digital credential that explicitly supports chaining.

## Supporting Definitions
Not specified

## Mental Models
Not specified

## See Also
Not specified

## Crosswalk References
Not specified
