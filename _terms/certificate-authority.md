---
title: "certificate-authority"
---

# certificate-authority

The entity in a public key infrastructure (PKI) that is responsible for issuing public key certificates and exacting compliance to a PKI policy.

## Formal definition
The entity in a public key infrastructure (PKI) that is responsible for issuing public key certificates and exacting compliance to a PKI policy.

## Why this concept matters
This concept is provided as a controlled glossary entry for standards, governance, and implementation review.

Use this concept consistently when mapping authority, evidence, reliance, and auditability across governance and implementation artifacts.

## Names and relationships

### Alternative designations
- **certificate authority** (`en`, `alternative`)
- **certificate authorities** (`en`, `alternative`)

### Related concepts
- [policy]({{ '/terms/policy/' | relative_url }})
- [governance-framework]({{ '/terms/governance-framework/' | relative_url }})
- [requirement]({{ '/terms/requirement/' | relative_url }})
- [governance]({{ '/terms/governance/' | relative_url }})
- [governing-authority]({{ '/terms/governing-authority/' | relative_url }})

### Semantic relations
- **related**: `urn:tig:concept:policy`
- **related**: `urn:tig:concept:governance-framework`
- **related**: `urn:tig:concept:requirement`
- **related**: `urn:tig:concept:governance`
- **related**: `urn:tig:concept:governing-authority`

### Cross-vocabulary mappings
Not specified

## Provenance and identity
- **Concept ID**: `urn:tig:concept:certificate-authority`
- **Editorial status**: `stable`
- **Provenance classification**: `locally_defined`
- **Source corpus**: Trust Infrastructure Glossary

### Standards and source references
- [NIST-CSRC](https://csrc.nist.gov/glossary/term/certificate_authority).

<details markdown="1">
<summary><strong>Implementation and governance metadata</strong></summary>

### Legacy aliases
certificate authority, certificate authorities

### Governance profile
- **Authority scope**: policy_definition, governance_recognition
- **Delegation mode**: direct
- **Revocation supported**: True
- **Lifecycle states**: proposed, active, suspended, revoked, retired
- **Execution role**: runtime
- **Control-plane role**: decision_plane_component

### Enforcement points
- policy_approval
- revocation_decision

### Assurance
**Evidence artifacts**
- policy_document
- audit_log
- status_record
- verification_log
- registry_entry

- **Assurance level hint**: AL2+
- **Auditability**: high

### Control plane
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

### Notes
Not specified

### Supporting definitions
- Also known as: [[ref: certification authority]].
- [Wikipedia](https://en.wikipedia.org/wiki/Certificate_authority): In [cryptography](https://en.wikipedia.org/wiki/Cryptography), a certificate authority or certification authority (CA) is an entity that stores, signs, and issues [digital certificates](https://en.wikipedia.org/wiki/Public_key_certificate). A digital certificate certifies the ownership of a public key by the named subject of the certificate. This allows others (relying parties) to rely upon signatures or on assertions made about the private key that corresponds to the certified public key. A CA acts as a trusted third party—trusted both by the subject (owner) of the certificate and by the party relying upon the certificate.[<sup>\[1\]</sup>](https://en.wikipedia.org/wiki/Certificate_authority#cite_note-1) The format of these certificates is specified by the [X.509](https://en.wikipedia.org/wiki/X.509) or [EMV](https://en.wikipedia.org/wiki/EMV) standard.

### Mental models
Not specified

### Crosswalk references
Not specified

</details>

---

*Generated from `glossary/terms/certificate-authority.yaml`. Edit the source concept and regenerate rather than editing this page directly.*
