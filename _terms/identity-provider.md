---
title: "identity-provider"
---

> Generated file. Update `glossary/terms/identity-provider.yaml` and regenerate artifacts instead of editing this page directly.

# identity-provider

## Definition
An identity provider (abbreviated IdP or IDP) is a system entity that creates, maintains, and manages identity information for principals and also provides authentication services to relying applications within a federation or distributed network.

## Aliases
identity provider, identity providers, IdP, IdPs

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

## See Also
- verification
- verifier
- relying-party
- trust-decision
- authorization
- permission

## Crosswalk References
Not specified
