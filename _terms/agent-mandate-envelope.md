---
title: "agent mandate envelope"
---

# agent mandate envelope

A structured artifact that binds an agent to an originating principal, delegated mandate, permitted scope, conditions, expiry, revocation semantics, and evidence requirements.

## Formal definition
A structured artifact that binds an agent to an originating principal, delegated mandate, permitted scope, conditions, expiry, revocation semantics, and evidence requirements.

## Why this concept matters
This term was added following a cross-repository terminology review of TSMM, TIS, TGA, and the DTG ZKP Task Force workspace.

Use this term to keep runtime governance, delegation, evidence, and privacy semantics consistent across interoperating trust infrastructure repositories.

## Names and relationships

### Alternative designations
- **agent-mandate-envelope** (`en`, `alternative`)

### Related concepts
- [agent]({{ '/terms/agent/' | relative_url }})
- [authority]({{ '/terms/authority/' | relative_url }})

### Semantic relations
- **related**: `urn:tig:concept:agent`
- **related**: `urn:tig:concept:authority`

### Cross-vocabulary mappings
Not specified

## Provenance and identity
- **Concept ID**: `urn:tig:concept:agent-mandate-envelope`
- **Editorial status**: `stable`
- **Provenance classification**: `locally_defined`
- **Source corpus**: Trust Infrastructure Glossary

### Standards and source references
- [TGA repository terminology and model documentation](https://github.com/sankarshanmukhopadhyay/trust-graph-artifacts) (GitHub) — informative

<details markdown="1">
<summary><strong>Implementation and governance metadata</strong></summary>

### Legacy aliases
agent mandate envelope, agent-mandate-envelope

### Governance profile
- **Authority scope**: assurance_and_audit, delegation_and_scope, policy_definition, verification_and_reliance
- **Delegation mode**: direct_or_constrained
- **Revocation supported**: True
- **Lifecycle states**: proposed, active, suspended, revoked, retired
- **Execution role**: hybrid
- **Control-plane role**: decision_plane_component

### Enforcement points
- policy_approval
- delegation_grant
- reliance_decision
- revocation_decision

### Assurance
**Evidence artifacts**
- policy_document
- delegation_record
- status_record
- verification_log

- **Assurance level hint**: AL2+
- **Auditability**: high

### Control plane
**Decision points**
- policy_approval
- delegation_grant
- reliance_decision
- revocation_decision

- **Accountable entity**: governance_authority

**Evidence produced**
- policy_document
- delegation_record
- status_record
- verification_log

### Notes
- This definition is normalized for cross-repository use and should be applied together with the governing profile or specification that supplies domain-specific constraints.

### Supporting definitions
Not specified

### Mental models
Not specified

### Crosswalk references
Not specified

</details>

---

*Generated from `glossary/terms/agent-mandate-envelope.yaml`. Edit the source concept and regenerate rather than editing this page directly.*
