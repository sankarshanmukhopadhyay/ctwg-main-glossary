---
title: "appraisability"
---

> Generated file. Update `glossary/terms/appraisability.yaml` and regenerate artifacts instead of editing this page directly.

# appraisability

## Definition
The ability for a communication endpoint identified with a verifiable identifier (VID) to be appraised for the set of its properties that enable a relying party or a verifier to make a trust decision about communicating with that endpoint.

## Reader Note
This term is provided as a controlled glossary entry for standards, governance, and implementation review.

## Implementation Relevance
Use this term consistently when mapping authority, evidence, reliance, and auditability across governance and implementation artifacts.

## Aliases
appraisability, appraisable, appraise

## See Also
- [trust basis]({{ '/terms/trust-basis/' | relative_url }})
- [verifiability]({{ '/terms/verifiable/' | relative_url }})

## Standards and Source References
- ToIP CTWG maintained glossary source: `spec/terms-definitions/appraisability.md`

## Governance Profile
- **Authority scope**: verification_and_reliance
- **Delegation mode**: direct
- **Revocation supported**: False
- **Lifecycle states**: documented, active, deprecated
- **Execution role**: runtime
- **Control-plane role**: decision_plane_component

## Enforcement Points
- reliance_decision

## Assurance
**Evidence artifacts**
- verification_log

- **Assurance level hint**: AL2+
- **Auditability**: high

## Control Plane
**Decision points**
- reliance_decision

- **Accountable entity**: verifier_operator

**Evidence produced**
- verification_log

## Notes
Not specified

## Supporting Definitions
Not specified

## Mental Models
Not specified

## Crosswalk References
Not specified
