---
title: "delegation"
---

> Generated file. Update `glossary/terms/delegation.yaml` and regenerate artifacts instead of editing this page directly.

# delegation

## Concept Identity
- **Concept ID**: `urn:tig:concept:delegation`
- **Editorial status**: `stable`
- **Provenance classification**: `adapted`
- **Source corpus**: Trust over IP Main Glossary

## In Simple English
A simple-English summary has not yet been added for this term.

## Definition
The act of a first party (the delegator) authorizing a second party (the delegatee) to perform a defined set of actions on behalf of the first party within an authorized scope and subject to applicable constraints.

## Reader Note
This term is provided as a controlled glossary entry for standards, governance, and implementation review.

## Implementation Relevance
Use this term consistently when mapping authority, evidence, reliance, and auditability across governance and implementation artifacts.

## Alternative Designations
- **delegate** (`en`, `alternative`)
- **delegated** (`en`, `alternative`)
- **delegates** (`en`, `alternative`)

## Legacy Aliases
delegation, delegate, delegated, delegates

## Semantic Relations
- **related**: `urn:tig:concept:delegator`
- **related**: `urn:tig:concept:delegatee`
- **related**: `urn:tig:concept:authorization`
- **related**: `urn:tig:concept:revocation`

## Cross-Vocabulary Mappings
Not specified

## See Also
- [delegator]({{ '/terms/delegator/' | relative_url }})
- [delegatee]({{ '/terms/delegatee/' | relative_url }})
- [authorization]({{ '/terms/authorization/' | relative_url }})
- [revocation]({{ '/terms/revocation/' | relative_url }})

## Standards and Source References
- ToIP CTWG maintained glossary source: `spec/terms-definitions/delegation.md`

## Governance Profile
- **Authority scope**: delegation_and_scope
- **Delegation mode**: direct_or_constrained
- **Revocation supported**: True
- **Lifecycle states**: proposed, active, suspended, revoked, retired
- **Execution role**: runtime
- **Control-plane role**: decision_plane_component

## Enforcement Points
- delegation_grant
- revocation_decision

## Assurance
**Evidence artifacts**
- delegation_record
- policy_document
- status_record
- audit_log
- verification_log
- registry_entry

- **Assurance level hint**: AL2+
- **Auditability**: high

## Control Plane
**Decision points**
- delegation_grant
- revocation_decision

- **Accountable entity**: glossary_maintainers

**Evidence produced**
- delegation_record
- policy_document
- status_record
- audit_log
- verification_log
- registry_entry

## Notes
Not specified

## Supporting Definitions
- Delegation may be expressed through a [[ref: delegation credential]] or other policy-governed mechanism and may be limited by scope, time, conditions, or revocation.
- More specific for KERI see: [[xref: keri1, delegated-identifier]]

## Mental Models
Not specified

## Crosswalk References
- **NIST**: AC-6
- **ISO**: ISO/IEC 42001 8.3
