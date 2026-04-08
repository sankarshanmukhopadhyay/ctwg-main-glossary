---
title: "toip-trust-registry-protocol"
---

# toip-trust-registry-protocol

## Definition
The open standard trust task protocol defined by the ToIP Foundation to perform the trust task of querying a trust registry. The ToIP Trust Registry Protocol operates at Layer 3 of the ToIP stack.

## Aliases
ToIP Trust Registry Protocol

## Governance Profile
- **Authority scope**: registry_management
- **Delegation mode**: direct
- **Revocation supported**: True
- **Lifecycle states**: proposed, active, suspended, revoked, retired
- **Execution role**: runtime
- **Control-plane role**: decision_plane_component

## Enforcement Points
- registration_decision
- revocation_decision

## Assurance
**Evidence artifacts**
- registry_entry

- **Assurance level hint**: AL2+
- **Auditability**: high

## Control Plane
**Decision points**
- registration_decision
- revocation_decision

- **Accountable entity**: registry_operator

**Evidence produced**
- registry_entry

## Notes
Not specified

## Supporting Definitions
Not specified

## Mental Models
Not specified

## See Also
Not specified

## Crosswalk References
Not specified
