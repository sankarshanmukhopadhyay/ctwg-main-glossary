---
title: "trust-anchor"
---

> Generated file. Update `glossary/terms/trust-anchor.yaml` and regenerate artifacts instead of editing this page directly.

# trust-anchor

## Definition
The authoritative source that serves as the origin of a trust chain.

## Reader Note
This term is provided as a controlled glossary entry for standards, governance, and implementation review.

## Implementation Relevance
Use this term consistently when mapping authority, evidence, reliance, and auditability across governance and implementation artifacts.

## Aliases
trust anchor, trust anchors

## See Also
- [governance]({{ '/terms/governance/' | relative_url }})
- [governance-framework]({{ '/terms/governance-framework/' | relative_url }})
- [governing-authority]({{ '/terms/governing-authority/' | relative_url }})
- [trust-registry]({{ '/terms/trust-registry/' | relative_url }})
- [definition]({{ '/terms/definition/' | relative_url }})
- [glossary]({{ '/terms/glossary/' | relative_url }})

## Standards and Source References
- ToIP CTWG maintained glossary source: `spec/terms-definitions/trust-anchor.md`

## Governance Profile
- **Authority scope**: governance_recognition
- **Delegation mode**: direct
- **Revocation supported**: False
- **Lifecycle states**: documented, active, deprecated
- **Execution role**: design
- **Control-plane role**: decision_plane_component

## Enforcement Points
- definition_approval

## Assurance
**Evidence artifacts**
- definition_change_record
- policy_document
- audit_log

- **Assurance level hint**: AL1+
- **Auditability**: moderate

## Control Plane
**Decision points**
- definition_approval

- **Accountable entity**: glossary_maintainers

**Evidence produced**
- definition_change_record
- policy_document
- audit_log

## Notes
- The term “trust anchor” is most commonly used in cryptography and public key infrastructure.

## Supporting Definitions
- Also known as: [[ref: trust root]].
- For more information, see: [Design Principles for the ToIP Stack](https://trustoverip.org/our-work/design-principles/).

## Mental Models
Not specified

## Crosswalk References
Not specified
