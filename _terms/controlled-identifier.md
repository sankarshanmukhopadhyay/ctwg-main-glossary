---
title: "controlled-identifier"
---

> Generated file. Update `glossary/terms/controlled-identifier.yaml` and regenerate artifacts instead of editing this page directly.

# controlled-identifier

## Concept Identity
- **Concept ID**: `urn:tig:concept:controlled-identifier`
- **Editorial status**: `stable`
- **Provenance classification**: `locally_defined`
- **Source corpus**: Trust Infrastructure Glossary

## In Simple English
An identifier whose controller can be discovered through an associated controlled identifier document containing verification material and service endpoints.

## Definition
An identifier whose controller can be discovered through an associated controlled identifier document containing verification material and service endpoints.

## Reader Note
This term is provided as a controlled glossary entry for standards, governance, and implementation review.

## Implementation Relevance
Use this term consistently when mapping authority, evidence, reliance, and auditability across governance and implementation artifacts.

## Alternative Designations
- **controlled identifier** (`en`, `alternative`)

## Legacy Aliases
controlled identifier

## Semantic Relations
- **related**: `urn:tig:concept:decentralized-identifier`
- **related**: `urn:tig:concept:did-document`
- **related**: `urn:tig:concept:controller`
- **related**: `urn:tig:concept:cryptographic-key`

## Cross-Vocabulary Mappings
Not specified

## See Also
- [decentralized-identifier]({{ '/terms/decentralized-identifier/' | relative_url }})
- [did-document]({{ '/terms/did-document/' | relative_url }})
- [controller]({{ '/terms/controller/' | relative_url }})
- [cryptographic-key]({{ '/terms/cryptographic-key/' | relative_url }})

## Standards and Source References
- [Controlled Identifiers v1.0](https://www.w3.org/TR/cid/) (W3C; Recommendation; 1.0; 2025-05-15) — normative

## Governance Profile
- **Authority scope**: verification_and_reliance, delegation_and_scope
- **Delegation mode**: direct_or_constrained
- **Revocation supported**: False
- **Lifecycle states**: proposed, active, retired
- **Execution role**: hybrid
- **Control-plane role**: decision_plane_component

## Enforcement Points
- reliance_decision
- delegation_grant

## Assurance
**Evidence artifacts**
- verification_log
- delegation_record
- audit_log

- **Assurance level hint**: AL2+
- **Auditability**: high

## Control Plane
**Decision points**
- reliance_decision
- delegation_grant

- **Accountable entity**: glossary_maintainers

**Evidence produced**
- verification_log
- delegation_record
- audit_log

## Notes
Not specified

## Supporting Definitions
Not specified

## Mental Models
Not specified

## Crosswalk References
- **W3C**: Controlled Identifiers v1.0, DID Core
