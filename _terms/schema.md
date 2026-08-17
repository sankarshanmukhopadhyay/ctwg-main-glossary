---
title: "schema"
---

> Generated file. Update `glossary/terms/schema.yaml` and regenerate artifacts instead of editing this page directly.

# schema

## Concept Identity
- **Concept ID**: `urn:tig:concept:schema`
- **Editorial status**: `stable`
- **Provenance classification**: `adapted`
- **Source corpus**: Trust over IP Main Glossary

## In Simple English
A simple-English summary has not yet been added for this term.

## Definition
A framework, pattern, or set of rules for enforcing a specific structure on a digital object or a set of digital data. There are many types of schemas, e.g., data schema, credential verification schema, database schema.

## Reader Note
This term is provided as a controlled glossary entry for standards, governance, and implementation review.

## Implementation Relevance
Use this term consistently when mapping authority, evidence, reliance, and auditability across governance and implementation artifacts.

## Alternative Designations
- **schemas** (`en`, `alternative`)

## Legacy Aliases
schema, schemas

## Semantic Relations
- **related**: `urn:tig:concept:credential`
- **related**: `urn:tig:concept:issuer`
- **related**: `urn:tig:concept:issuance`
- **related**: `urn:tig:concept:verifiable-credential`
- **related**: `urn:tig:concept:policy`
- **related**: `urn:tig:concept:governance-framework`

## Cross-Vocabulary Mappings
Not specified

## See Also
- [credential]({{ '/terms/credential/' | relative_url }})
- [issuer]({{ '/terms/issuer/' | relative_url }})
- [issuance]({{ '/terms/issuance/' | relative_url }})
- [verifiable-credential]({{ '/terms/verifiable-credential/' | relative_url }})
- [policy]({{ '/terms/policy/' | relative_url }})
- [governance-framework]({{ '/terms/governance-framework/' | relative_url }})

## Standards and Source References
- ToIP CTWG maintained glossary source: `spec/terms-definitions/schema.md`

## Governance Profile
- **Authority scope**: credential_issuance, policy_definition
- **Delegation mode**: direct
- **Revocation supported**: True
- **Lifecycle states**: proposed, active, suspended, revoked, retired
- **Execution role**: hybrid
- **Control-plane role**: decision_plane_component

## Enforcement Points
- policy_approval
- issuance_decision
- revocation_decision

## Assurance
**Evidence artifacts**
- policy_document
- issuance_log
- registry_entry
- audit_log
- status_record
- verification_log

- **Assurance level hint**: AL2+
- **Auditability**: high

## Control Plane
**Decision points**
- policy_approval
- issuance_decision
- revocation_decision

- **Accountable entity**: glossary_maintainers

**Evidence produced**
- policy_document
- issuance_log
- registry_entry
- audit_log
- status_record
- verification_log

## Notes
- `credentialSchema` is a Property Definition in the W3C VC Data Model. See section 3.2.1.

## Supporting Definitions
- For more information, see: W3C [Data Schemas](https://www.w3.org/TR/vc-data-model/#data-schemas).

## Mental Models
Not specified

## Crosswalk References
Not specified
