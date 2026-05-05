---
title: "registration-agent"
---

> Generated file. Update `glossary/terms/registration-agent.yaml` and regenerate artifacts instead of editing this page directly.

# registration-agent

## Definition
A party responsible for accepting registration requests and authenticating the registrant. The term may also apply to a party accepting issuance requests for digital credentials.

## Aliases
registration agent

## Governance Profile
- **Authority scope**: credential_issuance, delegation_and_scope
- **Delegation mode**: direct_or_constrained
- **Revocation supported**: True
- **Lifecycle states**: proposed, active, suspended, revoked, retired
- **Execution role**: runtime
- **Control-plane role**: decision_plane_component

## Enforcement Points
- delegation_grant
- issuance_decision
- revocation_decision

## Assurance
**Evidence artifacts**
- delegation_record
- issuance_log
- policy_document
- registry_entry
- status_record
- audit_log
- verification_log

- **Assurance level hint**: AL2+
- **Auditability**: high

## Control Plane
**Decision points**
- delegation_grant
- issuance_decision
- revocation_decision

- **Accountable entity**: glossary_maintainers

**Evidence produced**
- delegation_record
- issuance_log
- policy_document
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
- delegation
- delegator

## Crosswalk References
Not specified
