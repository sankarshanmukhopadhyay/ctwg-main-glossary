---
title: "authorization"
---

> Generated file. Update `glossary/terms/authorization.yaml` and regenerate artifacts instead of editing this page directly.

# authorization

## Concept Identity
- **Concept ID**: `urn:tig:concept:authorization`
- **Editorial status**: `stable`
- **Provenance classification**: `locally_defined`
- **Source corpus**: Trust Infrastructure Glossary

## In Simple English
A simple-English summary has not yet been added for this term.

## Definition
The process of determining whether a requested action or service is approved for a specific entity under applicable policies, rules, credentials, or other governing criteria.

## Reader Note
This term is provided as a controlled glossary entry for standards, governance, and implementation review.

## Implementation Relevance
Use this term consistently when mapping authority, evidence, reliance, and auditability across governance and implementation artifacts.

## Alternative Designations
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

## Legacy Aliases
authorization, authorizations, authorize, authorized, unauthorized, authorizing, unauthorizing, authorisation, authorisations, authorise, authorised, unauthorised, authorising, unauthorising

## Semantic Relations
- **related**: `urn:tig:concept:permission`

## Cross-Vocabulary Mappings
Not specified

## See Also
- [permission]({{ '/terms/permission/' | relative_url }})

## Standards and Source References
- [NIST-CSRC](https://csrc.nist.gov/glossary/term/authorization).

## Governance Profile
- **Authority scope**: credential_issuance, policy_definition, access_decisioning
- **Delegation mode**: direct
- **Revocation supported**: True
- **Lifecycle states**: proposed, active, suspended, revoked, retired
- **Execution role**: runtime
- **Control-plane role**: decision_plane_component

## Enforcement Points
- policy_approval
- issuance_decision
- access_decision
- revocation_decision

## Assurance
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

## Control Plane
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

## Notes
Not specified

## Supporting Definitions
Not specified

## Mental Models
Not specified

## Crosswalk References
- **NIST**: AC-2, AC-3
- **ISO**: ISO/IEC 27001 A.5.15, ISO/IEC 42001 8.2
