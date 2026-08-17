---
title: "identity-binding"
---

> Generated file. Update `glossary/terms/identity-binding.yaml` and regenerate artifacts instead of editing this page directly.

# identity-binding

## Concept Identity
- **Concept ID**: `urn:tig:concept:identity-binding`
- **Editorial status**: `stable`
- **Provenance classification**: `adapted`
- **Source corpus**: Trust over IP Main Glossary

## In Simple English
A simple-English summary has not yet been added for this term.

## Definition
The process of associating a set of identity data, such as a credential, with its subject, such as a natural person. The strength of an identity binding is one factor in determining an authenticator assurance level.

## Reader Note
This term is provided as a controlled glossary entry for standards, governance, and implementation review.

## Implementation Relevance
Use this term consistently when mapping authority, evidence, reliance, and auditability across governance and implementation artifacts.

## Alternative Designations
- **identity binding** (`en`, `alternative`)
- **identity bindings** (`en`, `alternative`)

## Legacy Aliases
identity binding, identity bindings

## Semantic Relations
- **related**: `urn:tig:concept:identity-assurance-level`
- **related**: `urn:tig:concept:identity-proofing`

## Cross-Vocabulary Mappings
Not specified

## See Also
- [identity assurance level]({{ '/terms/identity-assurance-level/' | relative_url }})
- [identity proofing]({{ '/terms/identity-proofing/' | relative_url }})

## Standards and Source References
- ToIP CTWG maintained glossary source: `spec/terms-definitions/identity-binding.md`

## Governance Profile
- **Authority scope**: credential_issuance, access_decisioning, assurance_and_audit
- **Delegation mode**: direct
- **Revocation supported**: True
- **Lifecycle states**: proposed, active, suspended, revoked, retired
- **Execution role**: design
- **Control-plane role**: decision_plane_component

## Enforcement Points
- issuance_decision
- access_decision
- revocation_decision

## Assurance
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

## Control Plane
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

## Notes
Not specified

## Supporting Definitions
Not specified

## Mental Models
Not specified

## Crosswalk References
Not specified
