---
title: "presentation"
---

# presentation

A simple-English summary has not yet been added for this concept.

## Formal definition
A verifiable message that a holder may send to a verifier containing proofs of one or more claims derived from one or more digital credentials from one or more issuers as a response to a specific presentation request from a  verifier.

## Why this concept matters
This concept is provided as a controlled glossary entry for standards, governance, and implementation review.

Use this concept consistently when mapping authority, evidence, reliance, and auditability across governance and implementation artifacts.

## Names and relationships

### Alternative designations
- **presentations** (`en`, `alternative`)
- **present** (`en`, `alternative`)
- **presents** (`en`, `alternative`)
- **presenting** (`en`, `alternative`)
- **presented** (`en`, `alternative`)

### Related concepts
- [credential]({{ '/terms/credential/' | relative_url }})
- [issuer]({{ '/terms/issuer/' | relative_url }})
- [issuance]({{ '/terms/issuance/' | relative_url }})
- [verifiable-credential]({{ '/terms/verifiable-credential/' | relative_url }})
- [verification]({{ '/terms/verification/' | relative_url }})
- [verifier]({{ '/terms/verifier/' | relative_url }})

### Semantic relations
- **related**: `urn:tig:concept:credential`
- **related**: `urn:tig:concept:issuer`
- **related**: `urn:tig:concept:issuance`
- **related**: `urn:tig:concept:verifiable-credential`
- **related**: `urn:tig:concept:verification`
- **related**: `urn:tig:concept:verifier`

### Cross-vocabulary mappings
Not specified

## Provenance and identity
- **Concept ID**: `urn:tig:concept:presentation`
- **Editorial status**: `stable`
- **Provenance classification**: `adapted`
- **Source corpus**: Trust over IP Main Glossary

### Standards and source references
- ToIP CTWG maintained glossary source: `spec/terms-definitions/presentation.md`

<details markdown="1">
<summary><strong>Implementation and governance metadata</strong></summary>

### Legacy aliases
presentation, presentations, present, presents, presenting, presented

### Governance profile
- **Authority scope**: credential_issuance, verification_and_reliance
- **Delegation mode**: direct
- **Revocation supported**: True
- **Lifecycle states**: proposed, active, suspended, revoked, retired
- **Execution role**: runtime
- **Control-plane role**: decision_plane_component

### Enforcement points
- reliance_decision
- issuance_decision
- revocation_decision

### Assurance
**Evidence artifacts**
- issuance_log
- verification_log

- **Assurance level hint**: AL2+
- **Auditability**: high

### Control plane
**Decision points**
- reliance_decision
- issuance_decision
- revocation_decision

- **Accountable entity**: issuer_operator

**Evidence produced**
- issuance_log
- verification_log

### Notes
Not specified

### Supporting definitions
- [eSSIF-Lab](https://essif-lab.github.io/framework/docs/terms/presentation): A (signed) digital [[ref: message]] that a [[ref: holder]] component may send to a [[ref: verifier]] component that contains [[ref: data]] derived from one or more [[ref: verifiable credentials]] (that (a [colleague](https://essif-lab.github.io/framework/docs/terms/colleague) component of) the [holder](https://essif-lab.github.io/framework/docs/terms/holder) component has received from [issuer](https://essif-lab.github.io/framework/docs/terms/issuer) components of one or more [parties](https://essif-lab.github.io/framework/docs/terms/party)), as a response to a specific [[ref: presentation request]] of a  [[ref: verifier ]]component.

### Mental models
Not specified

### Crosswalk references
Not specified

</details>

---

*Generated from `glossary/terms/presentation.yaml`. Edit the source concept and regenerate rather than editing this page directly.*
