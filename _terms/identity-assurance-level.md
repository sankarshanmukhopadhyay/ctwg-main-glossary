---
title: "identity-assurance-level"
---

# identity-assurance-level

A simple-English summary has not yet been added for this concept.

## Formal definition
A category that conveys the degree of confidence that a person’s claimed identity is their real identity, for example as defined in NIST SP 800-63-3 in terms of three levels: IAL 1 (Some confidence), IAL 2 (High confidence), IAL 3 (Very high confidence).

## Why this concept matters
This concept is provided as a controlled glossary entry for standards, governance, and implementation review.

Use this concept consistently when mapping authority, evidence, reliance, and auditability across governance and implementation artifacts.

## Names and relationships

### Alternative designations
- **identity assurance level** (`en`, `alternative`)
- **identity assurance levels** (`en`, `alternative`)
- **IAL** (`en`, `alternative`)
- **IALs** (`en`, `alternative`)

### Related concepts
- [authenticator assurance level]({{ '/terms/authenticator-assurance-level/' | relative_url }})
- [federation assurance level]({{ '/terms/federation-assurance-level/' | relative_url }})

### Semantic relations
- **related**: `urn:tig:concept:authenticator-assurance-level`
- **related**: `urn:tig:concept:federation-assurance-level`

### Cross-vocabulary mappings
Not specified

## Provenance and identity
- **Concept ID**: `urn:tig:concept:identity-assurance-level`
- **Editorial status**: `stable`
- **Provenance classification**: `locally_defined`
- **Source corpus**: Trust Infrastructure Glossary

### Standards and source references
- [NIST-CSRC](https://csrc.nist.gov/glossary/term/identity_assurance_level).

<details markdown="1">
<summary><strong>Implementation and governance metadata</strong></summary>

### Legacy aliases
identity assurance level, identity assurance levels, IAL, IALs

### Governance profile
- **Authority scope**: credential_issuance, assurance_and_audit
- **Delegation mode**: direct
- **Revocation supported**: False
- **Lifecycle states**: documented, active, deprecated
- **Execution role**: design
- **Control-plane role**: decision_plane_component

### Enforcement points
- issuance_decision

### Assurance
**Evidence artifacts**
- issuance_log
- attestation

- **Assurance level hint**: AL1+
- **Auditability**: moderate

### Control plane
**Decision points**
- issuance_decision

- **Accountable entity**: glossary_maintainers

**Evidence produced**
- issuance_log
- attestation

### Notes
Not specified

### Supporting definitions
Not specified

### Mental models
Not specified

### Crosswalk references
Not specified

</details>

---

*Generated from `glossary/terms/identity-assurance-level.yaml`. Edit the source concept and regenerate rather than editing this page directly.*
