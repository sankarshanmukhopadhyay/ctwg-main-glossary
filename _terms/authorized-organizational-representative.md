---
title: "authorized-organizational-representative"
---

# authorized-organizational-representative

A person who has the authority to make claims, sign documents or otherwise commit resources on behalf of an organization.

## Formal definition
A person who has the authority to make claims, sign documents or otherwise commit resources on behalf of an organization.

## Why this concept matters
This concept is provided as a controlled glossary entry for standards, governance, and implementation review.

Use this concept consistently when mapping authority, evidence, reliance, and auditability across governance and implementation artifacts.

## Names and relationships

### Alternative designations
- **authorized organizational representative** (`en`, `alternative`)

### Related concepts
- [credential]({{ '/terms/credential/' | relative_url }})
- [issuer]({{ '/terms/issuer/' | relative_url }})
- [issuance]({{ '/terms/issuance/' | relative_url }})
- [verifiable-credential]({{ '/terms/verifiable-credential/' | relative_url }})
- [delegation]({{ '/terms/delegation/' | relative_url }})
- [delegator]({{ '/terms/delegator/' | relative_url }})

### Semantic relations
- **related**: `urn:tig:concept:credential`
- **related**: `urn:tig:concept:issuer`
- **related**: `urn:tig:concept:issuance`
- **related**: `urn:tig:concept:verifiable-credential`
- **related**: `urn:tig:concept:delegation`
- **related**: `urn:tig:concept:delegator`

### Cross-vocabulary mappings
Not specified

## Provenance and identity
- **Concept ID**: `urn:tig:concept:authorized-organizational-representative`
- **Editorial status**: `stable`
- **Provenance classification**: `locally_defined`
- **Source corpus**: Trust Infrastructure Glossary

### Standards and source references
- [Law Insider](https://www.lawinsider.com/dictionary/authorized-organizational-representative#:~:text=Authorized%20Organizational%20Representative%20means%20the,the%20resources%20of%20the%20organization.)

<details markdown="1">
<summary><strong>Implementation and governance metadata</strong></summary>

### Legacy aliases
authorized organizational representative

### Governance profile
- **Authority scope**: credential_issuance, delegation_and_scope, governance_recognition
- **Delegation mode**: direct_or_constrained
- **Revocation supported**: True
- **Lifecycle states**: proposed, active, suspended, revoked, retired
- **Execution role**: runtime
- **Control-plane role**: decision_plane_component

### Enforcement points
- delegation_grant
- issuance_decision
- revocation_decision

### Assurance
**Evidence artifacts**
- delegation_record
- issuance_log
- policy_document
- registry_entry
- status_record
- audit_log
- verification_log

- **Assurance level hint**: AL2+
- **Auditability**: high

### Control plane
**Decision points**
- delegation_grant
- issuance_decision
- revocation_decision

- **Accountable entity**: governance_authority

**Evidence produced**
- delegation_record
- issuance_log
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

*Generated from `glossary/terms/authorized-organizational-representative.yaml`. Edit the source concept and regenerate rather than editing this page directly.*
