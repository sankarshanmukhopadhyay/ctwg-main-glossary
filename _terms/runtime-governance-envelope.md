---
title: "runtime governance envelope"
---

> Generated file. Update `glossary/terms/runtime-governance-envelope.yaml` and regenerate artifacts instead of editing this page directly.

# runtime governance envelope

## In Simple English
A structured envelope that binds the authority, policy, evidence, constraints, obligations, and lifecycle state applicable to a runtime interaction or task.

## Definition
A structured envelope that binds the authority, policy, evidence, constraints, obligations, and lifecycle state applicable to a runtime interaction or task.

## Reader Note
This term was added following a cross-repository terminology review of TSMM, TIS, TGA, and the DTG ZKP Task Force workspace.

## Implementation Relevance
Use this term to keep runtime governance, delegation, evidence, and privacy semantics consistent across interoperating trust infrastructure repositories.

## Aliases
runtime governance envelope, runtime-governance-envelope

## See Also
- [governance]({{ '/terms/governance/' | relative_url }})
- [authority]({{ '/terms/authority/' | relative_url }})
- [policy]({{ '/terms/policy/' | relative_url }})

## Standards and Source References
- [TIS repository terminology and model documentation](https://github.com/sankarshanmukhopadhyay/trust-infrastructure-schemas) (GitHub) — informative
- [TGA repository terminology and model documentation](https://github.com/sankarshanmukhopadhyay/trust-graph-artifacts) (GitHub) — informative

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
