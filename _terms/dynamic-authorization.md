---
title: "dynamic authorization"
---

> Generated file. Update `glossary/terms/dynamic-authorization.yaml` and regenerate artifacts instead of editing this page directly.

# dynamic authorization

## Concept Identity
- **Concept ID**: `urn:tig:concept:dynamic-authorization`
- **Editorial status**: `stable`
- **Provenance classification**: `locally_defined`
- **Source corpus**: Trust Infrastructure Glossary

## In Simple English
An authorization approach in which runtime decisions are produced by evaluating contextual attributes, evidence, and policy rather than relying only on static permissions.

## Definition
An authorization approach in which runtime decisions are produced by evaluating contextual attributes, evidence, and policy rather than relying only on static permissions.

## Reader Note
This term was added following a cross-repository terminology review of TSMM, TIS, TGA, and the DTG ZKP Task Force workspace.

## Implementation Relevance
Use this term to keep runtime governance, delegation, evidence, and privacy semantics consistent across interoperating trust infrastructure repositories.

## Alternative Designations
- **dynamic-authorization** (`en`, `alternative`)

## Legacy Aliases
dynamic authorization, dynamic-authorization

## Semantic Relations
- **related**: `urn:tig:concept:authorization`
- **related**: `urn:tig:concept:attribute-based-access-control`

## Cross-Vocabulary Mappings
Not specified

## See Also
- [authorization]({{ '/terms/authorization/' | relative_url }})
- [attribute-based-access-control]({{ '/terms/attribute-based-access-control/' | relative_url }})

## Standards and Source References
- [TSMM repository terminology and model documentation](https://github.com/sankarshanmukhopadhyay/trust-systems-meta-model) (GitHub) — informative

## Governance Profile
- **Authority scope**: assurance_and_audit, delegation_and_scope, policy_definition, verification_and_reliance
- **Delegation mode**: direct_or_constrained
- **Revocation supported**: True
- **Lifecycle states**: proposed, active, suspended, revoked, retired
- **Execution role**: hybrid
- **Control-plane role**: decision_plane_component

## Enforcement Points
- policy_approval
- delegation_grant
- reliance_decision
- revocation_decision

## Assurance
**Evidence artifacts**
- policy_document
- delegation_record
- status_record
- verification_log

- **Assurance level hint**: AL2+
- **Auditability**: high

## Control Plane
**Decision points**
- policy_approval
- delegation_grant
- reliance_decision
- revocation_decision

- **Accountable entity**: governance_authority

**Evidence produced**
- policy_document
- delegation_record
- status_record
- verification_log

## Notes
- This definition is normalized for cross-repository use and should be applied together with the governing profile or specification that supplies domain-specific constraints.

## Supporting Definitions
Not specified

## Mental Models
Not specified

## Crosswalk References
Not specified
