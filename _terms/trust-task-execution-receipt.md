---
title: "trust task execution receipt"
---

# trust task execution receipt

A structured receipt that records how a trust-relevant task was authorized, executed, evidenced, and completed or terminated.

## Formal definition
A structured receipt that records how a trust-relevant task was authorized, executed, evidenced, and completed or terminated.

## Why this concept matters
This term was added following a cross-repository terminology review of TSMM, TIS, TGA, and the DTG ZKP Task Force workspace.

Use this term to keep runtime governance, delegation, evidence, and privacy semantics consistent across interoperating trust infrastructure repositories.

## Names and relationships

### Alternative designations
- **trust-task-execution-receipt** (`en`, `alternative`)

### Related concepts
- [trust-task]({{ '/terms/trust-task/' | relative_url }})
- [authority]({{ '/terms/authority/' | relative_url }})
- [policy]({{ '/terms/policy/' | relative_url }})

### Semantic relations
- **related**: `urn:tig:concept:trust-task`
- **related**: `urn:tig:concept:authority`
- **related**: `urn:tig:concept:policy`

### Cross-vocabulary mappings
Not specified

## Provenance and identity
- **Concept ID**: `urn:tig:concept:trust-task-execution-receipt`
- **Editorial status**: `stable`
- **Provenance classification**: `locally_defined`
- **Source corpus**: Trust Infrastructure Glossary

### Standards and source references
- [TIS repository terminology and model documentation](https://github.com/sankarshanmukhopadhyay/trust-infrastructure-schemas) (GitHub) — informative

<details markdown="1">
<summary><strong>Implementation and governance metadata</strong></summary>

### Legacy aliases
trust task execution receipt, trust-task-execution-receipt

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

*Generated from `glossary/terms/trust-task-execution-receipt.yaml`. Edit the source concept and regenerate rather than editing this page directly.*
