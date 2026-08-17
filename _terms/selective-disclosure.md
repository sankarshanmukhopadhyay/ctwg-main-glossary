---
title: "selective-disclosure"
---

# selective-disclosure

A privacy-preserving presentation capability that allows a holder to disclose only selected claims or attributes from a credential while preserving verifiability.

## Formal definition
A privacy-preserving presentation capability that allows a holder to disclose only selected claims or attributes from a credential while preserving verifiability.

## Why this concept matters
This bridge term improves navigation across privacy, status, provenance, and assurance concepts.

Use this term where evidence needs to be carried across both reader-facing documentation and machine-verifiable assurance artifacts.

## Names and relationships

### Alternative designations
- **selective disclosure** (`en`, `alternative`)

### Related concepts
- [sd-jwt-vc]({{ '/terms/sd-jwt-vc/' | relative_url }})
- [verifiable-presentation]({{ '/terms/verifiable-presentation/' | relative_url }})
- [zero-knowledge-proof]({{ '/terms/zero-knowledge-proof/' | relative_url }})
- [correlation-privacy]({{ '/terms/correlation-privacy/' | relative_url }})

### Semantic relations
- **related**: `urn:tig:concept:sd-jwt-vc`
- **related**: `urn:tig:concept:verifiable-presentation`
- **related**: `urn:tig:concept:zero-knowledge-proof`
- **related**: `urn:tig:concept:correlation-privacy`

### Cross-vocabulary mappings
Not specified

## Provenance and identity
- **Concept ID**: `urn:tig:concept:selective-disclosure`
- **Editorial status**: `stable`
- **Provenance classification**: `locally_defined`
- **Source corpus**: Trust Infrastructure Glossary

### Standards and source references
- [SD-JWT-based Verifiable Credentials](https://www.rfc-editor.org/rfc/rfc9901.html) (IETF; RFC; 9901; 2025) — normative

<details markdown="1">
<summary><strong>Implementation and governance metadata</strong></summary>

### Legacy aliases
selective disclosure

### Governance profile
- **Authority scope**: assurance_and_audit, verification_and_reliance
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
- **W3C**: VC Data Model v2.0
- **IETF**: RFC 9901

</details>

---

*Generated from `glossary/terms/selective-disclosure.yaml`. Edit the source concept and regenerate rather than editing this page directly.*
