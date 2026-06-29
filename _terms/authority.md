---
title: "authority"
---

> Generated file. Update `glossary/terms/authority.yaml` and regenerate artifacts instead of editing this page directly.

# authority

## Definition
A party whose decisions, policies, rules, or recognition outcomes are accepted as governing, directive, or controlling by other parties within a defined scope.

## Reader Note
This term is provided as a controlled glossary entry for standards, governance, and implementation review.

## Implementation Relevance
Use this term consistently when mapping authority, evidence, reliance, and auditability across governance and implementation artifacts.

## Aliases
authority, authorities

## See Also
- [policy]({{ '/terms/policy/' | relative_url }})
- [governance-framework]({{ '/terms/governance-framework/' | relative_url }})
- [requirement]({{ '/terms/requirement/' | relative_url }})
- [delegation]({{ '/terms/delegation/' | relative_url }})
- [delegator]({{ '/terms/delegator/' | relative_url }})
- [delegatee]({{ '/terms/delegatee/' | relative_url }})

## Standards and Source References
- [eSSIF-Lab](https://essif-lab.github.io/framework/docs/terms/authority).

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
- status_record

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
- status_record

## Notes
- The practical significance of an authority depends on the scope in which its decisions are recognized, how that scope is established, and whether that recognition can be delegated, constrained, contested, or revoked.

## Supporting Definitions
Not specified

## Mental Models
Not specified

## Crosswalk References
- **NIST**: PM-1
- **ISO**: ISO/IEC 42001 5.3
