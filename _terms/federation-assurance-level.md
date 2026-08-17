---
title: "federation-assurance-level"
---

# federation-assurance-level

A simple-English summary has not yet been added for this concept.

## Formal definition
A category that describes the federation protocol used to communicate an assertion containing authentication) and attribute information (if applicable) to a relying party, as defined in NIST SP 800-63-3 in terms of three levels: FAL 1 (Some confidence), FAL 2 (High confidence), FAL 3 (Very high confidence).

## Why this concept matters
This concept is provided as a controlled glossary entry for standards, governance, and implementation review.

Use this concept consistently when mapping authority, evidence, reliance, and auditability across governance and implementation artifacts.

## Names and relationships

### Alternative designations
- **federation assurance level** (`en`, `alternative`)
- **federation assurance levels** (`en`, `alternative`)
- **FAL** (`en`, `alternative`)
- **FALs** (`en`, `alternative`)

### Related concepts
- [authenticator assurance level]({{ '/terms/authenticator-assurance-level/' | relative_url }})
- [identity assurance level]({{ '/terms/identity-assurance-level/' | relative_url }})

### Semantic relations
- **related**: `urn:tig:concept:authenticator-assurance-level`
- **related**: `urn:tig:concept:identity-assurance-level`

### Cross-vocabulary mappings
Not specified

## Provenance and identity
- **Concept ID**: `urn:tig:concept:federation-assurance-level`
- **Editorial status**: `stable`
- **Provenance classification**: `locally_defined`
- **Source corpus**: Trust Infrastructure Glossary

### Standards and source references
- [NIST-CSRC](https://csrc.nist.gov/glossary/term/federation_assurance_level).

<details markdown="1">
<summary><strong>Implementation and governance metadata</strong></summary>

### Legacy aliases
federation assurance level, federation assurance levels, FAL, FALs

### Governance profile
- **Authority scope**: verification_and_reliance, access_decisioning, assurance_and_audit
- **Delegation mode**: direct
- **Revocation supported**: False
- **Lifecycle states**: documented, active, deprecated
- **Execution role**: runtime
- **Control-plane role**: decision_plane_component

### Enforcement points
- reliance_decision
- access_decision

### Assurance
**Evidence artifacts**
- verification_log
- attestation
- access_decision_log

- **Assurance level hint**: AL2+
- **Auditability**: high

### Control plane
**Decision points**
- reliance_decision
- access_decision

- **Accountable entity**: glossary_maintainers

**Evidence produced**
- verification_log
- attestation
- access_decision_log

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

*Generated from `glossary/terms/federation-assurance-level.yaml`. Edit the source concept and regenerate rather than editing this page directly.*
