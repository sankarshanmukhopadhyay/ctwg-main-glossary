---
title: "authorization-graph"
---

> Generated file. Update `glossary/terms/authorization-graph.yaml` and regenerate artifacts instead of editing this page directly.

# authorization-graph

## Definition
A graph of the authorization relationships between different entities in a trust-community. In a digital trust ecosystem, the governing body is typically the trust root of an authorization graph. In some cases, an authorization graph can be traversed by making queries to one or more trust registries.

## Aliases
authorization graph

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

- **Assurance level hint**: AL2+
- **Auditability**: high

## Control Plane
**Decision points**
- access_decision
- revocation_decision

- **Accountable entity**: glossary_maintainers

**Evidence produced**
- access_decision_log

## Notes
Not specified

## Supporting Definitions
Not specified

## Mental Models
Not specified

## See Also
- governance graph
- reputation graph
- trust graph.

## Crosswalk References
Not specified
