---
title: "trust-chain"
---

# trust-chain

A simple-English summary has not yet been added for this concept.

## Formal definition
A sequence of cryptographically verifiable links, statements, or governance-recognized relationships used to establish whether a participant, key, credential, or federation entity should be trusted for a relying decision.

## Why this concept matters
In OpenID Federation this concept is expressed through signed entity statements and trust anchors. In credential ecosystems it can also describe transitive credential or registry relationships.

Use this term when a verifier or relying party must validate more than one link of authority before accepting a credential, key, or participant.

## Names and relationships

### Alternative designations
- **trust chain** (`en`, `alternative`)
- **trust chains** (`en`, `alternative`)

### Related concepts
- [openid-federation]({{ '/terms/openid-federation/' | relative_url }})
- [entity-statement]({{ '/terms/entity-statement/' | relative_url }})
- [trust-anchor]({{ '/terms/trust-anchor/' | relative_url }})
- [chain-of-trust]({{ '/terms/chain-of-trust/' | relative_url }})
- [trust-registry]({{ '/terms/trust-registry/' | relative_url }})

### Semantic relations
- **related**: `urn:tig:concept:openid-federation`
- **related**: `urn:tig:concept:entity-statement`
- **related**: `urn:tig:concept:trust-anchor`
- **related**: `urn:tig:concept:chain-of-trust`
- **related**: `urn:tig:concept:trust-registry`

### Cross-vocabulary mappings
Not specified

## Provenance and identity
- **Concept ID**: `urn:tig:concept:trust-chain`
- **Editorial status**: `stable`
- **Provenance classification**: `locally_defined`
- **Source corpus**: Trust Infrastructure Glossary

### Standards and source references
- [OpenID Federation 1.0](https://openid.net/specs/openid-federation-1_0.html) (OpenID Foundation; Final Specification; 1.0; 2026-02-17) — normative

<details markdown="1">
<summary><strong>Implementation and governance metadata</strong></summary>

### Legacy aliases
trust chain, trust chains

### Governance profile
- **Authority scope**: credential_issuance
- **Delegation mode**: direct
- **Revocation supported**: True
- **Lifecycle states**: proposed, active, suspended, revoked, retired
- **Execution role**: design
- **Control-plane role**: decision_plane_component

### Enforcement points
- issuance_decision
- revocation_decision

### Assurance
**Evidence artifacts**
- issuance_log
- registry_entry
- status_record
- audit_log
- verification_log

- **Assurance level hint**: AL2+
- **Auditability**: high

### Control plane
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

### Notes
Not specified

### Supporting definitions
- For more information, see: [Design Principles for the ToIP Stack](https://trustoverip.org/our-work/design-principles/).

### Mental models
Not specified

### Crosswalk references
- **OPENID**: OpenID Federation 1.0

</details>

---

*Generated from `glossary/terms/trust-chain.yaml`. Edit the source concept and regenerate rather than editing this page directly.*
