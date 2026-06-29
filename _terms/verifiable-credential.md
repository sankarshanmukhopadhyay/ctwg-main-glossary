---
title: "verifiable-credential"
---

> Generated file. Update `glossary/terms/verifiable-credential.yaml` and regenerate artifacts instead of editing this page directly.

# verifiable-credential

## Definition
A cryptographically secured credential whose authenticity and integrity can be verified, including credentials represented using the W3C Verifiable Credentials Data Model, ISO mdoc, or SD-JWT VC profiles depending on the ecosystem profile.

## Reader Note
Use this term for the general governance role of verifiable credentials. Use verifiable-credential-data-model-2-0 when specifically referring to the W3C data model.

## Implementation Relevance
Implementers should distinguish the credential data model, securing format, transport protocol, holder binding, status mechanism, and presentation protocol.

## Aliases
verifiable credential, verifiable credentials, VC, VCs

## See Also
- [digital-credential]({{ '/terms/digital-credential/' | relative_url }})
- [verifiable-credential-data-model-2-0]({{ '/terms/verifiable-credential-data-model-2-0/' | relative_url }})
- [secured-verifiable-credential]({{ '/terms/secured-verifiable-credential/' | relative_url }})
- [verifiable-presentation]({{ '/terms/verifiable-presentation/' | relative_url }})
- [bitstring-status-list]({{ '/terms/bitstring-status-list/' | relative_url }})
- [openid4vci]({{ '/terms/openid4vci/' | relative_url }})
- [openid4vp]({{ '/terms/openid4vp/' | relative_url }})
- [sd-jwt-vc]({{ '/terms/sd-jwt-vc/' | relative_url }})

## Standards and Source References
- [Verifiable Credentials Data Model v2.0](https://www.w3.org/TR/vc-data-model-2.0/) (W3C; Recommendation; 2.0; 2025-05-15) — normative
- [SD-JWT-based Verifiable Credentials](https://www.rfc-editor.org/rfc/rfc9901.html) (IETF; RFC; 9901; 2025) — normative

## Governance Profile
- **Authority scope**: credential_issuance
- **Delegation mode**: direct
- **Revocation supported**: True
- **Lifecycle states**: proposed, active, suspended, revoked, retired
- **Execution role**: hybrid
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
- Also known as: [[ref: VC]].
- [W3C VC](https://www.w3.org/TR/vc-data-model/#terminology): A verifiable credential is a tamper-evident credential that has authorship that can be cryptographically verified. Verifiable credentials can be used to build [verifiable presentations](https://www.w3.org/TR/vc-data-model/#dfn-verifiable-presentations), which can also be cryptographically verified. The [claims](https://www.w3.org/TR/vc-data-model/#dfn-claims) in a credential can be about different [subjects](https://www.w3.org/TR/vc-data-model/#dfn-subjects).

## Mental Models
- [W3C Verifiable Credentials Data Model Roles & Information Flows](https://www.w3.org/TR/vc-data-model/#roles)

## Crosswalk References
- **W3C**: VC Data Model v2.0
- **IETF**: RFC 9901
- **OPENID**: OpenID4VCI, OpenID4VP
