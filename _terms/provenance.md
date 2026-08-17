---
title: "provenance"
---

> Generated file. Update `glossary/terms/provenance.yaml` and regenerate artifacts instead of editing this page directly.

# provenance

## Concept Identity
- **Concept ID**: `urn:tig:concept:provenance`
- **Editorial status**: `stable`
- **Provenance classification**: `locally_defined`
- **Source corpus**: Trust Infrastructure Glossary

## In Simple English
Information about where something came from and what happened to it over time.

## Definition
Information about the origin, history, custody, transformation, or source lineage of data, content, credentials, or governed artifacts.

## Reader Note
This bridge term improves navigation across privacy, status, provenance, and assurance concepts.

## Implementation Relevance
Use this term where evidence needs to be carried across both reader-facing documentation and machine-verifiable assurance artifacts.

## Alternative Designations
None

## Legacy Aliases
provenance

## Semantic Relations
- **related**: `urn:tig:concept:c2pa-manifest`
- **related**: `urn:tig:concept:content-credential`
- **related**: `urn:tig:concept:audit-log`
- **related**: `urn:tig:concept:authenticity`

## Cross-Vocabulary Mappings
Not specified

## See Also
- [c2pa-manifest]({{ '/terms/c2pa-manifest/' | relative_url }})
- [content-credential]({{ '/terms/content-credential/' | relative_url }})
- [audit-log]({{ '/terms/audit-log/' | relative_url }})
- [authenticity]({{ '/terms/authenticity/' | relative_url }})

## Standards and Source References
- [C2PA Technical Specification 2.2](https://spec.c2pa.org/specifications/specifications/2.2/specs/C2PA_Specification.html) (C2PA; Technical Specification; 2.2; 2025) — normative

## Governance Profile
- **Authority scope**: assurance_and_audit, verification_and_reliance
- **Delegation mode**: direct
- **Revocation supported**: False
- **Lifecycle states**: proposed, active, retired
- **Execution role**: hybrid
- **Control-plane role**: decision_plane_component

## Enforcement Points
- reliance_decision

## Assurance
**Evidence artifacts**
- verification_log
- audit_log

- **Assurance level hint**: AL2+
- **Auditability**: high

## Control Plane
**Decision points**
- reliance_decision

- **Accountable entity**: glossary_maintainers

**Evidence produced**
- verification_log
- audit_log

## Notes
Not specified

## Supporting Definitions
Not specified

## Mental Models
Not specified

## Crosswalk References
- **C2PA**: C2PA Technical Specification 2.2
