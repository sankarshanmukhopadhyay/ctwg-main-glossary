---
title: "delegation"
---

> Generated file. Update `glossary/terms/delegation.yaml` and regenerate artifacts instead of editing this page directly.

# delegation

## Definition
The act of a first party (the delegator) authorizing a second party (the delegatee) to perform a defined set of actions on behalf of the first party within an authorized scope and subject to applicable constraints.

## Aliases
delegation, delegate, delegated, delegates

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
- Delegation may be expressed through a [[ref: delegation credential]] or other policy-governed mechanism and may be limited by scope, time, conditions, or revocation.
- More specific for KERI see: [[xref: keri1, delegated-identifier]]

## Mental Models
Not specified

## See Also
- delegator
- delegatee
- authorization
- revocation

## Crosswalk References
- **NIST**: AC-6
- **ISO**: ISO/IEC 42001 8.3
