---
title: "digital-vault"
---

# digital-vault

A simple-English summary has not yet been added for this concept.

## Formal definition
A secure container for data whose controller is the principal. A digital vault is most commonly used in conjunction with a digital wallet and a digital agent. A digital vault may be implemented on a local device or in the cloud; multiple digital vaults may be used by the same principal across different devices and/or the cloud; if so they may use some type of synchronization. If the capability is supported, data may flow into or out of the digital vault automatically based on subscriptions approved by the controller.

## Why this concept matters
This concept is provided as a controlled glossary entry for standards, governance, and implementation review.

Use this concept consistently when mapping authority, evidence, reliance, and auditability across governance and implementation artifacts.

## Names and relationships

### Alternative designations
- **digital vault** (`en`, `alternative`)
- **digital vaults** (`en`, `alternative`)

### Related concepts
- [enterprise data vault]({{ '/terms/enterprise-data-vault/' | relative_url }})
- [personal data vault]({{ '/terms/personal-data-vault/' | relative_url }})
- [virtual vault]({{ '/terms/virtual-vault/' | relative_url }})

### Semantic relations
- **related**: `urn:tig:concept:enterprise-data-vault`
- **related**: `urn:tig:concept:personal-data-vault`
- **related**: `urn:tig:concept:virtual-vault`

### Cross-vocabulary mappings
Not specified

## Provenance and identity
- **Concept ID**: `urn:tig:concept:digital-vault`
- **Editorial status**: `stable`
- **Provenance classification**: `adapted`
- **Source corpus**: Trust over IP Main Glossary

### Standards and source references
- ToIP CTWG maintained glossary source: `spec/terms-definitions/digital-vault.md`

<details markdown="1">
<summary><strong>Implementation and governance metadata</strong></summary>

### Legacy aliases
digital vault, digital vaults

### Governance profile
- **Authority scope**: delegation_and_scope, access_decisioning
- **Delegation mode**: direct_or_constrained
- **Revocation supported**: False
- **Lifecycle states**: documented, active, deprecated
- **Execution role**: runtime
- **Control-plane role**: decision_plane_component

### Enforcement points
- delegation_grant
- access_decision

### Assurance
**Evidence artifacts**
- delegation_record
- access_decision_log

- **Assurance level hint**: AL2+
- **Auditability**: high

### Control plane
**Decision points**
- delegation_grant
- access_decision

- **Accountable entity**: glossary_maintainers

**Evidence produced**
- delegation_record
- access_decision_log

### Notes
Not specified

### Supporting definitions
- Also known as: [[ref: data vault]], [[ref: encrypted data vault]].
- For more information, see: <https://en.wikipedia.org/wiki/Personal_data_service>, <https://digitalbazaar.github.io/encrypted-data-vaults/>

### Mental models
Not specified

### Crosswalk references
Not specified

</details>

---

*Generated from `glossary/terms/digital-vault.yaml`. Edit the source concept and regenerate rather than editing this page directly.*
