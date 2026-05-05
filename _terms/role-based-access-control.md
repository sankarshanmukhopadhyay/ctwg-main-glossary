---
title: "role-based-access-control"
---

> Generated file. Update `glossary/terms/role-based-access-control.yaml` and regenerate artifacts instead of editing this page directly.

# role-based-access-control

## Definition
Access control based on user roles (i.e., a collection of access authorizations a user receives based on an explicit or implicit assumption of a given role). Role permissions may be inherited through a role hierarchy and typically reflect the permissions needed to perform defined functions within an organization. A given role may apply to a single individual or to several individuals.

## Aliases
role-based access control, role-based access controls

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
- [Wikipedia](https://en.wikipedia.org/wiki/Role-based_access_control): In computer systems security, role-based access control (RBAC) or role-based security is an approach to restricting system access to authorized users, and to implementing [mandatory access control](https://en.wikipedia.org/wiki/Mandatory_access_control) (MAC) or [discretionary access control](https://en.wikipedia.org/wiki/Discretionary_access_control) (DAC).

## Mental Models
Not specified

## See Also
- authorization
- permission
- attribute-based-access-control
- access-control

## Crosswalk References
Not specified
