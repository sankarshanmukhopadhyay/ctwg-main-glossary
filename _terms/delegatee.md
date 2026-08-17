---
title: "delegatee"
---

> Generated file. Update `glossary/terms/delegatee.yaml` and regenerate artifacts instead of editing this page directly.

# delegatee

## In Simple English
The second party receiving a delegation from a first party (the delegator) and authorized to act only within the granted scope and applicable constraints.

## Definition
The second party receiving a delegation from a first party (the delegator) and authorized to act only within the granted scope and applicable constraints.

## Reader Note
This term is provided as a controlled glossary entry for standards, governance, and implementation review.

## Implementation Relevance
Use this term consistently when mapping authority, evidence, reliance, and auditability across governance and implementation artifacts.

## Aliases
delegatee, delegatees

## See Also
- [delegation]({{ '/terms/delegation/' | relative_url }})
- [delegator]({{ '/terms/delegator/' | relative_url }})
- [authorization]({{ '/terms/authorization/' | relative_url }})
- [revocation]({{ '/terms/revocation/' | relative_url }})

## Standards and Source References
- ToIP CTWG maintained glossary source: `spec/terms-definitions/delegatee.md`

## Governance Profile
- **Authority scope**: delegation_and_scope
- **Delegation mode**: direct_or_constrained
- **Revocation supported**: True
- **Lifecycle states**: proposed, active, suspended, revoked, retired
- **Execution role**: runtime
- **Control-plane role**: decision_plane_component

## Enforcement Points
- delegation_grant
- revocation_decision

## Assurance
**Evidence artifacts**
- delegation_record
- policy_document
- status_record
- audit_log
- verification_log
- registry_entry

- **Assurance level hint**: AL2+
- **Auditability**: high

## Control Plane
**Decision points**
- delegation_grant
- revocation_decision

- **Accountable entity**: glossary_maintainers

**Evidence produced**
- delegation_record
- policy_document
- status_record
- audit_log
- verification_log
- registry_entry

## Notes
Not specified

## Supporting Definitions
Not specified

## Mental Models
Not specified

## Crosswalk References
Not specified
