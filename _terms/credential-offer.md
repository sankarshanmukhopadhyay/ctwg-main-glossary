---
title: "credential-offer"
---

> Generated file. Update `glossary/terms/credential-offer.yaml` and regenerate artifacts instead of editing this page directly.

# credential-offer

## Definition
A protocol request invoked by an issuer to offer to issue a digital credential to the  holder of a digital wallet. If the request is invoked by the holder, it is called an issuance request.

## Aliases
credential offer, credential offers

## Governance Profile
- **Authority scope**: credential_issuance
- **Delegation mode**: direct
- **Revocation supported**: True
- **Lifecycle states**: proposed, active, suspended, revoked, retired
- **Execution role**: runtime
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

- **Accountable entity**: issuer_operator

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
