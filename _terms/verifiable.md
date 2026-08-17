---
title: "verifiable"
---

# verifiable

A simple-English summary has not yet been added for this concept.

## Formal definition
In the context of digital communications infrastructure, the ability to determine the authenticity of a communication (e.g., sender, contents, claims, metadata, provenance), or the underlying sociotechnical infrastructure (e.g., governance, roles, policies, authorizations, certifications).

## Why this concept matters
This concept is provided as a controlled glossary entry for standards, governance, and implementation review.

Use this concept consistently when mapping authority, evidence, reliance, and auditability across governance and implementation artifacts.

## Names and relationships

### Alternative designations
- **verifiability** (`en`, `alternative`)

### Related concepts
- [appraisable]({{ '/terms/appraisability/' | relative_url }})
- [digital signature]({{ '/terms/digital-signature/' | relative_url }})

### Semantic relations
- **related**: `urn:tig:concept:appraisable`
- **related**: `urn:tig:concept:digital-signature`

### Cross-vocabulary mappings
Not specified

## Provenance and identity
- **Concept ID**: `urn:tig:concept:verifiable`
- **Editorial status**: `stable`
- **Provenance classification**: `adapted`
- **Source corpus**: Trust over IP Main Glossary

### Standards and source references
- ToIP CTWG maintained glossary source: `spec/terms-definitions/verifiable.md`

<details markdown="1">
<summary><strong>Implementation and governance metadata</strong></summary>

### Legacy aliases
verifiable, verifiability

### Governance profile
- **Authority scope**: credential_issuance, access_decisioning, governance_recognition
- **Delegation mode**: direct
- **Revocation supported**: True
- **Lifecycle states**: proposed, active, suspended, revoked, retired
- **Execution role**: runtime
- **Control-plane role**: decision_plane_component

### Enforcement points
- issuance_decision
- access_decision
- revocation_decision

### Assurance
**Evidence artifacts**
- issuance_log
- access_decision_log
- policy_document
- registry_entry
- status_record
- audit_log
- verification_log

- **Assurance level hint**: AL2+
- **Auditability**: high

### Control plane
**Decision points**
- issuance_decision
- access_decision
- revocation_decision

- **Accountable entity**: governance_authority

**Evidence produced**
- issuance_log
- access_decision_log
- policy_document
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

*Generated from `glossary/terms/verifiable.yaml`. Edit the source concept and regenerate rather than editing this page directly.*
