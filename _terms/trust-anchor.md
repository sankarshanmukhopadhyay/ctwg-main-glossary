---
title: "trust-anchor"
---

# trust-anchor

The authoritative source that serves as the origin of a trust chain.

## Formal definition
The authoritative source that serves as the origin of a trust chain.

## Why this concept matters
This concept is provided as a controlled glossary entry for standards, governance, and implementation review.

Use this concept consistently when mapping authority, evidence, reliance, and auditability across governance and implementation artifacts.

## Names and relationships

### Alternative designations
- **trust anchor** (`en`, `alternative`)
- **trust anchors** (`en`, `alternative`)

### Related concepts
- [governance]({{ '/terms/governance/' | relative_url }})
- [governance-framework]({{ '/terms/governance-framework/' | relative_url }})
- [governing-authority]({{ '/terms/governing-authority/' | relative_url }})
- [trust-registry]({{ '/terms/trust-registry/' | relative_url }})
- [definition]({{ '/terms/definition/' | relative_url }})
- [glossary]({{ '/terms/glossary/' | relative_url }})

### Semantic relations
- **related**: `urn:tig:concept:governance`
- **related**: `urn:tig:concept:governance-framework`
- **related**: `urn:tig:concept:governing-authority`
- **related**: `urn:tig:concept:trust-registry`
- **related**: `urn:tig:concept:definition`
- **related**: `urn:tig:concept:glossary`

### Cross-vocabulary mappings
Not specified

## Provenance and identity
- **Concept ID**: `urn:tig:concept:trust-anchor`
- **Editorial status**: `stable`
- **Provenance classification**: `adapted`
- **Source corpus**: Trust over IP Main Glossary

### Standards and source references
- ToIP CTWG maintained glossary source: `spec/terms-definitions/trust-anchor.md`

<details markdown="1">
<summary><strong>Implementation and governance metadata</strong></summary>

### Legacy aliases
trust anchor, trust anchors

### Governance profile
- **Authority scope**: governance_recognition
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

- **Assurance level hint**: AL1+
- **Auditability**: moderate

### Control plane
**Decision points**
- definition_approval

- **Accountable entity**: glossary_maintainers

**Evidence produced**
- definition_change_record
- policy_document
- audit_log

### Notes
- The term “trust anchor” is most commonly used in cryptography and public key infrastructure.

### Supporting definitions
- Also known as: [[ref: trust root]].
- For more information, see: [Design Principles for the ToIP Stack](https://trustoverip.org/our-work/design-principles/).

### Mental models
Not specified

### Crosswalk references
Not specified

</details>

---

*Generated from `glossary/terms/trust-anchor.yaml`. Edit the source concept and regenerate rather than editing this page directly.*
