---
title: "authorized-organizational-representative"
---

# authorized-organizational-representative

## Definition
A person who has the authority to make claims, sign documents or otherwise commit resources on behalf of an organization.

## Aliases
authorized organizational representative

## Governance Profile
- **Authority scope**: credential_issuance, delegation_and_scope, governance_recognition
- **Delegation mode**: direct_or_constrained
- **Revocation supported**: True
- **Lifecycle states**: proposed, active, suspended, revoked, retired
- **Execution role**: runtime
- **Control-plane role**: decision_plane_component

## Enforcement Points
- delegation_grant
- issuance_decision
- revocation_decision

## Assurance
**Evidence artifacts**
- delegation_record
- issuance_log

- **Assurance level hint**: AL2+
- **Auditability**: high

## Control Plane
**Decision points**
- delegation_grant
- issuance_decision
- revocation_decision

- **Accountable entity**: governance_authority

**Evidence produced**
- delegation_record
- issuance_log

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
