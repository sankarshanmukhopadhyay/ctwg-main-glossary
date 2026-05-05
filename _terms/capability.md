---
title: "capability"
---

> Generated file. Update `glossary/terms/capability.yaml` and regenerate artifacts instead of editing this page directly.

# capability

## Definition
The ability or permission for an actor or agent to perform a specific action on behalf of a party within a defined scope and subject to applicable constraints.

## Aliases
capability, capabilities

## Governance Profile
- **Authority scope**: delegation_and_scope, access_decisioning
- **Delegation mode**: direct_or_constrained
- **Revocation supported**: True
- **Lifecycle states**: proposed, active, suspended, revoked, retired
- **Execution role**: runtime
- **Control-plane role**: decision_plane_component

## Enforcement Points
- delegation_grant
- access_decision
- revocation_decision

## Assurance
**Evidence artifacts**
- delegation_record
- access_decision_log
- policy_document
- status_record
- audit_log
- verification_log
- registry_entry

- **Assurance level hint**: AL2+
- **Auditability**: high

## Control Plane
**Decision points**
- delegation_grant
- access_decision
- revocation_decision

- **Accountable entity**: glossary_maintainers

**Evidence produced**
- delegation_record
- access_decision_log
- policy_document
- status_record
- audit_log
- verification_log
- registry_entry

## Notes
Not specified

## Supporting Definitions
Not specified

## Mental Models
Not specified

## See Also
- delegation
- delegator
- delegatee
- authorization
- permission

## Crosswalk References
Not specified
