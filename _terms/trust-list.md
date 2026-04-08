---
title: "trust-list"
---

# trust-list

## Definition
A one-dimensional trust graph in which an authoritative source publishes a list of entities that are trusted in a specific trust context. A trust list can be considered a simplified form of a trust registry.

## Aliases
trust list, trust lists

## Governance Profile
- **Authority scope**: registry_management, governance_recognition
- **Delegation mode**: direct
- **Revocation supported**: True
- **Lifecycle states**: proposed, active, suspended, revoked, retired
- **Execution role**: runtime
- **Control-plane role**: decision_plane_component

## Enforcement Points
- registration_decision
- revocation_decision

## Assurance
**Evidence artifacts**
- registry_entry

- **Assurance level hint**: AL2+
- **Auditability**: high

## Control Plane
**Decision points**
- registration_decision
- revocation_decision

- **Accountable entity**: registry_operator

**Evidence produced**
- registry_entry

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
