---
title: "wallet-engine"
---

# wallet-engine

A simple-English summary has not yet been added for this concept.

## Formal definition
The set of software components that form the core of a digital wallet, but which by themselves are not sufficient to deliver a fully functional wallet for use by a digital agent (of a principal). A wallet engine is to a digital wallet what a browser engine is to a web browser.

## Why this concept matters
This concept is provided as a controlled glossary entry for standards, governance, and implementation review.

Use this concept consistently when mapping authority, evidence, reliance, and auditability across governance and implementation artifacts.

## Names and relationships

### Alternative designations
- **wallet engine** (`en`, `alternative`)
- **wallet engines** (`en`, `alternative`)

### Related concepts
- [delegation]({{ '/terms/delegation/' | relative_url }})
- [delegator]({{ '/terms/delegator/' | relative_url }})
- [delegatee]({{ '/terms/delegatee/' | relative_url }})
- [authorization]({{ '/terms/authorization/' | relative_url }})

### Semantic relations
- **related**: `urn:tig:concept:delegation`
- **related**: `urn:tig:concept:delegator`
- **related**: `urn:tig:concept:delegatee`
- **related**: `urn:tig:concept:authorization`

### Cross-vocabulary mappings
Not specified

## Provenance and identity
- **Concept ID**: `urn:tig:concept:wallet-engine`
- **Editorial status**: `stable`
- **Provenance classification**: `adapted`
- **Source corpus**: Trust over IP Main Glossary

### Standards and source references
- ToIP CTWG maintained glossary source: `spec/terms-definitions/wallet-engine.md`

<details markdown="1">
<summary><strong>Implementation and governance metadata</strong></summary>

### Legacy aliases
wallet engine, wallet engines

### Governance profile
- **Authority scope**: delegation_and_scope
- **Delegation mode**: direct_or_constrained
- **Revocation supported**: False
- **Lifecycle states**: documented, active, deprecated
- **Execution role**: runtime
- **Control-plane role**: decision_plane_component

### Enforcement points
- delegation_grant

### Assurance
**Evidence artifacts**
- delegation_record

- **Assurance level hint**: AL2+
- **Auditability**: high

### Control plane
**Decision points**
- delegation_grant

- **Accountable entity**: glossary_maintainers

**Evidence produced**
- delegation_record

### Notes
Not specified

### Supporting definitions
- For more information: The charter of the [[ref: OpenWallet Foundation]] is to produce an open source [[ref: digital wallet]] engine.

### Mental models
Not specified

### Crosswalk references
Not specified

</details>

---

*Generated from `glossary/terms/wallet-engine.yaml`. Edit the source concept and regenerate rather than editing this page directly.*
