---
title: "pid"
---

# pid

A simple-English summary has not yet been added for this concept.

## Formal definition
A set of identity attributes used in the EUDI Wallet ecosystem to identify a natural or legal person under the applicable legal and governance framework.

## Why this concept matters
This term is part of the v1.2.0 standards-linked refresh and is anchored to active implementation vocabulary.

Use this term when mapping glossary language to implementation profiles, governance controls, conformance checks, or assurance evidence.

## Names and relationships

### Alternative designations
- **Person Identification Data** (`en`, `alternative`)
- **PID** (`en`, `alternative`)

### Related concepts
- [eudi-wallet]({{ '/terms/eudi-wallet/' | relative_url }})
- [identity-data]({{ '/terms/identity-data/' | relative_url }})
- [natural-person]({{ '/terms/natural-person/' | relative_url }})
- [legal-person]({{ '/terms/legal-person/' | relative_url }})

### Semantic relations
- **related**: `urn:tig:concept:eudi-wallet`
- **related**: `urn:tig:concept:identity-data`
- **related**: `urn:tig:concept:natural-person`
- **related**: `urn:tig:concept:legal-person`

### Cross-vocabulary mappings
Not specified

## Provenance and identity
- **Concept ID**: `urn:tig:concept:pid`
- **Editorial status**: `stable`
- **Provenance classification**: `locally_defined`
- **Source corpus**: Trust Infrastructure Glossary

### Standards and source references
- [EUDI Wallet Architecture and Reference Framework 2.0](https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework) (European Commission; Architecture Reference Framework; 2.0; 2025-05-29) — normative

<details markdown="1">
<summary><strong>Implementation and governance metadata</strong></summary>

### Legacy aliases
Person Identification Data, PID

### Governance profile
- **Authority scope**: credential_issuance, verification_and_reliance
- **Delegation mode**: direct
- **Revocation supported**: True
- **Lifecycle states**: proposed, active, suspended, revoked, retired
- **Execution role**: hybrid
- **Control-plane role**: decision_plane_component

### Enforcement points
- issuance_decision
- reliance_decision

### Assurance
**Evidence artifacts**
- issuance_log
- verification_log
- policy_document
- audit_log

- **Assurance level hint**: AL2+
- **Auditability**: high

### Control plane
**Decision points**
- issuance_decision
- reliance_decision

- **Accountable entity**: glossary_maintainers

**Evidence produced**
- issuance_log
- verification_log
- policy_document
- audit_log

### Notes
Not specified

### Supporting definitions
Not specified

### Mental models
Not specified

### Crosswalk references
- **EU**: EUDI ARF 2.0

</details>

---

*Generated from `glossary/terms/pid.yaml`. Edit the source concept and regenerate rather than editing this page directly.*
