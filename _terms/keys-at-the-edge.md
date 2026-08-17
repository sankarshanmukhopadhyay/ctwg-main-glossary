---
title: "keys-at-the-edge"
---

# keys-at-the-edge

A simple-English summary has not yet been added for this concept.

## Formal definition
A key management architecture in which keys are stored on a user’s local edge devices, such as a smartphone, tablet, or laptop, and then used in conjunction with a secure protocol to unlock a key management system (KMS) and/or a digital vault in the cloud. This approach can enable the storage and sharing of large data structures that are not feasible on edge devices. This architecture can also be used in conjunction with confidential computing to enable cloud-based digital agents to safely carry out “user not present” operations.

## Why this concept matters
This concept is provided as a controlled glossary entry for standards, governance, and implementation review.

Use this concept consistently when mapping authority, evidence, reliance, and auditability across governance and implementation artifacts.

## Names and relationships

### Alternative designations
None

### Related concepts
- [delegation]({{ '/terms/delegation/' | relative_url }})
- [delegator]({{ '/terms/delegator/' | relative_url }})
- [delegatee]({{ '/terms/delegatee/' | relative_url }})
- [authorization]({{ '/terms/authorization/' | relative_url }})

### Semantic relations
- **related**: `urn:tig:concept:delegation`
- **related**: `urn:tig:concept:delegator`
- **related**: `urn:tig:concept:delegatee`
- **related**: `urn:tig:concept:authorization`

### Cross-vocabulary mappings
Not specified

## Provenance and identity
- **Concept ID**: `urn:tig:concept:keys-at-the-edge`
- **Editorial status**: `stable`
- **Provenance classification**: `adapted`
- **Source corpus**: Trust over IP Main Glossary

### Standards and source references
- ToIP CTWG maintained glossary source: `spec/terms-definitions/keys-at-the-edge.md`

<details markdown="1">
<summary><strong>Implementation and governance metadata</strong></summary>

### Legacy aliases
keys-at-the-edge

### Governance profile
- **Authority scope**: delegation_and_scope
- **Delegation mode**: direct_or_constrained
- **Revocation supported**: False
- **Lifecycle states**: documented, active, deprecated
- **Execution role**: runtime
- **Control-plane role**: decision_plane_component

### Enforcement points
- delegation_grant

### Assurance
**Evidence artifacts**
- delegation_record

- **Assurance level hint**: AL2+
- **Auditability**: high

### Control plane
**Decision points**
- delegation_grant

- **Accountable entity**: glossary_maintainers

**Evidence produced**
- delegation_record

### Notes
Not specified

### Supporting definitions
- Also known as: [[ref: KATE]].

### Mental models
Not specified

### Crosswalk references
Not specified

</details>

---

*Generated from `glossary/terms/keys-at-the-edge.yaml`. Edit the source concept and regenerate rather than editing this page directly.*
