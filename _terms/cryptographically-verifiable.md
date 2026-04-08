---
title: "cryptographically-verifiable"
---

# cryptographically-verifiable

## Definition
A property of a data structure that has been digitally signed using a private key such that the digital signature can be verified using the public key. Verifiable data, verifiable messages, verifiable credentials, and verifiable data registries are all cryptographically verifiable. Cryptographic verifiability is a primary goal of the ToIP Technology Stack.

## Aliases
cryptographically verifiable, cryptographically verified

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
- Contrast with: [[ref: human auditable]].

## Mental Models
Not specified

## See Also
- tamper evident
- tamper resistant.

## Crosswalk References
Not specified
