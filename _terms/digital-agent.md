---
title: "digital-agent"
---

> Generated file. Update `glossary/terms/digital-agent.yaml` and regenerate artifacts instead of editing this page directly.

# digital-agent

## In Simple English
A simple-English summary has not yet been added for this term.

## Definition
In the context of ​​decentralized digital trust infrastructure, a software agent that operates in conjunction with a digital wallet or similar system component to take actions on behalf of its controller.

## Reader Note
This term is provided as a controlled glossary entry for standards, governance, and implementation review.

## Implementation Relevance
Use this term consistently when mapping authority, evidence, reliance, and auditability across governance and implementation artifacts.

## Aliases
digital agent, digital agents

## See Also
- [delegation]({{ '/terms/delegation/' | relative_url }})
- [delegator]({{ '/terms/delegator/' | relative_url }})
- [delegatee]({{ '/terms/delegatee/' | relative_url }})
- [authorization]({{ '/terms/authorization/' | relative_url }})
- [governance]({{ '/terms/governance/' | relative_url }})
- [governance-framework]({{ '/terms/governance-framework/' | relative_url }})

## Standards and Source References
- ToIP CTWG maintained glossary source: `spec/terms-definitions/digital-agent.md`

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
- A digital agent may act with significant operational authority. Its governance characteristics therefore depend on the policies, permissions, lifecycle controls, and revocation mechanisms under which it operates.
- In a ToIP context, a digital agent is frequently assumed to have privileged access to the digital wallets of its principal. In market parlance, a mobile app that performs the actions of a digital agent is often simply called a wallet or a digital wallet.

## Supporting Definitions
Not specified

## Mental Models
Not specified

## Crosswalk References
Not specified
