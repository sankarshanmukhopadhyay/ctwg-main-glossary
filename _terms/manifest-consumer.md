---
title: "manifest-consumer"
---

# manifest-consumer

An actor that consumes an asset with an associated C2PA manifest to obtain and evaluate provenance data.

## Formal definition
An actor that consumes an asset with an associated C2PA manifest to obtain and evaluate provenance data.

## Why this concept matters
This term is part of the v1.2.0 standards-linked refresh and is anchored to active implementation vocabulary.

Use this term when mapping glossary language to implementation profiles, governance controls, conformance checks, or assurance evidence.

## Names and relationships

### Alternative designations
- **C2PA manifest consumer** (`en`, `alternative`)
- **manifest consumer** (`en`, `alternative`)

### Related concepts
- [c2pa-manifest]({{ '/terms/c2pa-manifest/' | relative_url }})
- [content-credential]({{ '/terms/content-credential/' | relative_url }})
- [validation]({{ '/terms/validation/' | relative_url }})
- [provenance]({{ '/terms/provenance/' | relative_url }})

### Semantic relations
- **related**: `urn:tig:concept:c2pa-manifest`
- **related**: `urn:tig:concept:content-credential`
- **related**: `urn:tig:concept:validation`
- **related**: `urn:tig:concept:provenance`

### Cross-vocabulary mappings
Not specified

## Provenance and identity
- **Concept ID**: `urn:tig:concept:manifest-consumer`
- **Editorial status**: `stable`
- **Provenance classification**: `locally_defined`
- **Source corpus**: Trust Infrastructure Glossary

### Standards and source references
- [C2PA Technical Specification 2.2](https://spec.c2pa.org/specifications/specifications/2.2/specs/C2PA_Specification.html) (C2PA; Technical Specification; 2.2; 2025) — normative

<details markdown="1">
<summary><strong>Implementation and governance metadata</strong></summary>

### Legacy aliases
C2PA manifest consumer, manifest consumer

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
- **C2PA**: C2PA Technical Specification 2.2

</details>

---

*Generated from `glossary/terms/manifest-consumer.yaml`. Edit the source concept and regenerate rather than editing this page directly.*
