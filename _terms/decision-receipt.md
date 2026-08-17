---
title: "decision receipt"
---

# decision receipt

A record that explains what decision was made, under whose authority, using which policy and evidence, and with what result.

## Formal definition
A structured, integrity-protected record of a trust or governance decision, including the decision context, authority, policy, evidence, outcome, obligations, and traceability data.

## Why this concept matters
This term was added following a cross-repository terminology review of TSMM, TIS, TGA, and the DTG ZKP Task Force workspace.

Use this term to keep runtime governance, delegation, evidence, and privacy semantics consistent across interoperating trust infrastructure repositories.

## Names and relationships

### Alternative designations
- **decision-receipt** (`en`, `alternative`)

### Related concepts
- [trust-decision]({{ '/terms/trust-decision/' | relative_url }})
- [audit-log]({{ '/terms/audit-log/' | relative_url }})
- [attestation]({{ '/terms/attestation/' | relative_url }})

### Semantic relations
- **related**: `urn:tig:concept:trust-decision`
- **related**: `urn:tig:concept:audit-log`
- **related**: `urn:tig:concept:attestation`

### Cross-vocabulary mappings
Not specified

## Provenance and identity
- **Concept ID**: `urn:tig:concept:decision-receipt`
- **Editorial status**: `stable`
- **Provenance classification**: `locally_defined`
- **Source corpus**: Trust Infrastructure Glossary

### Standards and source references
- [TIS repository terminology and model documentation](https://github.com/sankarshanmukhopadhyay/trust-infrastructure-schemas) (GitHub) — informative
- [TGA repository terminology and model documentation](https://github.com/sankarshanmukhopadhyay/trust-graph-artifacts) (GitHub) — informative

<details markdown="1">
<summary><strong>Implementation and governance metadata</strong></summary>

### Legacy aliases
decision receipt, decision-receipt

### Governance profile
- **Authority scope**: assurance_and_audit, delegation_and_scope, policy_definition, verification_and_reliance
- **Delegation mode**: direct_or_constrained
- **Revocation supported**: True
- **Lifecycle states**: proposed, active, suspended, revoked, retired
- **Execution role**: hybrid
- **Control-plane role**: decision_plane_component

### Enforcement points
- policy_approval
- delegation_grant
- reliance_decision
- revocation_decision

### Assurance
**Evidence artifacts**
- policy_document
- delegation_record
- status_record
- verification_log

- **Assurance level hint**: AL2+
- **Auditability**: high

### Control plane
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

### Notes
- This definition is normalized for cross-repository use and should be applied together with the governing profile or specification that supplies domain-specific constraints.

### Supporting definitions
Not specified

### Mental models
Not specified

### Crosswalk references
Not specified

</details>

---

*Generated from `glossary/terms/decision-receipt.yaml`. Edit the source concept and regenerate rather than editing this page directly.*
