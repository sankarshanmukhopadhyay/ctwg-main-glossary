---
title: "trust-chain"
---

# trust-chain

## Definition
A set of cryptographically verifiable links between digital credentials or other data containers that enable transitive trust decisions.

## Aliases
trust chain, trust chains

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

- **Assurance level hint**: AL2+
- **Auditability**: high

## Control Plane
**Decision points**
- issuance_decision
- revocation_decision

- **Accountable entity**: glossary_maintainers

**Evidence produced**
- issuance_log

## Notes
Not specified

## Supporting Definitions
- For more information, see: [Design Principles for the ToIP Stack](https://trustoverip.org/our-work/design-principles/).

## Mental Models
Not specified

## See Also
- chained credentials
- trust graph.

## Crosswalk References
Not specified
