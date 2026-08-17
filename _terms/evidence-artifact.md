---
title: "evidence artifact"
---

# evidence artifact

A simple-English summary has not yet been added for this concept.

## Formal definition
A typed, structured output produced by a system, authorized actor, or assessment process to demonstrate that a rule was checked, a behavior occurred, or a condition holds.

## Why this concept matters
This term was added following a cross-repository terminology review of TSMM, TIS, TGA, and the DTG ZKP Task Force workspace.

Use this term to keep runtime governance, delegation, evidence, and privacy semantics consistent across interoperating trust infrastructure repositories.

## Names and relationships

### Alternative designations
- **evidence-artifact** (`en`, `alternative`)

### Related concepts
- [attestation]({{ '/terms/attestation/' | relative_url }})
- [controlled-document]({{ '/terms/controlled-document/' | relative_url }})
- [audit-log]({{ '/terms/audit-log/' | relative_url }})

### Semantic relations
- **related**: `urn:tig:concept:attestation`
- **related**: `urn:tig:concept:controlled-document`
- **related**: `urn:tig:concept:audit-log`

### Cross-vocabulary mappings
Not specified

## Provenance and identity
- **Concept ID**: `urn:tig:concept:evidence-artifact`
- **Editorial status**: `stable`
- **Provenance classification**: `locally_defined`
- **Source corpus**: Trust Infrastructure Glossary

### Standards and source references
- [TSMM repository terminology and model documentation](https://github.com/sankarshanmukhopadhyay/trust-systems-meta-model) (GitHub) — informative

<details markdown="1">
<summary><strong>Implementation and governance metadata</strong></summary>

### Legacy aliases
evidence artifact, evidence-artifact

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

*Generated from `glossary/terms/evidence-artifact.yaml`. Edit the source concept and regenerate rather than editing this page directly.*
