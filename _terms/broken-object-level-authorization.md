---
title: "broken-object-level-authorization"
---

> Generated file. Update `glossary/terms/broken-object-level-authorization.yaml` and regenerate artifacts instead of editing this page directly.

# broken-object-level-authorization

## In Simple English
Refers to security flaws where users can access data they shouldn't, due to inadequate permission checks on individual (sub)objects.

## Definition
Refers to security flaws where users can access data they shouldn't, due to inadequate permission checks on individual (sub)objects.

## Reader Note
This term is provided as a controlled glossary entry for standards, governance, and implementation review.

## Implementation Relevance
Use this term consistently when mapping authority, evidence, reliance, and auditability across governance and implementation artifacts.

## Aliases
broken-object-level-authorization, broken object level authorization

## See Also
- [authorization]({{ '/terms/authorization/' | relative_url }})
- [permission]({{ '/terms/permission/' | relative_url }})
- [role-based-access-control]({{ '/terms/role-based-access-control/' | relative_url }})
- [attribute-based-access-control]({{ '/terms/attribute-based-access-control/' | relative_url }})

## Standards and Source References
- ToIP CTWG maintained glossary source: `spec/terms-definitions/broken-object-level-authorization.md`

## Governance Profile
- **Authority scope**: access_decisioning
- **Delegation mode**: direct
- **Revocation supported**: True
- **Lifecycle states**: proposed, active, suspended, revoked, retired
- **Execution role**: runtime
- **Control-plane role**: decision_plane_component

## Enforcement Points
- access_decision
- revocation_decision

## Assurance
**Evidence artifacts**
- access_decision_log
- policy_document
- status_record
- audit_log
- verification_log
- registry_entry

- **Assurance level hint**: AL2+
- **Auditability**: high

## Control Plane
**Decision points**
- access_decision
- revocation_decision

- **Accountable entity**: glossary_maintainers

**Evidence produced**
- access_decision_log
- policy_document
- status_record
- audit_log
- verification_log
- registry_entry

## Notes
Not specified

## Supporting Definitions
- Also known as [[ref: BOLA]]

## Mental Models
Not specified

## Crosswalk References
Not specified
