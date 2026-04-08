---
title: "trust-graph"
---

# trust-graph

## Definition
A data structure describing the trust relationship between two or more entities. A simple trust graph may be expressed as a trust list. More complex trust graphs can be recorded or registered in and queried from a trust registry. Trust graphs can also be expressed using trust chains and chained credentials. Trust graphs can enable verifiers and relying parties to make transitive trust decisions.

## Aliases
trust graph, trust graphs

## Governance Profile
- **Authority scope**: credential_issuance, verification_and_reliance, registry_management
- **Delegation mode**: direct
- **Revocation supported**: True
- **Lifecycle states**: proposed, active, suspended, revoked, retired
- **Execution role**: runtime
- **Control-plane role**: decision_plane_component

## Enforcement Points
- registration_decision
- reliance_decision
- issuance_decision
- revocation_decision

## Assurance
**Evidence artifacts**
- registry_entry
- issuance_log
- verification_log

- **Assurance level hint**: AL2+
- **Auditability**: high

## Control Plane
**Decision points**
- registration_decision
- reliance_decision
- issuance_decision
- revocation_decision

- **Accountable entity**: verifier_operator

**Evidence produced**
- registry_entry
- issuance_log
- verification_log

## Notes
Not specified

## Supporting Definitions
Not specified

## Mental Models
Not specified

## See Also
- authorization graph
- governance graph
- reputation graph.

## Crosswalk References
Not specified
