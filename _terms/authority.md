---
title: "authority"
---

> Generated file. Update `glossary/terms/authority.yaml` and regenerate artifacts instead of editing this page directly.

# authority

## Definition
A party whose decisions, policies, rules, or recognition outcomes are accepted as governing, directive, or controlling by other parties within a defined scope.

## Aliases
authority, authorities

## Governance Profile
- **Authority scope**: policy_definition, delegation_and_scope, governance_recognition
- **Delegation mode**: direct_or_constrained
- **Revocation supported**: True
- **Lifecycle states**: proposed, active, suspended, revoked, retired
- **Execution role**: runtime
- **Control-plane role**: decision_plane_component

## Enforcement Points
- policy_approval
- delegation_grant
- revocation_decision

## Assurance
**Evidence artifacts**
- policy_document
- delegation_record
- status_record

- **Assurance level hint**: AL2+
- **Auditability**: high

## Control Plane
**Decision points**
- policy_approval
- delegation_grant
- revocation_decision

- **Accountable entity**: governance_authority

**Evidence produced**
- policy_document
- delegation_record
- status_record

## Notes
- The practical significance of an authority depends on the scope in which its decisions are recognized, how that scope is established, and whether that recognition can be delegated, constrained, contested, or revoked.

## Supporting Definitions
Not specified

## Mental Models
Not specified

## See Also
- policy
- governance-framework
- requirement
- delegation
- delegator
- delegatee

## Crosswalk References
- **NIST**: PM-1
- **ISO**: ISO/IEC 42001 5.3
