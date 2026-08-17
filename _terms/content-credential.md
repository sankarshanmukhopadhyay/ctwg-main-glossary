---
title: "content-credential"
---

# content-credential

The user-facing C2PA term for provenance information represented by C2PA manifests associated with an asset.

## Formal definition
The user-facing C2PA term for provenance information represented by C2PA manifests associated with an asset.

## Why this concept matters
This term is part of the v1.2.0 standards-linked refresh and is anchored to active implementation vocabulary.

Use this term when mapping glossary language to implementation profiles, governance controls, conformance checks, or assurance evidence.

## Names and relationships

### Alternative designations
- **Content Credential** (`en`, `alternative`)
- **Content Credentials** (`en`, `alternative`)

### Related concepts
- [c2pa]({{ '/terms/c2pa/' | relative_url }})
- [c2pa-manifest]({{ '/terms/c2pa-manifest/' | relative_url }})
- [provenance]({{ '/terms/provenance/' | relative_url }})
- [authenticity]({{ '/terms/authenticity/' | relative_url }})

### Semantic relations
- **related**: `urn:tig:concept:c2pa`
- **related**: `urn:tig:concept:c2pa-manifest`
- **related**: `urn:tig:concept:provenance`
- **related**: `urn:tig:concept:authenticity`

### Cross-vocabulary mappings
Not specified

## Provenance and identity
- **Concept ID**: `urn:tig:concept:content-credential`
- **Editorial status**: `stable`
- **Provenance classification**: `locally_defined`
- **Source corpus**: Trust Infrastructure Glossary

### Standards and source references
- [C2PA Technical Specification 2.2](https://spec.c2pa.org/specifications/specifications/2.2/specs/C2PA_Specification.html) (C2PA; Technical Specification; 2.2; 2025) — normative

<details markdown="1">
<summary><strong>Implementation and governance metadata</strong></summary>

### Legacy aliases
Content Credential, Content Credentials

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
- attestation
- verification_log
- audit_log

- **Assurance level hint**: AL2+
- **Auditability**: high

### Control plane
**Decision points**
- reliance_decision

- **Accountable entity**: glossary_maintainers

**Evidence produced**
- attestation
- verification_log
- audit_log

### Notes
Not specified

### Supporting definitions
Not specified

### Mental models
Not specified

### Crosswalk references
- **C2PA**: C2PA Technical Specification 2.2

</details>

---

*Generated from `glossary/terms/content-credential.yaml`. Edit the source concept and regenerate rather than editing this page directly.*
