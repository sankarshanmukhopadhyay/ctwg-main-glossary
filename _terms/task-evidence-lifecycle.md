---
title: "task evidence lifecycle"
---

> Generated file. Update `glossary/terms/task-evidence-lifecycle.yaml` and regenerate artifacts instead of editing this page directly.

# task evidence lifecycle

## Concept Identity
- **Concept ID**: `urn:tig:concept:task-evidence-lifecycle`
- **Editorial status**: `stable`
- **Provenance classification**: `locally_defined`
- **Source corpus**: Trust Infrastructure Glossary

## In Simple English
The sequence of evidence, receipts, artifacts, and review triggers associated with governance-significant task state transitions from initiation through completion, cancellation, or failure.

## Definition
The sequence of evidence, receipts, artifacts, and review triggers associated with governance-significant task state transitions from initiation through completion, cancellation, or failure.

## Reader Note
This term was added following a cross-repository terminology review of TSMM, TIS, TGA, and the DTG ZKP Task Force workspace.

## Implementation Relevance
Use this term to keep runtime governance, delegation, evidence, and privacy semantics consistent across interoperating trust infrastructure repositories.

## Alternative Designations
- **task-evidence-lifecycle** (`en`, `alternative`)

## Legacy Aliases
task evidence lifecycle, task-evidence-lifecycle

## Semantic Relations
- **related**: `urn:tig:concept:trust-task`
- **related**: `urn:tig:concept:audit-log`
- **related**: `urn:tig:concept:attestation`

## Cross-Vocabulary Mappings
Not specified

## See Also
- [trust-task]({{ '/terms/trust-task/' | relative_url }})
- [audit-log]({{ '/terms/audit-log/' | relative_url }})
- [attestation]({{ '/terms/attestation/' | relative_url }})

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
