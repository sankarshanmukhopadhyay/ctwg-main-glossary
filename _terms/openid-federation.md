---
title: "openid-federation"
---

> Generated file. Update `glossary/terms/openid-federation.yaml` and regenerate artifacts instead of editing this page directly.

# openid-federation

## Concept Identity
- **Concept ID**: `urn:tig:concept:openid-federation`
- **Editorial status**: `stable`
- **Provenance classification**: `locally_defined`
- **Source corpus**: Trust Infrastructure Glossary

## In Simple English
A federation framework for establishing trust among OpenID participants using entity statements, trust chains, and federation metadata.

## Definition
A federation framework for establishing trust among OpenID participants using entity statements, trust chains, and federation metadata.

## Reader Note
This term is provided as a controlled glossary entry for standards, governance, and implementation review.

## Implementation Relevance
Use this term consistently when mapping authority, evidence, reliance, and auditability across governance and implementation artifacts.

## Alternative Designations
- **OpenID Federation** (`en`, `alternative`)

## Legacy Aliases
OpenID Federation

## Semantic Relations
- **related**: `urn:tig:concept:federation`
- **related**: `urn:tig:concept:trust-chain`
- **related**: `urn:tig:concept:entity-statement`
- **related**: `urn:tig:concept:trust-anchor`

## Cross-Vocabulary Mappings
Not specified

## See Also
- [federation]({{ '/terms/federation/' | relative_url }})
- [trust-chain]({{ '/terms/trust-chain/' | relative_url }})
- [entity-statement]({{ '/terms/entity-statement/' | relative_url }})
- [trust-anchor]({{ '/terms/trust-anchor/' | relative_url }})

## Standards and Source References
- [OpenID Federation 1.0](https://openid.net/specs/openid-federation-1_0.html) (OpenID Foundation; Final Specification; 1.0; 2026-02-17) — normative

## Governance Profile
- **Authority scope**: governance_recognition, registry_management, verification_and_reliance
- **Delegation mode**: direct
- **Revocation supported**: False
- **Lifecycle states**: proposed, active, retired
- **Execution role**: hybrid
- **Control-plane role**: decision_plane_component

## Enforcement Points
- registration_decision
- reliance_decision

## Assurance
**Evidence artifacts**
- registry_entry
- verification_log
- audit_log
- policy_document

- **Assurance level hint**: AL2+
- **Auditability**: high

## Control Plane
**Decision points**
- registration_decision
- reliance_decision

- **Accountable entity**: glossary_maintainers

**Evidence produced**
- registry_entry
- verification_log
- audit_log
- policy_document

## Notes
Not specified

## Supporting Definitions
Not specified

## Mental Models
Not specified

## Crosswalk References
- **OPENID**: OpenID Federation 1.0
