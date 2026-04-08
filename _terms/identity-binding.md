---
title: "identity-binding"
---

# identity-binding

## Definition
The process of associating a set of identity data, such as a credential, with its subject, such as a natural person. The strength of an identity binding is one factor in determining an authenticator assurance level.

## Aliases
identity binding, identity bindings

## Governance Profile
- **Authority scope**: credential_issuance, access_decisioning, assurance_and_audit
- **Delegation mode**: direct
- **Revocation supported**: True
- **Lifecycle states**: proposed, active, suspended, revoked, retired
- **Execution role**: design
- **Control-plane role**: decision_plane_component

## Enforcement Points
- issuance_decision
- access_decision
- revocation_decision

## Assurance
**Evidence artifacts**
- issuance_log
- attestation

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
- attestation

## Notes
Not specified

## Supporting Definitions
Not specified

## Mental Models
Not specified

## See Also
- identity assurance level
- identity proofing.

## Crosswalk References
Not specified
