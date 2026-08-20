---
title: "evidence"
---

# evidence

Material that can be examined to decide whether a claim, control, or conclusion is supported.

## Formal definition
Information, records, observations, attestations, or other artifacts used to support, challenge, or evaluate a claim, control, requirement, decision, or assurance conclusion.

## Why this concept matters
This concept is provided as a controlled glossary entry for standards, governance, and implementation review.

Use this concept consistently when mapping authority, evidence, reliance, and auditability across governance and implementation artifacts.

## Names and relationships

### Alternative designations
None

### Related concepts
- [claim]({{ '/terms/claim/' | relative_url }})
- [attestation]({{ '/terms/attestation/' | relative_url }})
- [audit]({{ '/terms/audit/' | relative_url }})
- [proof]({{ '/terms/proof/' | relative_url }})

### Semantic relations
- **related**: `urn:tig:concept:claim`
- **related**: `urn:tig:concept:attestation`
- **related**: `urn:tig:concept:audit`
- **related**: `urn:tig:concept:proof`

### Cross-vocabulary mappings
Not specified

## Provenance and identity
- **Concept ID**: `urn:tig:concept:evidence`
- **Editorial status**: `proposed`
- **Provenance classification**: `locally_defined`
- **Source corpus**: Cross-repository trust infrastructure portfolio

### Standards and source references
- https://github.com/sankarshanmukhopadhyay/trust-systems-meta-model
- https://github.com/sankarshanmukhopadhyay/trust-infrastructure-schemas
- https://github.com/sankarshanmukhopadhyay/governance-authority-assurance-metamodel
- https://github.com/sankarshanmukhopadhyay/rahp-toolkit

<details markdown="1">
<summary><strong>Implementation and governance metadata</strong></summary>

### Legacy aliases
evidence

### Governance profile
- **Authority scope**: assurance_and_audit, verification_and_reliance
- **Delegation mode**: direct
- **Revocation supported**: False
- **Lifecycle states**: documented, active, retired
- **Execution role**: hybrid
- **Control-plane role**: reference_term

### Enforcement points
- reliance_decision

### Assurance
**Evidence artifacts**
- attestation
- audit_log
- verification_log

- **Assurance level hint**: AL1+
- **Auditability**: high

### Control plane
**Decision points**
- reliance_decision

- **Accountable entity**: evidence_producer

**Evidence produced**
- attestation
- audit_log
- verification_log

### Notes
- Evidence is not equivalent to a conclusion. Its relevance, integrity, provenance, freshness, and sufficiency must be evaluated in context.

### Supporting definitions
Not specified

### Mental models
Not specified

### Crosswalk references
Not specified

</details>

---

*Generated from `glossary/terms/evidence.yaml`. Edit the source concept and regenerate rather than editing this page directly.*
