---
title: "verifiable-credential"
---

# verifiable-credential

A simple-English summary has not yet been added for this concept.

## Formal definition
A cryptographically secured credential whose authenticity and integrity can be verified, including credentials represented using the W3C Verifiable Credentials Data Model, ISO mdoc, or SD-JWT VC profiles depending on the ecosystem profile.

## Why this concept matters
Use this term for the general governance role of verifiable credentials. Use verifiable-credential-data-model-2-0 when specifically referring to the W3C data model.

Implementers should distinguish the credential data model, securing format, transport protocol, holder binding, status mechanism, and presentation protocol.

## Names and relationships

### Alternative designations
- **verifiable credential** (`en`, `alternative`)
- **verifiable credentials** (`en`, `alternative`)
- **VC** (`en`, `alternative`)
- **VCs** (`en`, `alternative`)

### Related concepts
- [digital-credential]({{ '/terms/digital-credential/' | relative_url }})
- [verifiable-credential-data-model-2-0]({{ '/terms/verifiable-credential-data-model-2-0/' | relative_url }})
- [secured-verifiable-credential]({{ '/terms/secured-verifiable-credential/' | relative_url }})
- [verifiable-presentation]({{ '/terms/verifiable-presentation/' | relative_url }})
- [bitstring-status-list]({{ '/terms/bitstring-status-list/' | relative_url }})
- [openid4vci]({{ '/terms/openid4vci/' | relative_url }})
- [openid4vp]({{ '/terms/openid4vp/' | relative_url }})
- [sd-jwt-vc]({{ '/terms/sd-jwt-vc/' | relative_url }})

### Semantic relations
- **related**: `urn:tig:concept:digital-credential`
- **related**: `urn:tig:concept:verifiable-credential-data-model-2-0`
- **related**: `urn:tig:concept:secured-verifiable-credential`
- **related**: `urn:tig:concept:verifiable-presentation`
- **related**: `urn:tig:concept:bitstring-status-list`
- **related**: `urn:tig:concept:openid4vci`
- **related**: `urn:tig:concept:openid4vp`
- **related**: `urn:tig:concept:sd-jwt-vc`

### Cross-vocabulary mappings
Not specified

## Provenance and identity
- **Concept ID**: `urn:tig:concept:verifiable-credential`
- **Editorial status**: `stable`
- **Provenance classification**: `locally_defined`
- **Source corpus**: Trust Infrastructure Glossary

### Standards and source references
- [Verifiable Credentials Data Model v2.0](https://www.w3.org/TR/vc-data-model-2.0/) (W3C; Recommendation; 2.0; 2025-05-15) — normative
- [SD-JWT-based Verifiable Credentials](https://www.rfc-editor.org/rfc/rfc9901.html) (IETF; RFC; 9901; 2025) — normative

<details markdown="1">
<summary><strong>Implementation and governance metadata</strong></summary>

### Legacy aliases
verifiable credential, verifiable credentials, VC, VCs

### Governance profile
- **Authority scope**: credential_issuance
- **Delegation mode**: direct
- **Revocation supported**: True
- **Lifecycle states**: proposed, active, suspended, revoked, retired
- **Execution role**: hybrid
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
- Also known as: [[ref: VC]].
- [W3C VC](https://www.w3.org/TR/vc-data-model/#terminology): A verifiable credential is a tamper-evident credential that has authorship that can be cryptographically verified. Verifiable credentials can be used to build [verifiable presentations](https://www.w3.org/TR/vc-data-model/#dfn-verifiable-presentations), which can also be cryptographically verified. The [claims](https://www.w3.org/TR/vc-data-model/#dfn-claims) in a credential can be about different [subjects](https://www.w3.org/TR/vc-data-model/#dfn-subjects).

### Mental models
- [W3C Verifiable Credentials Data Model Roles & Information Flows](https://www.w3.org/TR/vc-data-model/#roles)

### Crosswalk references
- **W3C**: VC Data Model v2.0
- **IETF**: RFC 9901
- **OPENID**: OpenID4VCI, OpenID4VP

</details>

---

*Generated from `glossary/terms/verifiable-credential.yaml`. Edit the source concept and regenerate rather than editing this page directly.*
