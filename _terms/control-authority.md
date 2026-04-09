---
title: "control-authority"
---

> Generated file. Update `glossary/terms/control-authority.yaml` and regenerate artifacts instead of editing this page directly.

# control-authority

## Definition
In identity systems, control authority is the power to determine who controls what. It is a primary factor in determining the basis for trust in those systems.

## Aliases
control-authority, control authority

## Governance Profile
- **Authority scope**: governance_recognition
- **Delegation mode**: direct
- **Revocation supported**: True
- **Lifecycle states**: proposed, active, suspended, revoked, retired
- **Execution role**: runtime
- **Control-plane role**: decision_plane_component

## Enforcement Points
- revocation_decision

## Assurance
**Evidence artifacts**
- definition_change_record

- **Assurance level hint**: AL2+
- **Auditability**: high

## Control Plane
**Decision points**
- revocation_decision

- **Accountable entity**: governance_authority

**Evidence produced**
- definition_change_record

## Notes
- Control authority is especially important because it identifies where effective operational power resides, including the power to change, invalidate, or reassign control relationships.

## Supporting Definitions
- The entity with *control authority* takes action through operations that affect the:
- - creation (inception)
- - updating
- - rotation
- - revocation
- - deletion
- - delegation
- of authentication factors and their relation to the identifier.

## Mental Models
Not specified

## See Also
Not specified

## Crosswalk References
Not specified
