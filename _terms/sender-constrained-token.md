---
title: "sender-constrained-token"
---

# sender-constrained-token

A token whose use is cryptographically constrained to a specific sender or key holder, reducing replay risk if the token is copied.

## Formal definition
A token whose use is cryptographically constrained to a specific sender or key holder, reducing replay risk if the token is copied.

## Why this concept matters
This term is part of the v1.2.0 standards-linked refresh and is anchored to active implementation vocabulary.

Use this term when mapping glossary language to implementation profiles, governance controls, conformance checks, or assurance evidence.

## Names and relationships

### Alternative designations
- **sender constrained token** (`en`, `alternative`)

### Related concepts
- [dpop]({{ '/terms/dpop/' | relative_url }})
- [proof-of-possession]({{ '/terms/proof-of-possession/' | relative_url }})
- [authorization]({{ '/terms/authorization/' | relative_url }})
- [access-control]({{ '/terms/access-control/' | relative_url }})

### Semantic relations
- **related**: `urn:tig:concept:dpop`
- **related**: `urn:tig:concept:proof-of-possession`
- **related**: `urn:tig:concept:authorization`
- **related**: `urn:tig:concept:access-control`

### Cross-vocabulary mappings
Not specified

## Provenance and identity
- **Concept ID**: `urn:tig:concept:sender-constrained-token`
- **Editorial status**: `stable`
- **Provenance classification**: `locally_defined`
- **Source corpus**: Trust Infrastructure Glossary

### Standards and source references
- [OAuth 2.0 Demonstrating Proof of Possession](https://www.rfc-editor.org/rfc/rfc9449.html) (IETF; RFC; 9449; 2023-09) — normative

<details markdown="1">
<summary><strong>Implementation and governance metadata</strong></summary>

### Legacy aliases
sender constrained token

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

</details>

---

*Generated from `glossary/terms/sender-constrained-token.yaml`. Edit the source concept and regenerate rather than editing this page directly.*
