---
title: "verifiable-data-registry"
---

# verifiable-data-registry

## Definition
A registry that facilitates the creation, verification, updating, and/or deactivation of decentralized identifiers and DID documents. A verifiable data registry may also be used for other cryptographically-verifiable data structures such as verifiable credentials.

## Aliases
verifiable data registry, verifiable data registries, VDR, VDRs

## Governance Profile
- **Authority scope**: credential_issuance, registry_management
- **Delegation mode**: direct
- **Revocation supported**: True
- **Lifecycle states**: proposed, active, suspended, revoked, retired
- **Execution role**: runtime
- **Control-plane role**: decision_plane_component

## Enforcement Points
- registration_decision
- issuance_decision
- revocation_decision

## Assurance
**Evidence artifacts**
- registry_entry
- issuance_log

- **Assurance level hint**: AL2+
- **Auditability**: high

## Control Plane
**Decision points**
- registration_decision
- issuance_decision
- revocation_decision

- **Accountable entity**: registry_operator

**Evidence produced**
- registry_entry
- issuance_log

## Notes
- There is an earlier definition in the W3C VC 1.1. glossary that is not as mature as this one (it is not clear about the use of cryptographically verifiable data structures). We do not recommend that definition.

## Supporting Definitions
- Also known as: [[ref: VDR]].
- For more information, see: [[ref: W3C Verifiable Credentials Data Model Specification]].

## Mental Models
- [W3C Verifiable Credentials Data Model Roles & Information Flows](https://www.w3.org/TR/vc-data-model/#roles)

## See Also
- authoritative source
- trust registry
- system of record.

## Crosswalk References
Not specified
