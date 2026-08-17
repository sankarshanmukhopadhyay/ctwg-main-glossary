---
title: "issuance"
---

> Generated file. Update `glossary/terms/issuance.yaml` and regenerate artifacts instead of editing this page directly.

# issuance

## Concept Identity
- **Concept ID**: `urn:tig:concept:issuance`
- **Editorial status**: `stable`
- **Provenance classification**: `adapted`
- **Source corpus**: Trust over IP Main Glossary

## In Simple English
The action of an issuer producing and transmitting a digital credential to a holder. A holder may request issuance by submitting an issuance request.

## Definition
The action of an issuer producing and transmitting a digital credential to a holder. A holder may request issuance by submitting an issuance request.

## Reader Note
This term is provided as a controlled glossary entry for standards, governance, and implementation review.

## Implementation Relevance
Use this term consistently when mapping authority, evidence, reliance, and auditability across governance and implementation artifacts.

## Alternative Designations
- **issue** (`en`, `alternative`)
- **issues** (`en`, `alternative`)
- **issued** (`en`, `alternative`)
- **issuing** (`en`, `alternative`)

## Legacy Aliases
issuance, issue, issues, issued, issuing

## Semantic Relations
- **related**: `urn:tig:concept:presentation`
- **related**: `urn:tig:concept:revocation`

## Cross-Vocabulary Mappings
Not specified

## See Also
- [presentation]({{ '/terms/presentation/' | relative_url }})
- [revocation]({{ '/terms/revocation/' | relative_url }})

## Standards and Source References
- ToIP CTWG maintained glossary source: `spec/terms-definitions/issuance.md`

## Governance Profile
- **Authority scope**: credential_issuance
- **Delegation mode**: direct
- **Revocation supported**: True
- **Lifecycle states**: proposed, active, suspended, revoked, retired
- **Execution role**: runtime
- **Control-plane role**: decision_plane_component

## Enforcement Points
- issuance_decision
- revocation_decision

## Assurance
**Evidence artifacts**
- issuance_log
- registry_entry
- status_record
- audit_log
- verification_log

- **Assurance level hint**: AL2+
- **Auditability**: high

## Control Plane
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

## Notes
Not specified

## Supporting Definitions
Not specified

## Mental Models
Not specified

## Crosswalk References
Not specified
