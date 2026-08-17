---
title: "vp-token"
---

# vp-token

An OpenID4VP response artifact containing one or more presentations returned to a verifier in response to an authorization request.

## Formal definition
An OpenID4VP response artifact containing one or more presentations returned to a verifier in response to an authorization request.

## Why this concept matters
This concept is provided as a controlled glossary entry for standards, governance, and implementation review.

Use this concept consistently when mapping authority, evidence, reliance, and auditability across governance and implementation artifacts.

## Names and relationships

### Alternative designations
- **VP Token** (`en`, `alternative`)
- **vp_token** (`en`, `alternative`)

### Related concepts
- [openid4vp]({{ '/terms/openid4vp/' | relative_url }})
- [verifiable-presentation]({{ '/terms/verifiable-presentation/' | relative_url }})
- [presentation]({{ '/terms/presentation/' | relative_url }})
- [verifier]({{ '/terms/verifier/' | relative_url }})

### Semantic relations
- **related**: `urn:tig:concept:openid4vp`
- **related**: `urn:tig:concept:verifiable-presentation`
- **related**: `urn:tig:concept:presentation`
- **related**: `urn:tig:concept:verifier`

### Cross-vocabulary mappings
Not specified

## Provenance and identity
- **Concept ID**: `urn:tig:concept:vp-token`
- **Editorial status**: `stable`
- **Provenance classification**: `locally_defined`
- **Source corpus**: Trust Infrastructure Glossary

### Standards and source references
- [OpenID for Verifiable Presentations 1.0](https://openid.net/specs/openid-4-verifiable-presentations-1_0.html) (OpenID Foundation; Final Specification; 1.0; 2025-07-09) — normative

<details markdown="1">
<summary><strong>Implementation and governance metadata</strong></summary>

### Legacy aliases
VP Token, vp_token

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
- **OPENID**: OpenID4VP 1.0

</details>

---

*Generated from `glossary/terms/vp-token.yaml`. Edit the source concept and regenerate rather than editing this page directly.*
