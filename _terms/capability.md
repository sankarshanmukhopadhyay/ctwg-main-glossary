---
title: "capability"
---

# capability

A simple-English summary has not yet been added for this concept.

## Formal definition
The ability or permission for an actor or agent to perform a specific action on behalf of a party within a defined scope and subject to applicable constraints.

## Why this concept matters
This concept is provided as a controlled glossary entry for standards, governance, and implementation review.

Use this concept consistently when mapping authority, evidence, reliance, and auditability across governance and implementation artifacts.

## Names and relationships

### Alternative designations
- **capabilities** (`en`, `alternative`)

### Related concepts
- [delegation]({{ '/terms/delegation/' | relative_url }})
- [delegator]({{ '/terms/delegator/' | relative_url }})
- [delegatee]({{ '/terms/delegatee/' | relative_url }})
- [authorization]({{ '/terms/authorization/' | relative_url }})
- [permission]({{ '/terms/permission/' | relative_url }})

### Semantic relations
- **related**: `urn:tig:concept:delegation`
- **related**: `urn:tig:concept:delegator`
- **related**: `urn:tig:concept:delegatee`
- **related**: `urn:tig:concept:authorization`
- **related**: `urn:tig:concept:permission`

### Cross-vocabulary mappings
Not specified

## Provenance and identity
- **Concept ID**: `urn:tig:concept:capability`
- **Editorial status**: `stable`
- **Provenance classification**: `adapted`
- **Source corpus**: Trust over IP Main Glossary

### Standards and source references
- ToIP CTWG maintained glossary source: `spec/terms-definitions/capability.md`

<details markdown="1">
<summary><strong>Implementation and governance metadata</strong></summary>

### Legacy aliases
capability, capabilities

### Governance profile
- **Authority scope**: delegation_and_scope, access_decisioning
- **Delegation mode**: direct_or_constrained
- **Revocation supported**: True
- **Lifecycle states**: proposed, active, suspended, revoked, retired
- **Execution role**: runtime
- **Control-plane role**: decision_plane_component

### Enforcement points
- delegation_grant
- access_decision
- revocation_decision

### Assurance
**Evidence artifacts**
- delegation_record
- access_decision_log
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
- access_decision
- revocation_decision

- **Accountable entity**: glossary_maintainers

**Evidence produced**
- delegation_record
- access_decision_log
- policy_document
- status_record
- audit_log
- verification_log
- registry_entry

### Notes
Not specified

### Supporting definitions
Not specified

### Mental models
Not specified

### Crosswalk references
Not specified

</details>

---

*Generated from `glossary/terms/capability.yaml`. Edit the source concept and regenerate rather than editing this page directly.*
