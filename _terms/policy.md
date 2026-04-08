---
title: "policy"
---

# policy

## Definition
Statements, rules, or assertions that specify required, permitted, prohibited, or expected behavior of an entity within a defined scope. Policies may be human-readable, machine-readable, or both, and may be interpreted, enforced, or audited by people, software, or both.

## Aliases
policy, policies

## Governance Profile
- **Authority scope**: policy_definition, assurance_and_audit
- **Delegation mode**: direct
- **Revocation supported**: True
- **Lifecycle states**: proposed, active, suspended, revoked, retired
- **Execution role**: runtime
- **Control-plane role**: decision_plane_component

## Enforcement Points
- policy_approval
- revocation_decision

## Assurance
**Evidence artifacts**
- policy_document
- audit_log

- **Assurance level hint**: AL2+
- **Auditability**: high

## Control Plane
**Decision points**
- policy_approval
- revocation_decision

- **Accountable entity**: auditor

**Evidence produced**
- policy_document
- audit_log

## Notes
Not specified

## Supporting Definitions
- Example: An [[ref: authorization]] policy might specify the [[ref: access control]] rules applied by a software component at runtime.

## Mental Models
Not specified

## See Also
- governance framework
- governance requirement
- rule.

## Crosswalk References
- **NIST**: PL-1
- **ISO**: ISO/IEC 42001 5.2
