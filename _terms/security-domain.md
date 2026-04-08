---
title: "security-domain"
---

# security-domain

## Definition
An environment or context that includes a set of system resources and a set of system entities that have the right to access the resources as defined by a common security policy, security model, or security architecture.

## Aliases
security domain, security domains

## Governance Profile
- **Authority scope**: policy_definition
- **Delegation mode**: direct
- **Revocation supported**: False
- **Lifecycle states**: documented, active, deprecated
- **Execution role**: runtime
- **Control-plane role**: decision_plane_component

## Enforcement Points
- policy_approval

## Assurance
**Evidence artifacts**
- policy_document

- **Assurance level hint**: AL2+
- **Auditability**: high

## Control Plane
**Decision points**
- policy_approval

- **Accountable entity**: glossary_maintainers

**Evidence produced**
- policy_document

## Notes
Not specified

## Supporting Definitions
- See also KERI's [[xref: keri1, security-cost-performance-architecture-trade-off]]

## Mental Models
Not specified

## See Also
- trust domain.

## Crosswalk References
Not specified
