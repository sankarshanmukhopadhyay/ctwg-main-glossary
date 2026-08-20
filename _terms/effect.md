---
title: "effect"
---

# effect

The real-world or system consequence that follows from a governed decision or action.

## Formal definition
A material state change, permission, restriction, publication, transaction, invocation, or other externally meaningful consequence produced or authorized by a decision or governed action.

## Why this concept matters
This concept is provided as a controlled glossary entry for standards, governance, and implementation review.

Use this concept consistently when mapping authority, evidence, reliance, and auditability across governance and implementation artifacts.

## Names and relationships

### Alternative designations
None

### Related concepts
- [action]({{ '/terms/action/' | relative_url }})
- [authorization]({{ '/terms/authorization/' | relative_url }})
- [decision]({{ '/terms/decision/' | relative_url }})
- [policy]({{ '/terms/policy/' | relative_url }})

### Semantic relations
- **related**: `urn:tig:concept:action`
- **related**: `urn:tig:concept:authorization`
- **related**: `urn:tig:concept:decision`
- **related**: `urn:tig:concept:policy`

### Cross-vocabulary mappings
Not specified

## Provenance and identity
- **Concept ID**: `urn:tig:concept:effect`
- **Editorial status**: `proposed`
- **Provenance classification**: `locally_defined`
- **Source corpus**: Cross-repository trust infrastructure portfolio

### Standards and source references
- https://github.com/sankarshanmukhopadhyay/trust-systems-meta-model
- https://github.com/sankarshanmukhopadhyay/governance-authority-assurance-metamodel
- https://github.com/sankarshanmukhopadhyay/open-national-digital-trust-framework

<details markdown="1">
<summary><strong>Implementation and governance metadata</strong></summary>

### Legacy aliases
effect

### Governance profile
- **Authority scope**: access_decisioning, governance_recognition
- **Delegation mode**: direct_or_constrained
- **Revocation supported**: True
- **Lifecycle states**: proposed, active, revoked, retired
- **Execution role**: runtime
- **Control-plane role**: decision_plane_component

### Enforcement points
- access_decision
- reliance_decision

### Assurance
**Evidence artifacts**
- access_decision_log
- audit_log

- **Assurance level hint**: AL2+
- **Auditability**: high

### Control plane
**Decision points**
- access_decision
- reliance_decision

- **Accountable entity**: effect_authority

**Evidence produced**
- access_decision_log
- audit_log

### Notes
- An effect is distinct from a decision: a decision may authorize or require an effect, while execution determines whether that effect actually occurs.

### Supporting definitions
Not specified

### Mental models
Not specified

### Crosswalk references
Not specified

</details>

---

*Generated from `glossary/terms/effect.yaml`. Edit the source concept and regenerate rather than editing this page directly.*
