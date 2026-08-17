---
title: "issuance-request"
---

> Generated file. Update `glossary/terms/issuance-request.yaml` and regenerate artifacts instead of editing this page directly.

# issuance-request

## Concept Identity
- **Concept ID**: `urn:tig:concept:issuance-request`
- **Editorial status**: `stable`
- **Provenance classification**: `adapted`
- **Source corpus**: Trust over IP Main Glossary

## In Simple English
A protocol request invoked by the holder of a digital wallet to obtain a digital credential from an issuer.

## Definition
A protocol request invoked by the holder of a digital wallet to obtain a digital credential from an issuer.

## Reader Note
This term is provided as a controlled glossary entry for standards, governance, and implementation review.

## Implementation Relevance
Use this term consistently when mapping authority, evidence, reliance, and auditability across governance and implementation artifacts.

## Alternative Designations
- **issuance request** (`en`, `alternative`)
- **issuance requests** (`en`, `alternative`)

## Legacy Aliases
issuance request, issuance requests

## Semantic Relations
- **related**: `urn:tig:concept:presentation-request`

## Cross-Vocabulary Mappings
Not specified

## See Also
- [presentation request]({{ '/terms/presentation-request/' | relative_url }})

## Standards and Source References
- ToIP CTWG maintained glossary source: `spec/terms-definitions/issuance-request.md`

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
