---
title: "authenticator"
---

> Generated file. Update `glossary/terms/authenticator.yaml` and regenerate artifacts instead of editing this page directly.

# authenticator

## Definition
Something the claimant possesses and controls (typically a cryptographic module or password) that is used to authenticate the claimant’s identity.

## Aliases
authenticator

## Governance Profile
- **Authority scope**: credential_issuance, access_decisioning
- **Delegation mode**: direct
- **Revocation supported**: True
- **Lifecycle states**: proposed, active, suspended, revoked, retired
- **Execution role**: runtime
- **Control-plane role**: decision_plane_component

## Enforcement Points
- issuance_decision
- access_decision
- revocation_decision

## Assurance
**Evidence artifacts**
- issuance_log

- **Assurance level hint**: AL2+
- **Auditability**: high

## Control Plane
**Decision points**
- issuance_decision
- access_decision
- revocation_decision

- **Accountable entity**: glossary_maintainers

**Evidence produced**
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
