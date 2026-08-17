---
title: "trusted-execution-environment"
---

# trusted-execution-environment

A simple-English summary has not yet been added for this concept.

## Formal definition
A trusted execution environment (TEE) is a secure area of a main processor. It helps code and data loaded inside it to be protected with respect to confidentiality and integrity. Data integrity prevents unauthorized entities from outside the TEE from altering data, while code integrity prevents code in the TEE from being replaced or modified by unauthorized entities, which may also be the computer owner itself as in certain DRM schemes.

## Why this concept matters
This concept is provided as a controlled glossary entry for standards, governance, and implementation review.

Use this concept consistently when mapping authority, evidence, reliance, and auditability across governance and implementation artifacts.

## Names and relationships

### Alternative designations
- **trusted execution environment** (`en`, `alternative`)
- **trusted execution environments** (`en`, `alternative`)
- **TEE** (`en`, `alternative`)
- **TEEs** (`en`, `alternative`)

### Related concepts
- [Secure Enclave]({{ '/terms/secure-enclave/' | relative_url }})

### Semantic relations
- **related**: `urn:tig:concept:secure-enclave`

### Cross-vocabulary mappings
Not specified

## Provenance and identity
- **Concept ID**: `urn:tig:concept:trusted-execution-environment`
- **Editorial status**: `stable`
- **Provenance classification**: `locally_defined`
- **Source corpus**: Trust Infrastructure Glossary

### Standards and source references
- [Wikipedia](https://en.wikipedia.org/wiki/Trusted_execution_environment).

<details markdown="1">
<summary><strong>Implementation and governance metadata</strong></summary>

### Legacy aliases
trusted execution environment, trusted execution environments, TEE, TEEs

### Governance profile
- **Authority scope**: terminology_definition
- **Delegation mode**: direct
- **Revocation supported**: False
- **Lifecycle states**: documented, active, deprecated
- **Execution role**: design
- **Control-plane role**: decision_plane_component

### Enforcement points
- definition_approval

### Assurance
**Evidence artifacts**
- definition_change_record
- policy_document
- audit_log

- **Assurance level hint**: AL2+
- **Auditability**: high

### Control plane
**Decision points**
- definition_approval

- **Accountable entity**: glossary_maintainers

**Evidence produced**
- definition_change_record
- policy_document
- audit_log

### Notes
Not specified

### Supporting definitions
- Also known as: [[ref: TEE]].

### Mental models
Not specified

### Crosswalk references
Not specified

</details>

---

*Generated from `glossary/terms/trusted-execution-environment.yaml`. Edit the source concept and regenerate rather than editing this page directly.*
