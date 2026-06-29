---
title: "self-certifying-identifier"
---

> Generated file. Update `glossary/terms/self-certifying-identifier.yaml` and regenerate artifacts instead of editing this page directly.

# self-certifying-identifier

## Definition
A subclass of verifiable identifier (VID) that is cryptographically verifiable without the need to rely on any third party for verification because the identifier is cryptographically bound to the cryptographic keys from which it was generated.

## Reader Note
This term is provided as a controlled glossary entry for standards, governance, and implementation review.

## Implementation Relevance
Use this term consistently when mapping authority, evidence, reliance, and auditability across governance and implementation artifacts.

## Aliases
self-certifying identifier, self-certifying identifiers, SCID, SCIDs

## See Also
- [autonomic-identifier]({{ '/terms/autonomic-identifier/' | relative_url }})
- [verifiable-identifier]({{ '/terms/verifiable-identifier/' | relative_url }})
- [cryptographic-key]({{ '/terms/cryptographic-key/' | relative_url }})

## Standards and Source References
- ToIP CTWG maintained glossary source: `spec/terms-definitions/self-certifying-identifier.md`

## Governance Profile
- **Authority scope**: verification_and_reliance
- **Delegation mode**: direct
- **Revocation supported**: False
- **Lifecycle states**: documented, active, deprecated
- **Execution role**: design
- **Control-plane role**: reference_term

## Enforcement Points
- reliance_decision

## Assurance
**Evidence artifacts**
- verification_log

- **Assurance level hint**: AL1+
- **Auditability**: moderate

## Control Plane
**Decision points**
- reliance_decision

- **Accountable entity**: glossary_maintainers

**Evidence produced**
- verification_log

## Notes
Not specified

## Supporting Definitions
- Also known as: [[ref: SCID]].

## Mental Models
Not specified

## Crosswalk References
Not specified
