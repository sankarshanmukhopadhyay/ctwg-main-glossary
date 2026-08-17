---
title: "nullifier"
---

> Generated file. Update `glossary/terms/nullifier.yaml` and regenerate artifacts instead of editing this page directly.

# nullifier

## Concept Identity
- **Concept ID**: `urn:tig:concept:nullifier`
- **Editorial status**: `stable`
- **Provenance classification**: `locally_defined`
- **Source corpus**: Trust Infrastructure Glossary

## In Simple English
A simple-English summary has not yet been added for this term.

## Definition
A cryptographically derived value used to detect prohibited reuse or duplication within a defined scope without revealing the underlying secret or necessarily enabling correlation across other scopes.

## Reader Note
This term was added following a cross-repository terminology review of TSMM, TIS, TGA, and the DTG ZKP Task Force workspace.

## Implementation Relevance
Use this term to keep runtime governance, delegation, evidence, and privacy semantics consistent across interoperating trust infrastructure repositories.

## Alternative Designations
None

## Legacy Aliases
nullifier

## Semantic Relations
- **related**: `urn:tig:concept:zero-knowledge-proof`
- **related**: `urn:tig:concept:correlation-privacy`

## Cross-Vocabulary Mappings
Not specified

## See Also
- [zero-knowledge-proof]({{ '/terms/zero-knowledge-proof/' | relative_url }})
- [correlation-privacy]({{ '/terms/correlation-privacy/' | relative_url }})

## Standards and Source References
- [ZKP repository terminology and model documentation](https://github.com/trustoverip/dtgwg-zkp-tf) (GitHub) — informative

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
