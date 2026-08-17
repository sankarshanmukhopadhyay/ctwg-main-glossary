---
title: "verifiable-presentation"
---

# verifiable-presentation

A presentation with cryptographic proof or securing material that enables a verifier to check integrity, holder binding, or other presentation-specific verification requirements.

## Formal definition
A presentation with cryptographic proof or securing material that enables a verifier to check integrity, holder binding, or other presentation-specific verification requirements.

## Why this concept matters
Use this term for the presented artifact. Use openid4vp or vp-token when referring to the OpenID protocol container and flow.

A verifier should validate the presentation, intended audience, challenge or nonce binding, status information, and applicable policy before relying on it.

## Names and relationships

### Alternative designations
- **verifiable presentation** (`en`, `alternative`)
- **verifiable presentations** (`en`, `alternative`)
- **VP** (`en`, `alternative`)
- **VPs** (`en`, `alternative`)

### Related concepts
- [presentation]({{ '/terms/presentation/' | relative_url }})
- [vp-token]({{ '/terms/vp-token/' | relative_url }})
- [openid4vp]({{ '/terms/openid4vp/' | relative_url }})
- [verifiable-credential]({{ '/terms/verifiable-credential/' | relative_url }})
- [holder-binding]({{ '/terms/holder-binding/' | relative_url }})

### Semantic relations
- **related**: `urn:tig:concept:presentation`
- **related**: `urn:tig:concept:vp-token`
- **related**: `urn:tig:concept:openid4vp`
- **related**: `urn:tig:concept:verifiable-credential`
- **related**: `urn:tig:concept:holder-binding`

### Cross-vocabulary mappings
Not specified

## Provenance and identity
- **Concept ID**: `urn:tig:concept:verifiable-presentation`
- **Editorial status**: `stable`
- **Provenance classification**: `locally_defined`
- **Source corpus**: Trust Infrastructure Glossary

### Standards and source references
- [Verifiable Credentials Data Model v2.0](https://www.w3.org/TR/vc-data-model-2.0/) (W3C; Recommendation; 2.0; 2025-05-15) — normative

<details markdown="1">
<summary><strong>Implementation and governance metadata</strong></summary>

### Legacy aliases
verifiable presentation, verifiable presentations, VP, VPs

### Governance profile
- **Authority scope**: verification_and_reliance
- **Delegation mode**: direct
- **Revocation supported**: False
- **Lifecycle states**: proposed, active, retired
- **Execution role**: runtime
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
- **W3C**: VC Data Model v2.0
- **OPENID**: OpenID4VP 1.0

</details>

---

*Generated from `glossary/terms/verifiable-presentation.yaml`. Edit the source concept and regenerate rather than editing this page directly.*
