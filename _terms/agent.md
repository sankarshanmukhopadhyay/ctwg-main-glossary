---
title: "agent"
---

> Generated file. Update `glossary/terms/agent.yaml` and regenerate artifacts instead of editing this page directly.

# agent

## Definition
An actor that executes an action on behalf of a party (called the principal of that actor). In the context of decentralized digital trust infrastructure, the term “agent” is most frequently used to mean a digital agent.

## Aliases
agent, agents

## Governance Profile
- **Authority scope**: delegation_and_scope, governance_recognition
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

- **Accountable entity**: governance_authority

**Evidence produced**
- delegation_record
- policy_document
- status_record
- audit_log
- verification_log
- registry_entry

## Notes
- The governance significance of an agent depends on what authority it exercises, under what policies it operates, and what controls exist for oversight, limitation, and revocation.
- In a ToIP context, an agent is frequently assumed to have privileged access to the wallet(s) of its principal. In market parlance, a mobile app performing the actions of an agent is often simply called a wallet or a digital wallet.

## Supporting Definitions
Not specified

## Mental Models
Not specified

## See Also
- wallet.

## Crosswalk References
Not specified
