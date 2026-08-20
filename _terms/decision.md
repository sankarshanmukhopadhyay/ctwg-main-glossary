---
title: "decision"
---

# decision

A governed determination that chooses what should happen next or what state should apply.

## Formal definition
An attributable determination by an authorized actor or mechanism that selects an outcome, state transition, permission, denial, requirement, or other governed effect under applicable policy and evidence.

## Why this concept matters
This concept is provided as a controlled glossary entry for standards, governance, and implementation review.

Use this concept consistently when mapping authority, evidence, reliance, and auditability across governance and implementation artifacts.

## Names and relationships

### Alternative designations
None

### Related concepts
- [authority]({{ '/terms/authority/' | relative_url }})
- [policy]({{ '/terms/policy/' | relative_url }})
- [action]({{ '/terms/action/' | relative_url }})
- [risk-decision]({{ '/terms/risk-decision/' | relative_url }})

### Semantic relations
- **related**: `urn:tig:concept:authority`
- **related**: `urn:tig:concept:policy`
- **related**: `urn:tig:concept:action`

### Cross-vocabulary mappings
Not specified

## Provenance and identity
- **Concept ID**: `urn:tig:concept:decision`
- **Editorial status**: `proposed`
- **Provenance classification**: `locally_defined`
- **Source corpus**: Cross-repository trust infrastructure portfolio

### Standards and source references
- https://github.com/sankarshanmukhopadhyay/trust-systems-meta-model
- https://github.com/sankarshanmukhopadhyay/trust-infrastructure-schemas
- https://github.com/sankarshanmukhopadhyay/PolicyMesh
- https://github.com/sankarshanmukhopadhyay/open-national-digital-trust-framework

<details markdown="1">
<summary><strong>Implementation and governance metadata</strong></summary>

### Legacy aliases
decision

### Governance profile
- **Authority scope**: access_decisioning, governance_recognition, verification_and_reliance
- **Delegation mode**: direct_or_constrained
- **Revocation supported**: True
- **Lifecycle states**: proposed, active, revoked, retired
- **Execution role**: runtime
- **Control-plane role**: decision_plane_component

### Enforcement points
- access_decision
- reliance_decision
- policy_approval

### Assurance
**Evidence artifacts**
- audit_log
- verification_log
- policy_document

- **Assurance level hint**: AL2+
- **Auditability**: high

### Control plane
**Decision points**
- access_decision
- reliance_decision
- policy_approval

- **Accountable entity**: decision_authority

**Evidence produced**
- audit_log
- verification_log
- policy_document

### Notes
- A decision should be distinguishable from the evidence considered and from the downstream effect produced by acting on the decision.

### Supporting definitions
Not specified

### Mental models
Not specified

### Crosswalk references
Not specified

</details>

---

*Generated from `glossary/terms/decision.yaml`. Edit the source concept and regenerate rather than editing this page directly.*
