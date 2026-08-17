---
title: "issuance"
---

# issuance

The action of an issuer producing and transmitting a digital credential to a holder. A holder may request issuance by submitting an issuance request.

## Formal definition
The action of an issuer producing and transmitting a digital credential to a holder. A holder may request issuance by submitting an issuance request.

## Why this concept matters
This concept is provided as a controlled glossary entry for standards, governance, and implementation review.

Use this concept consistently when mapping authority, evidence, reliance, and auditability across governance and implementation artifacts.

## Names and relationships

### Alternative designations
- **issue** (`en`, `alternative`)
- **issues** (`en`, `alternative`)
- **issued** (`en`, `alternative`)
- **issuing** (`en`, `alternative`)

### Related concepts
- [presentation]({{ '/terms/presentation/' | relative_url }})
- [revocation]({{ '/terms/revocation/' | relative_url }})

### Semantic relations
- **related**: `urn:tig:concept:presentation`
- **related**: `urn:tig:concept:revocation`

### Cross-vocabulary mappings
Not specified

## Provenance and identity
- **Concept ID**: `urn:tig:concept:issuance`
- **Editorial status**: `stable`
- **Provenance classification**: `adapted`
- **Source corpus**: Trust over IP Main Glossary

### Standards and source references
- ToIP CTWG maintained glossary source: `spec/terms-definitions/issuance.md`

<details markdown="1">
<summary><strong>Implementation and governance metadata</strong></summary>

### Legacy aliases
issuance, issue, issues, issued, issuing

### Governance profile
- **Authority scope**: credential_issuance
- **Delegation mode**: direct
- **Revocation supported**: True
- **Lifecycle states**: proposed, active, suspended, revoked, retired
- **Execution role**: runtime
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

- **Accountable entity**: issuer_operator

**Evidence produced**
- issuance_log
- registry_entry
- status_record
- audit_log
- verification_log

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

*Generated from `glossary/terms/issuance.yaml`. Edit the source concept and regenerate rather than editing this page directly.*
