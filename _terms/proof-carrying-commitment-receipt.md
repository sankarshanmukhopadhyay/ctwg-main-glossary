---
title: "proof-carrying commitment receipt"
---

> Generated file. Update `glossary/terms/proof-carrying-commitment-receipt.yaml` and regenerate artifacts instead of editing this page directly.

# proof-carrying commitment receipt

## Concept Identity
- **Concept ID**: `urn:tig:concept:proof-carrying-commitment-receipt`
- **Editorial status**: `stable`
- **Provenance classification**: `locally_defined`
- **Source corpus**: Trust Infrastructure Glossary

## In Simple English
A simple-English summary has not yet been added for this term.

## Definition
A receipt that records a commitment together with cryptographic or verifiable evidence sufficient to evaluate who was authorized, what was committed, under which conditions, and with what lifecycle status.

## Reader Note
This term was added following a cross-repository terminology review of TSMM, TIS, TGA, and the DTG ZKP Task Force workspace.

## Implementation Relevance
Use this term to keep runtime governance, delegation, evidence, and privacy semantics consistent across interoperating trust infrastructure repositories.

## Alternative Designations
- **proof-carrying-commitment-receipt** (`en`, `alternative`)

## Legacy Aliases
proof-carrying commitment receipt, proof-carrying-commitment-receipt

## Semantic Relations
- **related**: `urn:tig:concept:claim`
- **related**: `urn:tig:concept:proof`

## Cross-Vocabulary Mappings
Not specified

## See Also
- [claim]({{ '/terms/claim/' | relative_url }})
- [proof]({{ '/terms/proof/' | relative_url }})

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
