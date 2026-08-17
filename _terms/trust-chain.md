---
title: "trust-chain"
---

> Generated file. Update `glossary/terms/trust-chain.yaml` and regenerate artifacts instead of editing this page directly.

# trust-chain

## Concept Identity
- **Concept ID**: `urn:tig:concept:trust-chain`
- **Editorial status**: `stable`
- **Provenance classification**: `locally_defined`
- **Source corpus**: Trust Infrastructure Glossary

## In Simple English
A simple-English summary has not yet been added for this term.

## Definition
A sequence of cryptographically verifiable links, statements, or governance-recognized relationships used to establish whether a participant, key, credential, or federation entity should be trusted for a relying decision.

## Reader Note
In OpenID Federation this concept is expressed through signed entity statements and trust anchors. In credential ecosystems it can also describe transitive credential or registry relationships.

## Implementation Relevance
Use this term when a verifier or relying party must validate more than one link of authority before accepting a credential, key, or participant.

## Alternative Designations
- **trust chain** (`en`, `alternative`)
- **trust chains** (`en`, `alternative`)

## Legacy Aliases
trust chain, trust chains

## Semantic Relations
- **related**: `urn:tig:concept:openid-federation`
- **related**: `urn:tig:concept:entity-statement`
- **related**: `urn:tig:concept:trust-anchor`
- **related**: `urn:tig:concept:chain-of-trust`
- **related**: `urn:tig:concept:trust-registry`

## Cross-Vocabulary Mappings
Not specified

## See Also
- [openid-federation]({{ '/terms/openid-federation/' | relative_url }})
- [entity-statement]({{ '/terms/entity-statement/' | relative_url }})
- [trust-anchor]({{ '/terms/trust-anchor/' | relative_url }})
- [chain-of-trust]({{ '/terms/chain-of-trust/' | relative_url }})
- [trust-registry]({{ '/terms/trust-registry/' | relative_url }})

## Standards and Source References
- [OpenID Federation 1.0](https://openid.net/specs/openid-federation-1_0.html) (OpenID Foundation; Final Specification; 1.0; 2026-02-17) — normative

## Governance Profile
- **Authority scope**: credential_issuance
- **Delegation mode**: direct
- **Revocation supported**: True
- **Lifecycle states**: proposed, active, suspended, revoked, retired
- **Execution role**: design
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

- **Accountable entity**: glossary_maintainers

**Evidence produced**
- issuance_log
- registry_entry
- status_record
- audit_log
- verification_log

## Notes
Not specified

## Supporting Definitions
- For more information, see: [Design Principles for the ToIP Stack](https://trustoverip.org/our-work/design-principles/).

## Mental Models
Not specified

## Crosswalk References
- **OPENID**: OpenID Federation 1.0
