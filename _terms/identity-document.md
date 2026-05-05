---
title: "identity-document"
---

> Generated file. Update `glossary/terms/identity-document.yaml` and regenerate artifacts instead of editing this page directly.

# identity-document

## Definition
A physical or digital document containing identity data. A credential is a specialized form of identity document. Birth certificates, bank statements, and utility bills can all be considered identity documents.

## Aliases
identity document, identity documents

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
- registry_entry
- status_record
- audit_log
- verification_log

- **Assurance level hint**: AL2+
- **Auditability**: high

## Control Plane
**Decision points**
- issuance_decision
- revocation_decision

- **Accountable entity**: glossary_maintainers

**Evidence produced**
- issuance_log
- registry_entry
- status_record
- audit_log
- verification_log

## Notes
Not specified

## Supporting Definitions
Not specified

## Mental Models
Not specified

## See Also
- credential
- issuer
- issuance
- verifiable-credential

## Crosswalk References
Not specified
