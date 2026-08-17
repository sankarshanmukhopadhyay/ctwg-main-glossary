---
title: "revocation"
---

# revocation

A simple-English summary has not yet been added for this concept.

## Formal definition
In the context of digital credentials, revocation is an event or status change signifying that the issuer no longer attests to the validity of a credential it has issued. In the context of cryptographic keys, revocation is an event or status change signifying that the controller no longer attests to the validity of a public/private key pair for which the controller is authoritative.

## Why this concept matters
This concept is provided as a controlled glossary entry for standards, governance, and implementation review.

Use this concept consistently when mapping authority, evidence, reliance, and auditability across governance and implementation artifacts.

## Names and relationships

### Alternative designations
- **revocations** (`en`, `alternative`)
- **revoke** (`en`, `alternative`)
- **revokes** (`en`, `alternative`)
- **revoked** (`en`, `alternative`)
- **revoking** (`en`, `alternative`)

### Related concepts
- [issuance]({{ '/terms/issuance/' | relative_url }})
- [presentation]({{ '/terms/presentation/' | relative_url }})

### Semantic relations
- **related**: `urn:tig:concept:issuance`
- **related**: `urn:tig:concept:presentation`

### Cross-vocabulary mappings
Not specified

## Provenance and identity
- **Concept ID**: `urn:tig:concept:revocation`
- **Editorial status**: `stable`
- **Provenance classification**: `adapted`
- **Source corpus**: Trust over IP Main Glossary

### Standards and source references
- ToIP CTWG maintained glossary source: `spec/terms-definitions/revocation.md`

<details markdown="1">
<summary><strong>Implementation and governance metadata</strong></summary>

### Legacy aliases
revocation, revocations, revoke, revokes, revoked, revoking

### Governance profile
- **Authority scope**: credential_issuance, verification_and_reliance, governance_recognition
- **Delegation mode**: direct
- **Revocation supported**: True
- **Lifecycle states**: proposed, active, suspended, revoked, retired
- **Execution role**: runtime
- **Control-plane role**: decision_plane_component

### Enforcement points
- reliance_decision
- issuance_decision
- revocation_decision

### Assurance
**Evidence artifacts**
- status_record
- issuance_log
- verification_log

- **Assurance level hint**: AL2+
- **Auditability**: high

### Control plane
**Decision points**
- reliance_decision
- issuance_decision
- revocation_decision

- **Accountable entity**: issuer_operator

**Evidence produced**
- status_record
- issuance_log
- verification_log

### Notes
- Revocation only has practical effect when relying parties or other affected actors can discover and act on the changed status.

### Supporting definitions
- [eSSIF-Lab](https://essif-lab.github.io/framework/docs/essifLab-glossary#revokerevocation): the act, by or on behalf of the [party](https://essif-lab.github.io/framework/docs/terms/party) that has issued the [credential](https://essif-lab.github.io/framework/docs/terms/credential), of no longer vouching for the correctness or any other qualification of (arbitrary parts of) that [credential](https://essif-lab.github.io/framework/docs/terms/credential).
- [NIST-CSRC](https://csrc.nist.gov/glossary/term/revocation): **​​For digital certificates**: The process of permanently ending the binding between a certificate and the identity asserted in the certificate from a specified time forward. **For cryptographic keys**: A process whereby a notice is made available to affected entities that keys should be removed from operational use prior to the end of the established cryptoperiod of those keys.

### Mental models
Not specified

### Crosswalk references
- **NIST**: CM-3
- **ISO**: ISO/IEC 27001 A.5.36

</details>

---

*Generated from `glossary/terms/revocation.yaml`. Edit the source concept and regenerate rather than editing this page directly.*
