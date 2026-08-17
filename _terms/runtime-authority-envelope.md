---
title: "runtime authority envelope"
---

> Generated file. Update `glossary/terms/runtime-authority-envelope.yaml` and regenerate artifacts instead of editing this page directly.

# runtime authority envelope

## Concept Identity
- **Concept ID**: `urn:tig:concept:runtime-authority-envelope`
- **Editorial status**: `stable`
- **Provenance classification**: `locally_defined`
- **Source corpus**: Trust Infrastructure Glossary

## In Simple English
The current set of permissions, limits, delegation history, and status that must be checked before an action is allowed.

## Definition
A runtime artifact that carries the currently valid authority, scope, constraints, delegation lineage, and status required before an action may be executed.

## Reader Note
This term was added following a cross-repository terminology review of TSMM, TIS, TGA, and the DTG ZKP Task Force workspace.

## Implementation Relevance
Use this term to keep runtime governance, delegation, evidence, and privacy semantics consistent across interoperating trust infrastructure repositories.

## Alternative Designations
- **runtime-authority-envelope** (`en`, `alternative`)

## Legacy Aliases
runtime authority envelope, runtime-authority-envelope

## Semantic Relations
- **related**: `urn:tig:concept:authority`
- **related**: `urn:tig:concept:policy`
- **related**: `urn:tig:concept:governance-framework`

## Cross-Vocabulary Mappings
Not specified

## See Also
- [authority]({{ '/terms/authority/' | relative_url }})
- [policy]({{ '/terms/policy/' | relative_url }})
- [governance-framework]({{ '/terms/governance-framework/' | relative_url }})

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
