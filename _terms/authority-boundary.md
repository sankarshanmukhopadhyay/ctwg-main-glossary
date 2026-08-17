---
title: "authority boundary"
---

# authority boundary

A machine- or human-readable constraint that identifies where authority begins and ends, including the permitted actor, scope, action, target, conditions, and lifecycle state.

## Formal definition
A machine- or human-readable constraint that identifies where authority begins and ends, including the permitted actor, scope, action, target, conditions, and lifecycle state.

## Why this concept matters
This term was added following a cross-repository terminology review of TSMM, TIS, TGA, and the DTG ZKP Task Force workspace.

Use this term to keep runtime governance, delegation, evidence, and privacy semantics consistent across interoperating trust infrastructure repositories.

## Names and relationships

### Alternative designations
- **authority-boundary** (`en`, `alternative`)

### Related concepts
- [authority]({{ '/terms/authority/' | relative_url }})
- [scope]({{ '/terms/scope/' | relative_url }})
- [trust-boundary]({{ '/terms/trust-boundary/' | relative_url }})

### Semantic relations
- **related**: `urn:tig:concept:authority`
- **related**: `urn:tig:concept:scope`
- **related**: `urn:tig:concept:trust-boundary`

### Cross-vocabulary mappings
Not specified

## Provenance and identity
- **Concept ID**: `urn:tig:concept:authority-boundary`
- **Editorial status**: `stable`
- **Provenance classification**: `locally_defined`
- **Source corpus**: Trust Infrastructure Glossary

### Standards and source references
- [TIS repository terminology and model documentation](https://github.com/sankarshanmukhopadhyay/trust-infrastructure-schemas) (GitHub) — informative
- [TGA repository terminology and model documentation](https://github.com/sankarshanmukhopadhyay/trust-graph-artifacts) (GitHub) — informative

<details markdown="1">
<summary><strong>Implementation and governance metadata</strong></summary>

### Legacy aliases
authority boundary, authority-boundary

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

*Generated from `glossary/terms/authority-boundary.yaml`. Edit the source concept and regenerate rather than editing this page directly.*
