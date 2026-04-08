---
title: "issuance-request"
---

# issuance-request

## Definition
A protocol request invoked by the holder of a digital wallet to obtain a digital credential from an issuer.

## Aliases
issuance request, issuance requests

## Governance Profile
- **Authority scope**: credential_issuance
- **Delegation mode**: direct
- **Revocation supported**: True
- **Lifecycle states**: proposed, active, suspended, revoked, retired
- **Execution role**: runtime
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

- **Accountable entity**: issuer_operator

**Evidence produced**
- issuance_log

## Notes
Not specified

## Supporting Definitions
Not specified

## Mental Models
Not specified

## See Also
- presentation request.

## Crosswalk References
Not specified
