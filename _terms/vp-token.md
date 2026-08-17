---
title: "vp-token"
---

> Generated file. Update `glossary/terms/vp-token.yaml` and regenerate artifacts instead of editing this page directly.

# vp-token

## Concept Identity
- **Concept ID**: `urn:tig:concept:vp-token`
- **Editorial status**: `stable`
- **Provenance classification**: `locally_defined`
- **Source corpus**: Trust Infrastructure Glossary

## In Simple English
An OpenID4VP response artifact containing one or more presentations returned to a verifier in response to an authorization request.

## Definition
An OpenID4VP response artifact containing one or more presentations returned to a verifier in response to an authorization request.

## Reader Note
This term is provided as a controlled glossary entry for standards, governance, and implementation review.

## Implementation Relevance
Use this term consistently when mapping authority, evidence, reliance, and auditability across governance and implementation artifacts.

## Alternative Designations
- **VP Token** (`en`, `alternative`)
- **vp_token** (`en`, `alternative`)

## Legacy Aliases
VP Token, vp_token

## Semantic Relations
- **related**: `urn:tig:concept:openid4vp`
- **related**: `urn:tig:concept:verifiable-presentation`
- **related**: `urn:tig:concept:presentation`
- **related**: `urn:tig:concept:verifier`

## Cross-Vocabulary Mappings
Not specified

## See Also
- [openid4vp]({{ '/terms/openid4vp/' | relative_url }})
- [verifiable-presentation]({{ '/terms/verifiable-presentation/' | relative_url }})
- [presentation]({{ '/terms/presentation/' | relative_url }})
- [verifier]({{ '/terms/verifier/' | relative_url }})

## Standards and Source References
- [OpenID for Verifiable Presentations 1.0](https://openid.net/specs/openid-4-verifiable-presentations-1_0.html) (OpenID Foundation; Final Specification; 1.0; 2025-07-09) — normative

## Governance Profile
- **Authority scope**: verification_and_reliance
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
- **OPENID**: OpenID4VP 1.0
