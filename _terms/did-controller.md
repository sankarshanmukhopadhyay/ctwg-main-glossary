---
title: "did-controller"
---

# did-controller

## Definition
An entity that has the capability to make changes to a DID document. A DID might have more than one DID controller. The DID controller(s) can be denoted by the optional `controller` property at the top level of the DID document. Note that a DID controller might be the DID subject.

## Aliases
DID controller, DID controllers

## Governance Profile
- **Authority scope**: access_decisioning
- **Delegation mode**: direct
- **Revocation supported**: False
- **Lifecycle states**: documented, active, deprecated
- **Execution role**: runtime
- **Control-plane role**: decision_plane_component

## Enforcement Points
- access_decision

## Assurance
**Evidence artifacts**
- access_decision_log

- **Assurance level hint**: AL2+
- **Auditability**: high

## Control Plane
**Decision points**
- access_decision

- **Accountable entity**: glossary_maintainers

**Evidence produced**
- access_decision_log

## Notes
Not specified

## Supporting Definitions
Not specified

## Mental Models
Not specified

## See Also
- controller.

## Crosswalk References
Not specified
