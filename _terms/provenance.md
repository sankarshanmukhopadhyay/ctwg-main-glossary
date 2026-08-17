---
title: "provenance"
---

# provenance

Information about where something came from and what happened to it over time.

## Formal definition
Information about the origin, history, custody, transformation, or source lineage of data, content, credentials, or governed artifacts.

## Why this concept matters
This bridge term improves navigation across privacy, status, provenance, and assurance concepts.

Use this term where evidence needs to be carried across both reader-facing documentation and machine-verifiable assurance artifacts.

## Names and relationships

### Alternative designations
None

### Related concepts
- [c2pa-manifest]({{ '/terms/c2pa-manifest/' | relative_url }})
- [content-credential]({{ '/terms/content-credential/' | relative_url }})
- [audit-log]({{ '/terms/audit-log/' | relative_url }})
- [authenticity]({{ '/terms/authenticity/' | relative_url }})

### Semantic relations
- **related**: `urn:tig:concept:c2pa-manifest`
- **related**: `urn:tig:concept:content-credential`
- **related**: `urn:tig:concept:audit-log`
- **related**: `urn:tig:concept:authenticity`

### Cross-vocabulary mappings
Not specified

## Provenance and identity
- **Concept ID**: `urn:tig:concept:provenance`
- **Editorial status**: `stable`
- **Provenance classification**: `locally_defined`
- **Source corpus**: Trust Infrastructure Glossary

### Standards and source references
- [C2PA Technical Specification 2.2](https://spec.c2pa.org/specifications/specifications/2.2/specs/C2PA_Specification.html) (C2PA; Technical Specification; 2.2; 2025) — normative

<details markdown="1">
<summary><strong>Implementation and governance metadata</strong></summary>

### Legacy aliases
provenance

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
- **C2PA**: C2PA Technical Specification 2.2

</details>

---

*Generated from `glossary/terms/provenance.yaml`. Edit the source concept and regenerate rather than editing this page directly.*
