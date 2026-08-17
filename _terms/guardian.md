---
title: "guardian"
---

# guardian

A simple-English summary has not yet been added for this concept.

## Formal definition
A party that has been assigned rights and duties in a guardianship arrangement for the purpose of caring for, protecting, guarding, and defending the entity that is the dependent in that guardianship arrangement. In the context of decentralized digital trust infrastructure, a guardian is issued guardianship credentials into their own digital wallet in order to perform such actions on behalf of the dependent as are required by this role.

## Why this concept matters
This concept is provided as a controlled glossary entry for standards, governance, and implementation review.

Use this concept consistently when mapping authority, evidence, reliance, and auditability across governance and implementation artifacts.

## Names and relationships

### Alternative designations
- **guardians** (`en`, `alternative`)

### Related concepts
- [custodian]({{ '/terms/custodian/' | relative_url }})
- [zero-knowledge service provider]({{ '/terms/zero-knowledge-service-provider/' | relative_url }})

### Semantic relations
- **related**: `urn:tig:concept:custodian`
- **related**: `urn:tig:concept:zero-knowledge-service-provider`

### Cross-vocabulary mappings
Not specified

## Provenance and identity
- **Concept ID**: `urn:tig:concept:guardian`
- **Editorial status**: `stable`
- **Provenance classification**: `locally_defined`
- **Source corpus**: Trust Infrastructure Glossary

### Standards and source references
- [eSSIF-Lab](https://essif-lab.github.io/framework/docs/essifLab-glossary#guardian)

<details markdown="1">
<summary><strong>Implementation and governance metadata</strong></summary>

### Legacy aliases
guardian, guardians

### Governance profile
- **Authority scope**: credential_issuance
- **Delegation mode**: direct
- **Revocation supported**: True
- **Lifecycle states**: proposed, active, suspended, revoked, retired
- **Execution role**: design
- **Control-plane role**: decision_plane_component

### Enforcement points
- issuance_decision
- revocation_decision

### Assurance
**Evidence artifacts**
- issuance_log
- registry_entry
- status_record
- audit_log
- verification_log

- **Assurance level hint**: AL2+
- **Auditability**: high

### Control plane
**Decision points**
- issuance_decision
- revocation_decision

- **Accountable entity**: glossary_maintainers

**Evidence produced**
- issuance_log
- registry_entry
- status_record
- audit_log
- verification_log

### Notes
- A guardian is a very different role than a custodian, who does not take any actions on behalf of a principal unless explicitly authorized.

### Supporting definitions
- [Wikipedia](https://en.wikipedia.org/wiki/Legal_guardian): A legal guardian is a person who has been appointed by a court or otherwise has the legal authority (and the corresponding [duty](https://en.wikipedia.org/wiki/Duty)) to make decisions relevant to the personal and [property](https://en.wikipedia.org/wiki/Property) interests of another person who is deemed incompetent, called a [ward](https://en.wikipedia.org/wiki/Ward_\(law\)).
- For more information, see: [On Guardianship in Self-Sovereign Identity V2.0](https://sovrin.org/wp-content/uploads/Guardianship-Whitepaper-V2.0.pdf) (April, 2023).

### Mental models
- [eSSIF-Lab Guardianship](https://essif-lab.github.io/framework/docs/terms/pattern-guardianship)

### Crosswalk references
Not specified

</details>

---

*Generated from `glossary/terms/guardian.yaml`. Edit the source concept and regenerate rather than editing this page directly.*
