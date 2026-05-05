---
title: "transitive-trust-decision"
---

> Generated file. Update `glossary/terms/transitive-trust-decision.yaml` and regenerate artifacts instead of editing this page directly.

# transitive-trust-decision

## Definition
A trust decision made by a first party about a second party or another entity based on information about the second party or the other entity that is obtained from one or more third parties.

## Aliases
transitive trust decision, transitive trust decisions

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
- A primary purpose of digital credentials, chained credentials, trust registries, and the ToIP stack is to facilitate transitive trust decisions.

## Supporting Definitions
- For more information, see: [Design Principles for the ToIP Stack](https://trustoverip.org/our-work/design-principles/).

## Mental Models
Not specified

## See Also
- credential
- issuer
- issuance
- verifiable-credential

## Crosswalk References
Not specified
