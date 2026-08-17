---
title: "delegator"
---

# delegator

The first party that makes a delegation to a second party (the delegatee) and remains accountable for granting authority within the permitted scope.

## Formal definition
The first party that makes a delegation to a second party (the delegatee) and remains accountable for granting authority within the permitted scope.

## Why this concept matters
This concept is provided as a controlled glossary entry for standards, governance, and implementation review.

Use this concept consistently when mapping authority, evidence, reliance, and auditability across governance and implementation artifacts.

## Names and relationships

### Alternative designations
- **delegators** (`en`, `alternative`)

### Related concepts
- [delegation]({{ '/terms/delegation/' | relative_url }})
- [delegatee]({{ '/terms/delegatee/' | relative_url }})
- [authorization]({{ '/terms/authorization/' | relative_url }})
- [governance]({{ '/terms/governance/' | relative_url }})
- [governance-framework]({{ '/terms/governance-framework/' | relative_url }})
- [governing-authority]({{ '/terms/governing-authority/' | relative_url }})

### Semantic relations
- **related**: `urn:tig:concept:delegation`
- **related**: `urn:tig:concept:delegatee`
- **related**: `urn:tig:concept:authorization`
- **related**: `urn:tig:concept:governance`
- **related**: `urn:tig:concept:governance-framework`
- **related**: `urn:tig:concept:governing-authority`

### Cross-vocabulary mappings
Not specified

## Provenance and identity
- **Concept ID**: `urn:tig:concept:delegator`
- **Editorial status**: `stable`
- **Provenance classification**: `adapted`
- **Source corpus**: Trust over IP Main Glossary

### Standards and source references
- ToIP CTWG maintained glossary source: `spec/terms-definitions/delegator.md`

<details markdown="1">
<summary><strong>Implementation and governance metadata</strong></summary>

### Legacy aliases
delegator, delegators

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
Not specified

### Supporting definitions
- [eSSIF-Lab](https://essif-lab.github.io/framework/docs/essifLab): the transferral of [ownership](https://essif-lab.github.io/framework/docs/terms/ownership) of one or more obligation of a [party](https://essif-lab.github.io/framework/docs/terms/party) (the [delegator](https://essif-lab.github.io/framework/docs/terms/delegate)), including the associated accountability, to another party (the [delegatee](https://essif-lab.github.io/framework/docs/terms/delegate)), which implies that the delegatee can realize such obligation as it sees fit.

### Mental models
Not specified

### Crosswalk references
Not specified

</details>

---

*Generated from `glossary/terms/delegator.yaml`. Edit the source concept and regenerate rather than editing this page directly.*
