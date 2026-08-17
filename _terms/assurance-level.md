---
title: "assurance-level"
---

# assurance-level

A stated level of confidence supported by defined evidence, controls, and review expectations.

## Formal definition
A level of confidence in a claim that may be relied on by others. Different types of assurance levels are defined for different types of trust assurance mechanisms. Examples include authenticator assurance level, federation assurance level, and identity assurance level.

## Why this concept matters
This concept is provided as a controlled glossary entry for standards, governance, and implementation review.

Use this concept consistently when mapping authority, evidence, reliance, and auditability across governance and implementation artifacts.

## Names and relationships

### Alternative designations
- **assurance level** (`en`, `alternative`)
- **assurance levels** (`en`, `alternative`)

### Related concepts
- [credential]({{ '/terms/credential/' | relative_url }})
- [issuer]({{ '/terms/issuer/' | relative_url }})
- [issuance]({{ '/terms/issuance/' | relative_url }})
- [verifiable-credential]({{ '/terms/verifiable-credential/' | relative_url }})
- [authorization]({{ '/terms/authorization/' | relative_url }})
- [permission]({{ '/terms/permission/' | relative_url }})

### Semantic relations
- **related**: `urn:tig:concept:credential`
- **related**: `urn:tig:concept:issuer`
- **related**: `urn:tig:concept:issuance`
- **related**: `urn:tig:concept:verifiable-credential`
- **related**: `urn:tig:concept:authorization`
- **related**: `urn:tig:concept:permission`

### Cross-vocabulary mappings
Not specified

## Provenance and identity
- **Concept ID**: `urn:tig:concept:assurance-level`
- **Editorial status**: `stable`
- **Provenance classification**: `adapted`
- **Source corpus**: Trust over IP Main Glossary

### Standards and source references
- ToIP CTWG maintained glossary source: `spec/terms-definitions/assurance-level.md`

<details markdown="1">
<summary><strong>Implementation and governance metadata</strong></summary>

### Legacy aliases
assurance level, assurance levels

### Governance profile
- **Authority scope**: credential_issuance, access_decisioning, assurance_and_audit
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
- attestation
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

- **Accountable entity**: glossary_maintainers

**Evidence produced**
- issuance_log
- attestation
- access_decision_log
- policy_document
- registry_entry
- status_record
- audit_log
- verification_log

### Notes
- Assurance levels are most useful when the criteria for each level are explicit, testable, and supported by inspectable evidence.

### Supporting definitions
- For verifiable credentials, an assurance level measures the degree of certainty in an identity's authenticity or a credential's validity. It is influenced by the strength of the identity assurance process, the robustness of the authentication process, the management of the credential issuer, and the evidence available to support those assessments.

### Mental models
Not specified

### Crosswalk references
- **NIST**: IA-8
- **ISO**: ISO/IEC 29115

</details>

---

*Generated from `glossary/terms/assurance-level.yaml`. Edit the source concept and regenerate rather than editing this page directly.*
