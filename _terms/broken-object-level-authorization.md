---
title: "broken-object-level-authorization"
---

# broken-object-level-authorization

Refers to security flaws where users can access data they shouldn't, due to inadequate permission checks on individual (sub)objects.

## Formal definition
Refers to security flaws where users can access data they shouldn't, due to inadequate permission checks on individual (sub)objects.

## Why this concept matters
This concept is provided as a controlled glossary entry for standards, governance, and implementation review.

Use this concept consistently when mapping authority, evidence, reliance, and auditability across governance and implementation artifacts.

## Names and relationships

### Alternative designations
- **broken object level authorization** (`en`, `alternative`)

### Related concepts
- [authorization]({{ '/terms/authorization/' | relative_url }})
- [permission]({{ '/terms/permission/' | relative_url }})
- [role-based-access-control]({{ '/terms/role-based-access-control/' | relative_url }})
- [attribute-based-access-control]({{ '/terms/attribute-based-access-control/' | relative_url }})

### Semantic relations
- **related**: `urn:tig:concept:authorization`
- **related**: `urn:tig:concept:permission`
- **related**: `urn:tig:concept:role-based-access-control`
- **related**: `urn:tig:concept:attribute-based-access-control`

### Cross-vocabulary mappings
Not specified

## Provenance and identity
- **Concept ID**: `urn:tig:concept:broken-object-level-authorization`
- **Editorial status**: `stable`
- **Provenance classification**: `adapted`
- **Source corpus**: Trust over IP Main Glossary

### Standards and source references
- ToIP CTWG maintained glossary source: `spec/terms-definitions/broken-object-level-authorization.md`

<details markdown="1">
<summary><strong>Implementation and governance metadata</strong></summary>

### Legacy aliases
broken-object-level-authorization, broken object level authorization

### Governance profile
- **Authority scope**: access_decisioning
- **Delegation mode**: direct
- **Revocation supported**: True
- **Lifecycle states**: proposed, active, suspended, revoked, retired
- **Execution role**: runtime
- **Control-plane role**: decision_plane_component

### Enforcement points
- access_decision
- revocation_decision

### Assurance
**Evidence artifacts**
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
- access_decision
- revocation_decision

- **Accountable entity**: glossary_maintainers

**Evidence produced**
- access_decision_log
- policy_document
- status_record
- audit_log
- verification_log
- registry_entry

### Notes
Not specified

### Supporting definitions
- Also known as [[ref: BOLA]]

### Mental models
Not specified

### Crosswalk references
Not specified

</details>

---

*Generated from `glossary/terms/broken-object-level-authorization.yaml`. Edit the source concept and regenerate rather than editing this page directly.*
