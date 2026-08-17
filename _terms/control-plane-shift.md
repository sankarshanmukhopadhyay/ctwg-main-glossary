---
title: "control-plane shift"
---

> Generated file. Update `glossary/terms/control-plane-shift.yaml` and regenerate artifacts instead of editing this page directly.

# control-plane shift

## Concept Identity
- **Concept ID**: `urn:tig:concept:control-plane-shift`
- **Editorial status**: `stable`
- **Provenance classification**: `locally_defined`
- **Source corpus**: Trust Infrastructure Glossary

## In Simple English
A change in which actor, policy, infrastructure component, or governance mechanism can determine, constrain, or revoke system behavior.

## Definition
A change in which actor, policy, infrastructure component, or governance mechanism can determine, constrain, or revoke system behavior.

## Reader Note
This term was added following a cross-repository terminology review of TSMM, TIS, TGA, and the DTG ZKP Task Force workspace.

## Implementation Relevance
Use this term to keep runtime governance, delegation, evidence, and privacy semantics consistent across interoperating trust infrastructure repositories.

## Alternative Designations
- **control-plane-shift** (`en`, `alternative`)

## Legacy Aliases
control-plane shift, control-plane-shift

## Semantic Relations
- **related**: `urn:tig:concept:locus-of-control`
- **related**: `urn:tig:concept:authority`
- **related**: `urn:tig:concept:governance`

## Cross-Vocabulary Mappings
Not specified

## See Also
- [locus-of-control]({{ '/terms/locus-of-control/' | relative_url }})
- [authority]({{ '/terms/authority/' | relative_url }})
- [governance]({{ '/terms/governance/' | relative_url }})

## Standards and Source References
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
