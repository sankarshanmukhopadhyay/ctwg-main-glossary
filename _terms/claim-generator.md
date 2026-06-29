---
title: "claim-generator"
---

> Generated file. Update `glossary/terms/claim-generator.yaml` and regenerate artifacts instead of editing this page directly.

# claim-generator

## Definition
A hardware or software actor that creates a C2PA claim about an asset and signs or causes the signing of the associated manifest data.

## Reader Note
This term is part of the v1.2.0 standards-linked refresh and is anchored to active implementation vocabulary.

## Implementation Relevance
Use this term when mapping glossary language to implementation profiles, governance controls, conformance checks, or assurance evidence.

## Aliases
C2PA claim generator, claim generator

## See Also
- [c2pa-manifest]({{ '/terms/c2pa-manifest/' | relative_url }})
- [content-credential]({{ '/terms/content-credential/' | relative_url }})
- [actor]({{ '/terms/actor/' | relative_url }})
- [digital-signature]({{ '/terms/digital-signature/' | relative_url }})

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
- attestation
- verification_log
- audit_log

- **Assurance level hint**: AL2+
- **Auditability**: high

## Control Plane
**Decision points**
- reliance_decision

- **Accountable entity**: glossary_maintainers

**Evidence produced**
- attestation
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
