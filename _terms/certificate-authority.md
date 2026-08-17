---
title: "certificate-authority"
---

> Generated file. Update `glossary/terms/certificate-authority.yaml` and regenerate artifacts instead of editing this page directly.

# certificate-authority

## Concept Identity
- **Concept ID**: `urn:tig:concept:certificate-authority`
- **Editorial status**: `stable`
- **Provenance classification**: `locally_defined`
- **Source corpus**: Trust Infrastructure Glossary

## In Simple English
The entity in a public key infrastructure (PKI) that is responsible for issuing public key certificates and exacting compliance to a PKI policy.

## Definition
The entity in a public key infrastructure (PKI) that is responsible for issuing public key certificates and exacting compliance to a PKI policy.

## Reader Note
This term is provided as a controlled glossary entry for standards, governance, and implementation review.

## Implementation Relevance
Use this term consistently when mapping authority, evidence, reliance, and auditability across governance and implementation artifacts.

## Alternative Designations
- **certificate authority** (`en`, `alternative`)
- **certificate authorities** (`en`, `alternative`)

## Legacy Aliases
certificate authority, certificate authorities

## Semantic Relations
- **related**: `urn:tig:concept:policy`
- **related**: `urn:tig:concept:governance-framework`
- **related**: `urn:tig:concept:requirement`
- **related**: `urn:tig:concept:governance`
- **related**: `urn:tig:concept:governing-authority`

## Cross-Vocabulary Mappings
Not specified

## See Also
- [policy]({{ '/terms/policy/' | relative_url }})
- [governance-framework]({{ '/terms/governance-framework/' | relative_url }})
- [requirement]({{ '/terms/requirement/' | relative_url }})
- [governance]({{ '/terms/governance/' | relative_url }})
- [governing-authority]({{ '/terms/governing-authority/' | relative_url }})

## Standards and Source References
- [NIST-CSRC](https://csrc.nist.gov/glossary/term/certificate_authority).

## Governance Profile
- **Authority scope**: policy_definition, governance_recognition
- **Delegation mode**: direct
- **Revocation supported**: True
- **Lifecycle states**: proposed, active, suspended, revoked, retired
- **Execution role**: runtime
- **Control-plane role**: decision_plane_component

## Enforcement Points
- policy_approval
- revocation_decision

## Assurance
**Evidence artifacts**
- policy_document
- audit_log
- status_record
- verification_log
- registry_entry

- **Assurance level hint**: AL2+
- **Auditability**: high

## Control Plane
**Decision points**
- policy_approval
- revocation_decision

- **Accountable entity**: governance_authority

**Evidence produced**
- policy_document
- audit_log
- status_record
- verification_log
- registry_entry

## Notes
Not specified

## Supporting Definitions
- Also known as: [[ref: certification authority]].
- [Wikipedia](https://en.wikipedia.org/wiki/Certificate_authority): In [cryptography](https://en.wikipedia.org/wiki/Cryptography), a certificate authority or certification authority (CA) is an entity that stores, signs, and issues [digital certificates](https://en.wikipedia.org/wiki/Public_key_certificate). A digital certificate certifies the ownership of a public key by the named subject of the certificate. This allows others (relying parties) to rely upon signatures or on assertions made about the private key that corresponds to the certified public key. A CA acts as a trusted third party—trusted both by the subject (owner) of the certificate and by the party relying upon the certificate.[<sup>\[1\]</sup>](https://en.wikipedia.org/wiki/Certificate_authority#cite_note-1) The format of these certificates is specified by the [X.509](https://en.wikipedia.org/wiki/X.509) or [EMV](https://en.wikipedia.org/wiki/EMV) standard.

## Mental Models
Not specified

## Crosswalk References
Not specified
