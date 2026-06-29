---
title: "governing-body"
---

> Generated file. Update `glossary/terms/governing-body.yaml` and regenerate artifacts instead of editing this page directly.

# governing-body

## Definition
The party (or set of parties) authoritative for governing a trust community, usually (but not always) by developing, publishing, maintaining, and enforcing a governance framework. A governing body may be a government, a formal legal entity of any kind, an informal group of any kind, or an individual. A governing body may also delegate operational responsibilities to an administering body.

## Reader Note
This term is provided as a controlled glossary entry for standards, governance, and implementation review.

## Implementation Relevance
Use this term consistently when mapping authority, evidence, reliance, and auditability across governance and implementation artifacts.

## Aliases
governing body, governing bodies

## See Also
- [policy]({{ '/terms/policy/' | relative_url }})
- [governance-framework]({{ '/terms/governance-framework/' | relative_url }})
- [requirement]({{ '/terms/requirement/' | relative_url }})
- [delegation]({{ '/terms/delegation/' | relative_url }})
- [delegator]({{ '/terms/delegator/' | relative_url }})
- [delegatee]({{ '/terms/delegatee/' | relative_url }})

## Standards and Source References
- ToIP CTWG maintained glossary source: `spec/terms-definitions/governing-body.md`

## Governance Profile
- **Authority scope**: policy_definition, delegation_and_scope, governance_recognition
- **Delegation mode**: direct_or_constrained
- **Revocation supported**: True
- **Lifecycle states**: proposed, active, suspended, revoked, retired
- **Execution role**: runtime
- **Control-plane role**: decision_plane_component

## Enforcement Points
- policy_approval
- delegation_grant
- revocation_decision

## Assurance
**Evidence artifacts**
- policy_document
- delegation_record
- audit_log
- status_record
- verification_log
- registry_entry

- **Assurance level hint**: AL2+
- **Auditability**: high

## Control Plane
**Decision points**
- policy_approval
- delegation_grant
- revocation_decision

- **Accountable entity**: governance_authority

**Evidence produced**
- policy_document
- delegation_record
- audit_log
- status_record
- verification_log
- registry_entry

## Notes
Not specified

## Supporting Definitions
- Also known as: [[ref: governing authority]].

## Mental Models
Not specified

## Crosswalk References
Not specified
