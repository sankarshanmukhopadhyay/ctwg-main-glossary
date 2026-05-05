---
title: "permission"
---

> Generated file. Update `glossary/terms/permission.yaml` and regenerate artifacts instead of editing this page directly.

# permission

## Definition
Authorization to perform some action on a system.

## Aliases
permission, permissions

## Governance Profile
- **Authority scope**: access_decisioning
- **Delegation mode**: direct
- **Revocation supported**: True
- **Lifecycle states**: proposed, active, suspended, revoked, retired
- **Execution role**: runtime
- **Control-plane role**: decision_plane_component

## Enforcement Points
- access_decision
- revocation_decision

## Assurance
**Evidence artifacts**
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
- access_decision
- revocation_decision

- **Accountable entity**: glossary_maintainers

**Evidence produced**
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
- authorization
- role-based-access-control
- attribute-based-access-control
- access-control
- revocation

## Crosswalk References
Not specified
