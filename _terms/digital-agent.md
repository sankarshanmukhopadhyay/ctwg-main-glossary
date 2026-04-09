---
title: "digital-agent"
---

> Generated file. Update `glossary/terms/digital-agent.yaml` and regenerate artifacts instead of editing this page directly.

# digital-agent

## Definition
In the context of ​​decentralized digital trust infrastructure, a software agent that operates in conjunction with a digital wallet or similar system component to take actions on behalf of its controller.

## Aliases
digital agent, digital agents

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

- **Assurance level hint**: AL2+
- **Auditability**: high

## Control Plane
**Decision points**
- delegation_grant
- revocation_decision

- **Accountable entity**: governance_authority

**Evidence produced**
- delegation_record

## Notes
- A digital agent may act with significant operational authority. Its governance characteristics therefore depend on the policies, permissions, lifecycle controls, and revocation mechanisms under which it operates.
- In a ToIP context, a digital agent is frequently assumed to have privileged access to the digital wallets of its principal. In market parlance, a mobile app that performs the actions of a digital agent is often simply called a wallet or a digital wallet.

## Supporting Definitions
Not specified

## Mental Models
Not specified

## See Also
Not specified

## Crosswalk References
Not specified
