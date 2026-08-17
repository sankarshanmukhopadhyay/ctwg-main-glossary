---
title: "verifiable-presentation"
---

> Generated file. Update `glossary/terms/verifiable-presentation.yaml` and regenerate artifacts instead of editing this page directly.

# verifiable-presentation

## In Simple English
A presentation with cryptographic proof or securing material that enables a verifier to check integrity, holder binding, or other presentation-specific verification requirements.

## Definition
A presentation with cryptographic proof or securing material that enables a verifier to check integrity, holder binding, or other presentation-specific verification requirements.

## Reader Note
Use this term for the presented artifact. Use openid4vp or vp-token when referring to the OpenID protocol container and flow.

## Implementation Relevance
A verifier should validate the presentation, intended audience, challenge or nonce binding, status information, and applicable policy before relying on it.

## Aliases
verifiable presentation, verifiable presentations, VP, VPs

## See Also
- [presentation]({{ '/terms/presentation/' | relative_url }})
- [vp-token]({{ '/terms/vp-token/' | relative_url }})
- [openid4vp]({{ '/terms/openid4vp/' | relative_url }})
- [verifiable-credential]({{ '/terms/verifiable-credential/' | relative_url }})
- [holder-binding]({{ '/terms/holder-binding/' | relative_url }})

## Standards and Source References
- [Verifiable Credentials Data Model v2.0](https://www.w3.org/TR/vc-data-model-2.0/) (W3C; Recommendation; 2.0; 2025-05-15) — normative

## Governance Profile
- **Authority scope**: verification_and_reliance
- **Delegation mode**: direct
- **Revocation supported**: False
- **Lifecycle states**: proposed, active, retired
- **Execution role**: runtime
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
- **W3C**: VC Data Model v2.0
- **OPENID**: OpenID4VP 1.0
