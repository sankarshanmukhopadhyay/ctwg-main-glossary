---
title: "delegatee"
---

> Generated file. Update `glossary/terms/delegatee.yaml` and regenerate artifacts instead of editing this page directly.

# delegatee

## Definition
The second party receiving a delegation from a first party (the delegator) and authorized to act only within the granted scope and applicable constraints.

## Aliases
delegatee, delegatees

## Governance Profile
- **Authority scope**: delegation_and_scope
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
- revocation_decision

- **Accountable entity**: glossary_maintainers

**Evidence produced**
- delegation_record
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
- authorization
- revocation

## Crosswalk References
Not specified
