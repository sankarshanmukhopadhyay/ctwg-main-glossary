---
title: "decision receipt"
---

> Generated file. Update `glossary/terms/decision-receipt.yaml` and regenerate artifacts instead of editing this page directly.

# decision receipt

## Concept Identity
- **Concept ID**: `urn:tig:concept:decision-receipt`
- **Editorial status**: `stable`
- **Provenance classification**: `locally_defined`
- **Source corpus**: Trust Infrastructure Glossary

## In Simple English
A record that explains what decision was made, under whose authority, using which policy and evidence, and with what result.

## Definition
A structured, integrity-protected record of a trust or governance decision, including the decision context, authority, policy, evidence, outcome, obligations, and traceability data.

## Reader Note
This term was added following a cross-repository terminology review of TSMM, TIS, TGA, and the DTG ZKP Task Force workspace.

## Implementation Relevance
Use this term to keep runtime governance, delegation, evidence, and privacy semantics consistent across interoperating trust infrastructure repositories.

## Alternative Designations
- **decision-receipt** (`en`, `alternative`)

## Legacy Aliases
decision receipt, decision-receipt

## Semantic Relations
- **related**: `urn:tig:concept:trust-decision`
- **related**: `urn:tig:concept:audit-log`
- **related**: `urn:tig:concept:attestation`

## Cross-Vocabulary Mappings
Not specified

## See Also
- [trust-decision]({{ '/terms/trust-decision/' | relative_url }})
- [audit-log]({{ '/terms/audit-log/' | relative_url }})
- [attestation]({{ '/terms/attestation/' | relative_url }})

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
