---
title: "dcql"
---

> Generated file. Update `glossary/terms/dcql.yaml` and regenerate artifacts instead of editing this page directly.

# dcql

## Concept Identity
- **Concept ID**: `urn:tig:concept:dcql`
- **Editorial status**: `stable`
- **Provenance classification**: `locally_defined`
- **Source corpus**: Trust Infrastructure Glossary

## In Simple English
A query language defined by OpenID4VP for requesting credential presentations in a flexible and credential-format-aware way.

## Definition
A query language defined by OpenID4VP for requesting credential presentations in a flexible and credential-format-aware way.

## Reader Note
This term is provided as a controlled glossary entry for standards, governance, and implementation review.

## Implementation Relevance
Use this term consistently when mapping authority, evidence, reliance, and auditability across governance and implementation artifacts.

## Alternative Designations
- **Digital Credentials Query Language** (`en`, `alternative`)
- **DCQL** (`en`, `alternative`)

## Legacy Aliases
Digital Credentials Query Language, DCQL

## Semantic Relations
- **related**: `urn:tig:concept:openid4vp`
- **related**: `urn:tig:concept:presentation-request`
- **related**: `urn:tig:concept:verifiable-presentation`
- **related**: `urn:tig:concept:credential`

## Cross-Vocabulary Mappings
Not specified

## See Also
- [openid4vp]({{ '/terms/openid4vp/' | relative_url }})
- [presentation-request]({{ '/terms/presentation-request/' | relative_url }})
- [verifiable-presentation]({{ '/terms/verifiable-presentation/' | relative_url }})
- [credential]({{ '/terms/credential/' | relative_url }})

## Standards and Source References
- [OpenID for Verifiable Presentations 1.0](https://openid.net/specs/openid-4-verifiable-presentations-1_0.html) (OpenID Foundation; Final Specification; 1.0; 2025-07-09) — normative

## Governance Profile
- **Authority scope**: verification_and_reliance, policy_definition
- **Delegation mode**: direct
- **Revocation supported**: False
- **Lifecycle states**: proposed, active, retired
- **Execution role**: hybrid
- **Control-plane role**: decision_plane_component

## Enforcement Points
- reliance_decision
- policy_approval

## Assurance
**Evidence artifacts**
- policy_document
- verification_log
- audit_log

- **Assurance level hint**: AL2+
- **Auditability**: high

## Control Plane
**Decision points**
- reliance_decision
- policy_approval

- **Accountable entity**: glossary_maintainers

**Evidence produced**
- policy_document
- verification_log
- audit_log

## Notes
Not specified

## Supporting Definitions
Not specified

## Mental Models
Not specified

## Crosswalk References
- **OPENID**: OpenID4VP 1.0
