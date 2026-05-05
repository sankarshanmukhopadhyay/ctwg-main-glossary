---
title: "keys-at-the-edge"
---

> Generated file. Update `glossary/terms/keys-at-the-edge.yaml` and regenerate artifacts instead of editing this page directly.

# keys-at-the-edge

## Definition
A key management architecture in which keys are stored on a user’s local edge devices, such as a smartphone, tablet, or laptop, and then used in conjunction with a secure protocol to unlock a key management system (KMS) and/or a digital vault in the cloud. This approach can enable the storage and sharing of large data structures that are not feasible on edge devices. This architecture can also be used in conjunction with confidential computing to enable cloud-based digital agents to safely carry out “user not present” operations.

## Aliases
keys-at-the-edge

## Governance Profile
- **Authority scope**: delegation_and_scope
- **Delegation mode**: direct_or_constrained
- **Revocation supported**: False
- **Lifecycle states**: documented, active, deprecated
- **Execution role**: runtime
- **Control-plane role**: decision_plane_component

## Enforcement Points
- delegation_grant

## Assurance
**Evidence artifacts**
- delegation_record

- **Assurance level hint**: AL2+
- **Auditability**: high

## Control Plane
**Decision points**
- delegation_grant

- **Accountable entity**: glossary_maintainers

**Evidence produced**
- delegation_record

## Notes
Not specified

## Supporting Definitions
- Also known as: [[ref: KATE]].

## Mental Models
Not specified

## See Also
- delegation
- delegator
- delegatee
- authorization

## Crosswalk References
Not specified
