---
title: "authority"
---

# authority

The recognized right or power to make a decision, grant permission, impose a rule, or act within a defined scope.

## Formal definition
A party whose decisions, policies, rules, or recognition outcomes are accepted as governing, directive, or controlling by other parties within a defined scope.

## Why this concept matters
This concept is provided as a controlled glossary entry for standards, governance, and implementation review.

Use this concept consistently when mapping authority, evidence, reliance, and auditability across governance and implementation artifacts.

## Names and relationships

### Alternative designations
- **authorities** (`en`, `alternative`)

### Related concepts
- [policy]({{ '/terms/policy/' | relative_url }})
- [governance-framework]({{ '/terms/governance-framework/' | relative_url }})
- [requirement]({{ '/terms/requirement/' | relative_url }})
- [delegation]({{ '/terms/delegation/' | relative_url }})
- [delegator]({{ '/terms/delegator/' | relative_url }})
- [delegatee]({{ '/terms/delegatee/' | relative_url }})

### Semantic relations
- **related**: `urn:tig:concept:policy`
- **related**: `urn:tig:concept:governance-framework`
- **related**: `urn:tig:concept:requirement`
- **related**: `urn:tig:concept:delegation`
- **related**: `urn:tig:concept:delegator`
- **related**: `urn:tig:concept:delegatee`

### Cross-vocabulary mappings
Not specified

## Provenance and identity
- **Concept ID**: `urn:tig:concept:authority`
- **Editorial status**: `stable`
- **Provenance classification**: `locally_defined`
- **Source corpus**: Trust Infrastructure Glossary

### Standards and source references
- [eSSIF-Lab](https://essif-lab.github.io/framework/docs/terms/authority).

<details markdown="1">
<summary><strong>Implementation and governance metadata</strong></summary>

### Legacy aliases
authority, authorities

### Governance profile
- **Authority scope**: policy_definition, delegation_and_scope, governance_recognition
- **Delegation mode**: direct_or_constrained
- **Revocation supported**: True
- **Lifecycle states**: proposed, active, suspended, revoked, retired
- **Execution role**: runtime
- **Control-plane role**: decision_plane_component

### Enforcement points
- policy_approval
- delegation_grant
- revocation_decision

### Assurance
**Evidence artifacts**
- policy_document
- delegation_record
- status_record

- **Assurance level hint**: AL2+
- **Auditability**: high

### Control plane
**Decision points**
- policy_approval
- delegation_grant
- revocation_decision

- **Accountable entity**: governance_authority

**Evidence produced**
- policy_document
- delegation_record
- status_record

### Notes
- The practical significance of an authority depends on the scope in which its decisions are recognized, how that scope is established, and whether that recognition can be delegated, constrained, contested, or revoked.

### Supporting definitions
Not specified

### Mental models
Not specified

### Crosswalk references
- **NIST**: PM-1
- **ISO**: ISO/IEC 42001 5.3

</details>

---

*Generated from `glossary/terms/authority.yaml`. Edit the source concept and regenerate rather than editing this page directly.*
