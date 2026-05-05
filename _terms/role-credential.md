---
title: "role-credential"
---

> Generated file. Update `glossary/terms/role-credential.yaml` and regenerate artifacts instead of editing this page directly.

# role-credential

## Definition
A credential claiming that the subject has a specific role.

## Aliases
role credential, role credentials

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
- registry_entry
- status_record
- audit_log
- verification_log

- **Assurance level hint**: AL2+
- **Auditability**: high

## Control Plane
**Decision points**
- issuance_decision
- revocation_decision

- **Accountable entity**: glossary_maintainers

**Evidence produced**
- issuance_log
- registry_entry
- status_record
- audit_log
- verification_log

## Notes
Not specified

## Supporting Definitions
Not specified

## Mental Models
Not specified

## See Also
- credential
- issuer
- issuance
- verifiable-credential

## Crosswalk References
Not specified
