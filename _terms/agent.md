---
title: "agent"
---

# agent

A person or software component that acts for someone or something else within a defined scope.

## Formal definition
An actor that executes an action on behalf of a party (called the principal of that actor). In the context of decentralized digital trust infrastructure, the term “agent” is most frequently used to mean a digital agent.

## Why this concept matters
This concept is provided as a controlled glossary entry for standards, governance, and implementation review.

Use this concept consistently when mapping authority, evidence, reliance, and auditability across governance and implementation artifacts.

## Names and relationships

### Alternative designations
- **agents** (`en`, `alternative`)

### Related concepts
- [wallet]({{ '/terms/wallet/' | relative_url }})

### Semantic relations
- **related**: `urn:tig:concept:wallet`

### Cross-vocabulary mappings
Not specified

## Provenance and identity
- **Concept ID**: `urn:tig:concept:agent`
- **Editorial status**: `stable`
- **Provenance classification**: `locally_defined`
- **Source corpus**: Trust Infrastructure Glossary

### Standards and source references
- [eSSIF-Lab](https://essif-lab.github.io/framework/docs/essifLab-glossary#agent).

<details markdown="1">
<summary><strong>Implementation and governance metadata</strong></summary>

### Legacy aliases
agent, agents

### Governance profile
- **Authority scope**: delegation_and_scope, governance_recognition
- **Delegation mode**: direct_or_constrained
- **Revocation supported**: True
- **Lifecycle states**: proposed, active, suspended, revoked, retired
- **Execution role**: runtime
- **Control-plane role**: decision_plane_component

### Enforcement points
- delegation_grant
- revocation_decision

### Assurance
**Evidence artifacts**
- delegation_record
- policy_document
- status_record
- audit_log
- verification_log
- registry_entry

- **Assurance level hint**: AL2+
- **Auditability**: high

### Control plane
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

### Notes
- The governance significance of an agent depends on what authority it exercises, under what policies it operates, and what controls exist for oversight, limitation, and revocation.
- In a ToIP context, an agent is frequently assumed to have privileged access to the wallet(s) of its principal. In market parlance, a mobile app performing the actions of an agent is often simply called a wallet or a digital wallet.

### Supporting definitions
Not specified

### Mental models
Not specified

### Crosswalk references
Not specified

</details>

---

*Generated from `glossary/terms/agent.yaml`. Edit the source concept and regenerate rather than editing this page directly.*
