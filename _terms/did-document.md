---
title: "did-document"
---

> Generated file. Update `glossary/terms/did-document.yaml` and regenerate artifacts instead of editing this page directly.

# did-document

## Definition
A set of data describing the DID subject, including mechanisms, such as cryptographic public keys, that the DID subject or a DID delegate can use to authenticate itself and prove its association with the DID. A DID document might have one or more different representations as defined in section 6 of the W3C Decentralized Identifiers (DIDs) 1.0 specification.

## Aliases
DID document, DID documents, DID doc, DID docs

## Governance Profile
- **Authority scope**: delegation_and_scope
- **Delegation mode**: direct_or_constrained
- **Revocation supported**: True
- **Lifecycle states**: proposed, active, suspended, revoked, retired
- **Execution role**: runtime
- **Control-plane role**: decision_plane_component

## Enforcement Points
- delegation_grant
- revocation_decision

## Assurance
**Evidence artifacts**
- delegation_record
- policy_document
- status_record
- audit_log
- verification_log
- registry_entry

- **Assurance level hint**: AL2+
- **Auditability**: high

## Control Plane
**Decision points**
- delegation_grant
- revocation_decision

- **Accountable entity**: glossary_maintainers

**Evidence produced**
- delegation_record
- policy_document
- status_record
- audit_log
- verification_log
- registry_entry

## Notes
Not specified

## Supporting Definitions
Not specified

## Mental Models
Not specified

## See Also
- delegation
- delegator
- delegatee
- authorization

## Crosswalk References
Not specified
