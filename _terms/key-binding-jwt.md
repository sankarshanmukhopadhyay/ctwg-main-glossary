---
title: "key-binding-jwt"
---

# key-binding-jwt

A JWT used to demonstrate holder control of a key associated with an SD-JWT or SD-JWT VC presentation.

## Formal definition
A JWT used to demonstrate holder control of a key associated with an SD-JWT or SD-JWT VC presentation.

## Why this concept matters
This concept is provided as a controlled glossary entry for standards, governance, and implementation review.

Use this concept consistently when mapping authority, evidence, reliance, and auditability across governance and implementation artifacts.

## Names and relationships

### Alternative designations
- **KB-JWT** (`en`, `alternative`)
- **Key Binding JWT** (`en`, `alternative`)

### Related concepts
- [holder-binding]({{ '/terms/holder-binding/' | relative_url }})
- [sd-jwt-vc]({{ '/terms/sd-jwt-vc/' | relative_url }})
- [proof-of-possession]({{ '/terms/proof-of-possession/' | relative_url }})
- [cryptographic-key]({{ '/terms/cryptographic-key/' | relative_url }})

### Semantic relations
- **related**: `urn:tig:concept:holder-binding`
- **related**: `urn:tig:concept:sd-jwt-vc`
- **related**: `urn:tig:concept:proof-of-possession`
- **related**: `urn:tig:concept:cryptographic-key`

### Cross-vocabulary mappings
Not specified

## Provenance and identity
- **Concept ID**: `urn:tig:concept:key-binding-jwt`
- **Editorial status**: `stable`
- **Provenance classification**: `locally_defined`
- **Source corpus**: Trust Infrastructure Glossary

### Standards and source references
- [SD-JWT-based Verifiable Credentials](https://www.rfc-editor.org/rfc/rfc9901.html) (IETF; RFC; 9901; 2025) — normative

<details markdown="1">
<summary><strong>Implementation and governance metadata</strong></summary>

### Legacy aliases
KB-JWT, Key Binding JWT

### Governance profile
- **Authority scope**: verification_and_reliance
- **Delegation mode**: direct
- **Revocation supported**: False
- **Lifecycle states**: proposed, active, retired
- **Execution role**: hybrid
- **Control-plane role**: decision_plane_component

### Enforcement points
- reliance_decision

### Assurance
**Evidence artifacts**
- verification_log
- audit_log

- **Assurance level hint**: AL2+
- **Auditability**: high

### Control plane
**Decision points**
- reliance_decision

- **Accountable entity**: glossary_maintainers

**Evidence produced**
- verification_log
- audit_log

### Notes
Not specified

### Supporting definitions
Not specified

### Mental models
Not specified

### Crosswalk references
- **IETF**: RFC 9901

</details>

---

*Generated from `glossary/terms/key-binding-jwt.yaml`. Edit the source concept and regenerate rather than editing this page directly.*
