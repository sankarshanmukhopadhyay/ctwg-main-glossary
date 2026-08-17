---
title: "delegation"
---

# delegation

A simple-English summary has not yet been added for this concept.

## Formal definition
The act of a first party (the delegator) authorizing a second party (the delegatee) to perform a defined set of actions on behalf of the first party within an authorized scope and subject to applicable constraints.

## Why this concept matters
This concept is provided as a controlled glossary entry for standards, governance, and implementation review.

Use this concept consistently when mapping authority, evidence, reliance, and auditability across governance and implementation artifacts.

## Names and relationships

### Alternative designations
- **delegate** (`en`, `alternative`)
- **delegated** (`en`, `alternative`)
- **delegates** (`en`, `alternative`)

### Related concepts
- [delegator]({{ '/terms/delegator/' | relative_url }})
- [delegatee]({{ '/terms/delegatee/' | relative_url }})
- [authorization]({{ '/terms/authorization/' | relative_url }})
- [revocation]({{ '/terms/revocation/' | relative_url }})

### Semantic relations
- **related**: `urn:tig:concept:delegator`
- **related**: `urn:tig:concept:delegatee`
- **related**: `urn:tig:concept:authorization`
- **related**: `urn:tig:concept:revocation`

### Cross-vocabulary mappings
Not specified

## Provenance and identity
- **Concept ID**: `urn:tig:concept:delegation`
- **Editorial status**: `stable`
- **Provenance classification**: `adapted`
- **Source corpus**: Trust over IP Main Glossary

### Standards and source references
- ToIP CTWG maintained glossary source: `spec/terms-definitions/delegation.md`

<details markdown="1">
<summary><strong>Implementation and governance metadata</strong></summary>

### Legacy aliases
delegation, delegate, delegated, delegates

### Governance profile
- **Authority scope**: delegation_and_scope
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

- **Accountable entity**: glossary_maintainers

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
- Delegation may be expressed through a [[ref: delegation credential]] or other policy-governed mechanism and may be limited by scope, time, conditions, or revocation.
- More specific for KERI see: [[xref: keri1, delegated-identifier]]

### Mental models
Not specified

### Crosswalk references
- **NIST**: AC-6
- **ISO**: ISO/IEC 42001 8.3

</details>

---

*Generated from `glossary/terms/delegation.yaml`. Edit the source concept and regenerate rather than editing this page directly.*
