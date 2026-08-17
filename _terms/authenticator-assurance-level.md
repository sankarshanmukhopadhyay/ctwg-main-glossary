---
title: "authenticator-assurance-level"
---

# authenticator-assurance-level

A measure of the strength of an authentication mechanism and, therefore, the confidence in it.

## Formal definition
A measure of the strength of an authentication mechanism and, therefore, the confidence in it.

## Why this concept matters
This concept is provided as a controlled glossary entry for standards, governance, and implementation review.

Use this concept consistently when mapping authority, evidence, reliance, and auditability across governance and implementation artifacts.

## Names and relationships

### Alternative designations
- **authenticator assurance level** (`en`, `alternative`)
- **authenticator assurance levels** (`en`, `alternative`)
- **AAL** (`en`, `alternative`)
- **AALs** (`en`, `alternative`)

### Related concepts
- [federation assurance level]({{ '/terms/federation-assurance-level/' | relative_url }})
- [identity assurance level]({{ '/terms/identity-assurance-level/' | relative_url }})
- [identity binding]({{ '/terms/identity-binding/' | relative_url }})

### Semantic relations
- **related**: `urn:tig:concept:federation-assurance-level`
- **related**: `urn:tig:concept:identity-assurance-level`
- **related**: `urn:tig:concept:identity-binding`

### Cross-vocabulary mappings
Not specified

## Provenance and identity
- **Concept ID**: `urn:tig:concept:authenticator-assurance-level`
- **Editorial status**: `stable`
- **Provenance classification**: `locally_defined`
- **Source corpus**: Trust Infrastructure Glossary

### Standards and source references
- [NIST-CSRC](https://csrc.nist.gov/glossary/term/authenticator_assurance_level).

<details markdown="1">
<summary><strong>Implementation and governance metadata</strong></summary>

### Legacy aliases
authenticator assurance level, authenticator assurance levels, AAL, AALs

### Governance profile
- **Authority scope**: access_decisioning, assurance_and_audit
- **Delegation mode**: direct
- **Revocation supported**: False
- **Lifecycle states**: documented, active, deprecated
- **Execution role**: runtime
- **Control-plane role**: decision_plane_component

### Enforcement points
- access_decision

### Assurance
**Evidence artifacts**
- attestation
- access_decision_log

- **Assurance level hint**: AL2+
- **Auditability**: high

### Control plane
**Decision points**
- access_decision

- **Accountable entity**: glossary_maintainers

**Evidence produced**
- attestation
- access_decision_log

### Notes
- In NIST SP 800-63-3, AAL is defined in terms of three levels: AAL1 (Some confidence), AAL2 (High confidence), AAL3 (Very high confidence).

### Supporting definitions
- Also known as: [[ref: AAL]]

### Mental models
Not specified

### Crosswalk references
Not specified

</details>

---

*Generated from `glossary/terms/authenticator-assurance-level.yaml`. Edit the source concept and regenerate rather than editing this page directly.*
