---
title: "authorization"
---

# authorization

A simple-English summary has not yet been added for this concept.

## Formal definition
The process of determining whether a requested action or service is approved for a specific entity under applicable policies, rules, credentials, or other governing criteria.

## Why this concept matters
This concept is provided as a controlled glossary entry for standards, governance, and implementation review.

Use this concept consistently when mapping authority, evidence, reliance, and auditability across governance and implementation artifacts.

## Names and relationships

### Alternative designations
- **authorizations** (`en`, `alternative`)
- **authorize** (`en`, `alternative`)
- **authorized** (`en`, `alternative`)
- **unauthorized** (`en`, `alternative`)
- **authorizing** (`en`, `alternative`)
- **unauthorizing** (`en`, `alternative`)
- **authorisation** (`en`, `alternative`)
- **authorisations** (`en`, `alternative`)
- **authorise** (`en`, `alternative`)
- **authorised** (`en`, `alternative`)
- **unauthorised** (`en`, `alternative`)
- **authorising** (`en`, `alternative`)
- **unauthorising** (`en`, `alternative`)

### Related concepts
- [permission]({{ '/terms/permission/' | relative_url }})

### Semantic relations
- **related**: `urn:tig:concept:permission`

### Cross-vocabulary mappings
Not specified

## Provenance and identity
- **Concept ID**: `urn:tig:concept:authorization`
- **Editorial status**: `stable`
- **Provenance classification**: `locally_defined`
- **Source corpus**: Trust Infrastructure Glossary

### Standards and source references
- [NIST-CSRC](https://csrc.nist.gov/glossary/term/authorization).

<details markdown="1">
<summary><strong>Implementation and governance metadata</strong></summary>

### Legacy aliases
authorization, authorizations, authorize, authorized, unauthorized, authorizing, unauthorizing, authorisation, authorisations, authorise, authorised, unauthorised, authorising, unauthorising

### Governance profile
- **Authority scope**: credential_issuance, policy_definition, access_decisioning
- **Delegation mode**: direct
- **Revocation supported**: True
- **Lifecycle states**: proposed, active, suspended, revoked, retired
- **Execution role**: runtime
- **Control-plane role**: decision_plane_component

### Enforcement points
- policy_approval
- issuance_decision
- access_decision
- revocation_decision

### Assurance
**Evidence artifacts**
- policy_document
- issuance_log
- access_decision_log
- registry_entry
- audit_log
- status_record
- verification_log

- **Assurance level hint**: AL2+
- **Auditability**: high

### Control plane
**Decision points**
- policy_approval
- issuance_decision
- access_decision
- revocation_decision

- **Accountable entity**: glossary_maintainers

**Evidence produced**
- policy_document
- issuance_log
- access_decision_log
- registry_entry
- audit_log
- status_record
- verification_log

### Notes
Not specified

### Supporting definitions
Not specified

### Mental models
Not specified

### Crosswalk references
- **NIST**: AC-2, AC-3
- **ISO**: ISO/IEC 27001 A.5.15, ISO/IEC 42001 8.2

</details>

---

*Generated from `glossary/terms/authorization.yaml`. Edit the source concept and regenerate rather than editing this page directly.*
