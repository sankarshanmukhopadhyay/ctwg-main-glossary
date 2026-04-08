---
title: "delegator"
---

# delegator

## Definition
The first party that makes a delegation to a second party (the delegatee) and remains accountable for granting authority within the permitted scope.

## Aliases
delegator, delegators

## Governance Profile
- **Authority scope**: delegation_and_scope, governance_recognition
- **Delegation mode**: direct_or_constrained
- **Revocation supported**: True
- **Lifecycle states**: proposed, active, suspended, revoked, retired
- **Execution role**: runtime
- **Control-plane role**: decision_plane_component

## Enforcement Points
- delegation_grant
- revocation_decision

## Assurance
**Evidence artifacts**
- delegation_record

- **Assurance level hint**: AL2+
- **Auditability**: high

## Control Plane
**Decision points**
- delegation_grant
- revocation_decision

- **Accountable entity**: governance_authority

**Evidence produced**
- delegation_record

## Notes
Not specified

## Supporting Definitions
- [eSSIF-Lab](https://essif-lab.github.io/framework/docs/essifLab): the transferral of [ownership](https://essif-lab.github.io/framework/docs/terms/ownership) of one or more obligation of a [party](https://essif-lab.github.io/framework/docs/terms/party) (the [delegator](https://essif-lab.github.io/framework/docs/terms/delegate)), including the associated accountability, to another party (the [delegatee](https://essif-lab.github.io/framework/docs/terms/delegate)), which implies that the delegatee can realize such obligation as it sees fit.

## Mental Models
Not specified

## See Also
Not specified

## Crosswalk References
Not specified
