---
title: "dcql"
---

# dcql

A query language defined by OpenID4VP for requesting credential presentations in a flexible and credential-format-aware way.

## Formal definition
A query language defined by OpenID4VP for requesting credential presentations in a flexible and credential-format-aware way.

## Why this concept matters
This concept is provided as a controlled glossary entry for standards, governance, and implementation review.

Use this concept consistently when mapping authority, evidence, reliance, and auditability across governance and implementation artifacts.

## Names and relationships

### Alternative designations
- **Digital Credentials Query Language** (`en`, `alternative`)
- **DCQL** (`en`, `alternative`)

### Related concepts
- [openid4vp]({{ '/terms/openid4vp/' | relative_url }})
- [presentation-request]({{ '/terms/presentation-request/' | relative_url }})
- [verifiable-presentation]({{ '/terms/verifiable-presentation/' | relative_url }})
- [credential]({{ '/terms/credential/' | relative_url }})

### Semantic relations
- **related**: `urn:tig:concept:openid4vp`
- **related**: `urn:tig:concept:presentation-request`
- **related**: `urn:tig:concept:verifiable-presentation`
- **related**: `urn:tig:concept:credential`

### Cross-vocabulary mappings
Not specified

## Provenance and identity
- **Concept ID**: `urn:tig:concept:dcql`
- **Editorial status**: `stable`
- **Provenance classification**: `locally_defined`
- **Source corpus**: Trust Infrastructure Glossary

### Standards and source references
- [OpenID for Verifiable Presentations 1.0](https://openid.net/specs/openid-4-verifiable-presentations-1_0.html) (OpenID Foundation; Final Specification; 1.0; 2025-07-09) — normative

<details markdown="1">
<summary><strong>Implementation and governance metadata</strong></summary>

### Legacy aliases
Digital Credentials Query Language, DCQL

### Governance profile
- **Authority scope**: verification_and_reliance, policy_definition
- **Delegation mode**: direct
- **Revocation supported**: False
- **Lifecycle states**: proposed, active, retired
- **Execution role**: hybrid
- **Control-plane role**: decision_plane_component

### Enforcement points
- reliance_decision
- policy_approval

### Assurance
**Evidence artifacts**
- policy_document
- verification_log
- audit_log

- **Assurance level hint**: AL2+
- **Auditability**: high

### Control plane
**Decision points**
- reliance_decision
- policy_approval

- **Accountable entity**: glossary_maintainers

**Evidence produced**
- policy_document
- verification_log
- audit_log

### Notes
Not specified

### Supporting definitions
Not specified

### Mental models
Not specified

### Crosswalk references
- **OPENID**: OpenID4VP 1.0

</details>

---

*Generated from `glossary/terms/dcql.yaml`. Edit the source concept and regenerate rather than editing this page directly.*
