---
title: "end-to-end-principle"
---

> Generated file. Update `glossary/terms/end-to-end-principle.yaml` and regenerate artifacts instead of editing this page directly.

# end-to-end-principle

## Definition
The end-to-end principle is a design framework in computer networking. In networks designed according to this principle, guaranteeing certain application-specific features, such as reliability and security, requires that they reside in the communicating end nodes of the network. Intermediary nodes, such as gateways and routers, that exist to establish the network, may implement these to improve efficiency but cannot guarantee end-to-end correctness.

## Reader Note
This term is provided as a controlled glossary entry for standards, governance, and implementation review.

## Implementation Relevance
Use this term consistently when mapping authority, evidence, reliance, and auditability across governance and implementation artifacts.

## Aliases
End-to-End Principle

## See Also
- [policy]({{ '/terms/policy/' | relative_url }})
- [governance-framework]({{ '/terms/governance-framework/' | relative_url }})
- [requirement]({{ '/terms/requirement/' | relative_url }})

## Standards and Source References
- [Wikipedia](https://en.wikipedia.org/wiki/End-to-end_principle).

## Governance Profile
- **Authority scope**: policy_definition
- **Delegation mode**: direct
- **Revocation supported**: False
- **Lifecycle states**: documented, active, deprecated
- **Execution role**: hybrid
- **Control-plane role**: decision_plane_component

## Enforcement Points
- policy_approval

## Assurance
**Evidence artifacts**
- policy_document

- **Assurance level hint**: AL2+
- **Auditability**: high

## Control Plane
**Decision points**
- policy_approval

- **Accountable entity**: glossary_maintainers

**Evidence produced**
- policy_document

## Notes
Not specified

## Supporting Definitions
- For more information, see: <https://trustoverip.org/permalink/Design-Principles-for-the-ToIP-Stack-V1.0-2022-11-17.pdf>

## Mental Models
Not specified

## Crosswalk References
Not specified
