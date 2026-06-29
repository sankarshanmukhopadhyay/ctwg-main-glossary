---
title: "identity-provider"
---

> Generated file. Update `glossary/terms/identity-provider.yaml` and regenerate artifacts instead of editing this page directly.

# identity-provider

## Definition
An identity provider (abbreviated IdP or IDP) is a system entity that creates, maintains, and manages identity information for principals and also provides authentication services to relying applications within a federation or distributed network.

## Reader Note
This term is provided as a controlled glossary entry for standards, governance, and implementation review.

## Implementation Relevance
Use this term consistently when mapping authority, evidence, reliance, and auditability across governance and implementation artifacts.

## Aliases
identity provider, identity providers, IdP, IdPs

## See Also
- [verification]({{ '/terms/verification/' | relative_url }})
- [verifier]({{ '/terms/verifier/' | relative_url }})
- [relying-party]({{ '/terms/relying-party/' | relative_url }})
- [trust-decision]({{ '/terms/trust-decision/' | relative_url }})
- [authorization]({{ '/terms/authorization/' | relative_url }})
- [permission]({{ '/terms/permission/' | relative_url }})

## Standards and Source References
- [Wikipedia](https://en.wikipedia.org/wiki/Identity_provider).

## Governance Profile
- **Authority scope**: verification_and_reliance, access_decisioning
- **Delegation mode**: direct
- **Revocation supported**: False
- **Lifecycle states**: documented, active, deprecated
- **Execution role**: runtime
- **Control-plane role**: decision_plane_component

## Enforcement Points
- reliance_decision
- access_decision

## Assurance
**Evidence artifacts**
- verification_log
- access_decision_log

- **Assurance level hint**: AL2+
- **Auditability**: high

## Control Plane
**Decision points**
- reliance_decision
- access_decision

- **Accountable entity**: glossary_maintainers

**Evidence produced**
- verification_log
- access_decision_log

## Notes
- The term “identity provider” is used in federated identity systems because it is a required component of their architecture. By contrast, decentralized identity and self-sovereign identity systems do not use the term because they are architected to enable entities to create and control their own digital identities without the need to depend on an external provider.

## Supporting Definitions
Not specified

## Mental Models
Not specified

## Crosswalk References
Not specified
