---
title: "trust-registry"
---

# trust-registry

## Definition
A registry that serves as an authoritative source for trust graphs or other governed information describing one or more trust communities. A trust registry is typically authorized by a governance framework.

## Aliases
trust registry, trust registries

## Governance Profile
- **Authority scope**: policy_definition, registry_management, governance_recognition
- **Delegation mode**: direct
- **Revocation supported**: True
- **Lifecycle states**: proposed, active, suspended, revoked, retired
- **Execution role**: runtime
- **Control-plane role**: decision_plane_component

## Enforcement Points
- policy_approval
- registration_decision
- revocation_decision

## Assurance
**Evidence artifacts**
- policy_document
- registry_entry
- status_record

- **Assurance level hint**: AL2+
- **Auditability**: high

## Control Plane
**Decision points**
- policy_approval
- registration_decision
- revocation_decision

- **Accountable entity**: governance_authority

**Evidence produced**
- policy_document
- registry_entry
- status_record

## Notes
- In operational terms, a trust registry often functions as a governance decision-plane component because its published information may be used to determine recognition, admission, status, or reliance.

## Supporting Definitions
Not specified

## Mental Models
Not specified

## See Also
- trust list
- verifiable data registry.

## Crosswalk References
- **NIST**: CA-3
- **ISO**: ISO/IEC 27001 A.5.19
