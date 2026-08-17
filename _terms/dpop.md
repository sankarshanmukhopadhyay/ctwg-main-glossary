---
title: "dpop"
---

# dpop

An OAuth 2.0 mechanism for sender-constraining tokens by requiring a client to prove possession of a private key when using a token.

## Formal definition
An OAuth 2.0 mechanism for sender-constraining tokens by requiring a client to prove possession of a private key when using a token.

## Why this concept matters
This term is part of the v1.2.0 standards-linked refresh and is anchored to active implementation vocabulary.

Use this term when mapping glossary language to implementation profiles, governance controls, conformance checks, or assurance evidence.

## Names and relationships

### Alternative designations
- **DPoP** (`en`, `alternative`)
- **Demonstrating Proof of Possession** (`en`, `alternative`)

### Related concepts
- [proof-of-possession]({{ '/terms/proof-of-possession/' | relative_url }})
- [sender-constrained-token]({{ '/terms/sender-constrained-token/' | relative_url }})
- [cryptographic-key]({{ '/terms/cryptographic-key/' | relative_url }})
- [authorization]({{ '/terms/authorization/' | relative_url }})

### Semantic relations
- **related**: `urn:tig:concept:proof-of-possession`
- **related**: `urn:tig:concept:sender-constrained-token`
- **related**: `urn:tig:concept:cryptographic-key`
- **related**: `urn:tig:concept:authorization`

### Cross-vocabulary mappings
Not specified

## Provenance and identity
- **Concept ID**: `urn:tig:concept:dpop`
- **Editorial status**: `stable`
- **Provenance classification**: `locally_defined`
- **Source corpus**: Trust Infrastructure Glossary

### Standards and source references
- [OAuth 2.0 Demonstrating Proof of Possession](https://www.rfc-editor.org/rfc/rfc9449.html) (IETF; RFC; 9449; 2023-09) — normative

<details markdown="1">
<summary><strong>Implementation and governance metadata</strong></summary>

### Legacy aliases
DPoP, Demonstrating Proof of Possession

### Governance profile
- **Authority scope**: access_decisioning, verification_and_reliance
- **Delegation mode**: direct
- **Revocation supported**: False
- **Lifecycle states**: proposed, active, retired
- **Execution role**: hybrid
- **Control-plane role**: decision_plane_component

### Enforcement points
- access_decision
- reliance_decision

### Assurance
**Evidence artifacts**
- access_decision_log
- verification_log
- audit_log

- **Assurance level hint**: AL2+
- **Auditability**: high

### Control plane
**Decision points**
- access_decision
- reliance_decision

- **Accountable entity**: glossary_maintainers

**Evidence produced**
- access_decision_log
- verification_log
- audit_log

### Notes
Not specified

### Supporting definitions
Not specified

### Mental models
Not specified

### Crosswalk references
- **IETF**: RFC 9449
- **OPENID**: OpenID4VCI

</details>

---

*Generated from `glossary/terms/dpop.yaml`. Edit the source concept and regenerate rather than editing this page directly.*
