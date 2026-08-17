---
title: "verification"
---

# verification

An action an agent (of a principal) performs to determine the authenticity of a claim or other data object. Cryptographic verification uses cryptographic keys.

## Formal definition
An action an agent (of a principal) performs to determine the authenticity of a claim or other data object. Cryptographic verification uses cryptographic keys.

## Why this concept matters
This concept is provided as a controlled glossary entry for standards, governance, and implementation review.

Use this concept consistently when mapping authority, evidence, reliance, and auditability across governance and implementation artifacts.

## Names and relationships

### Alternative designations
- **verify** (`en`, `alternative`)
- **verifies** (`en`, `alternative`)
- **verified** (`en`, `alternative`)
- **verifying** (`en`, `alternative`)

### Related concepts
- [validation]({{ '/terms/validation/' | relative_url }})
- [verifier]({{ '/terms/verifier/' | relative_url }})
- [proof]({{ '/terms/proof/' | relative_url }})
- [cryptographic-verifiability]({{ '/terms/cryptographic-verifiability/' | relative_url }})

### Semantic relations
- **related**: `urn:tig:concept:validation`
- **related**: `urn:tig:concept:verifier`
- **related**: `urn:tig:concept:proof`
- **related**: `urn:tig:concept:cryptographic-verifiability`

### Cross-vocabulary mappings
Not specified

## Provenance and identity
- **Concept ID**: `urn:tig:concept:verification`
- **Editorial status**: `stable`
- **Provenance classification**: `adapted`
- **Source corpus**: Trust over IP Main Glossary

### Standards and source references
- ToIP CTWG maintained glossary source: `spec/terms-definitions/verification.md`

<details markdown="1">
<summary><strong>Implementation and governance metadata</strong></summary>

### Legacy aliases
verification, verify, verifies, verified, verifying

### Governance profile
- **Authority scope**: credential_issuance, delegation_and_scope
- **Delegation mode**: direct_or_constrained
- **Revocation supported**: False
- **Lifecycle states**: documented, active, deprecated
- **Execution role**: runtime
- **Control-plane role**: decision_plane_component

### Enforcement points
- delegation_grant
- issuance_decision

### Assurance
**Evidence artifacts**
- delegation_record
- issuance_log

- **Assurance level hint**: AL2+
- **Auditability**: high

### Control plane
**Decision points**
- delegation_grant
- issuance_decision

- **Accountable entity**: glossary_maintainers

**Evidence produced**
- delegation_record
- issuance_log

### Notes
Not specified

### Supporting definitions
- [eSSIF-Lab](https://essif-lab.github.io/framework/docs/essifLab-glossary#verify): The act, by or on behalf of a [party](https://essif-lab.github.io/framework/docs/terms/party), of determining whether that data is authentic (i.e. originates from the [party](https://essif-lab.github.io/framework/docs/terms/party) that authored it), timely (i.e. has not expired), and conforms to other specifications that apply to its structure.

### Mental models
- [W3C Verifiable Credentials Data Model Roles & Information Flows](https://www.w3.org/TR/vc-data-model/#roles)

### Crosswalk references
Not specified

</details>

---

*Generated from `glossary/terms/verification.yaml`. Edit the source concept and regenerate rather than editing this page directly.*
