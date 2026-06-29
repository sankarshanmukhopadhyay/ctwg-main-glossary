---
title: "entity-statement"
---

> Generated file. Update `glossary/terms/entity-statement.yaml` and regenerate artifacts instead of editing this page directly.

# entity-statement

## Definition
A signed statement in OpenID Federation that describes metadata, authority, and trust relationships for a federation entity.

## Reader Note
This term is part of the v1.2.0 standards-linked refresh and is anchored to active implementation vocabulary.

## Implementation Relevance
Use this term when mapping glossary language to implementation profiles, governance controls, conformance checks, or assurance evidence.

## Aliases
entity statement

## See Also
- [openid-federation]({{ '/terms/openid-federation/' | relative_url }})
- [federation]({{ '/terms/federation/' | relative_url }})
- [trust-chain]({{ '/terms/trust-chain/' | relative_url }})
- [metadata]({{ '/terms/metadata/' | relative_url }})

## Standards and Source References
- [OpenID Federation 1.0](https://openid.net/specs/openid-federation-1_0.html) (OpenID Foundation; Final Specification; 1.0; 2026-02-17) — normative

## Governance Profile
- **Authority scope**: governance_recognition, registry_management
- **Delegation mode**: direct
- **Revocation supported**: False
- **Lifecycle states**: proposed, active, retired
- **Execution role**: hybrid
- **Control-plane role**: decision_plane_component

## Enforcement Points
- registration_decision
- reliance_decision

## Assurance
**Evidence artifacts**
- registry_entry
- verification_log
- audit_log

- **Assurance level hint**: AL2+
- **Auditability**: high

## Control Plane
**Decision points**
- registration_decision
- reliance_decision

- **Accountable entity**: glossary_maintainers

**Evidence produced**
- registry_entry
- verification_log
- audit_log

## Notes
Not specified

## Supporting Definitions
Not specified

## Mental Models
Not specified

## Crosswalk References
- **OPENID**: OpenID Federation 1.0
