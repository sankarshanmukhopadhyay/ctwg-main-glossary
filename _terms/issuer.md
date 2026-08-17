---
title: "issuer"
---

# issuer

A simple-English summary has not yet been added for this concept.

## Formal definition
A role an agent performs to assert a set of claims, package and digitally sign them, typically in the form of a digital credential, and transmit them to a holder under applicable policy and governance constraints.

## Why this concept matters
This concept is provided as a controlled glossary entry for standards, governance, and implementation review.

Use this concept consistently when mapping authority, evidence, reliance, and auditability across governance and implementation artifacts.

## Names and relationships

### Alternative designations
- **issuers** (`en`, `alternative`)

### Related concepts
- [verifier]({{ '/terms/verifier/' | relative_url }})
- [holder]({{ '/terms/holder/' | relative_url }})

### Semantic relations
- **related**: `urn:tig:concept:verifier`
- **related**: `urn:tig:concept:holder`

### Cross-vocabulary mappings
Not specified

## Provenance and identity
- **Concept ID**: `urn:tig:concept:issuer`
- **Editorial status**: `stable`
- **Provenance classification**: `adapted`
- **Source corpus**: Trust over IP Main Glossary

### Standards and source references
- ToIP CTWG maintained glossary source: `spec/terms-definitions/issuer.md`

<details markdown="1">
<summary><strong>Implementation and governance metadata</strong></summary>

### Legacy aliases
issuer, issuers

### Governance profile
- **Authority scope**: credential_issuance, policy_definition, delegation_and_scope, governance_recognition
- **Delegation mode**: direct_or_constrained
- **Revocation supported**: True
- **Lifecycle states**: proposed, active, suspended, revoked, retired
- **Execution role**: runtime
- **Control-plane role**: decision_plane_component

### Enforcement points
- policy_approval
- delegation_grant
- issuance_decision
- revocation_decision

### Assurance
**Evidence artifacts**
- policy_document
- delegation_record
- status_record
- issuance_log

- **Assurance level hint**: AL2+
- **Auditability**: high

### Control plane
**Decision points**
- policy_approval
- delegation_grant
- issuance_decision
- revocation_decision

- **Accountable entity**: governance_authority

**Evidence produced**
- policy_document
- delegation_record
- status_record
- issuance_log

### Notes
- An issuer commonly bears responsibility for issuance criteria, status maintenance, and revocation handling relevant to the credentials it issues.

### Supporting definitions
- [eSSIF-Lab](https://essif-lab.github.io/framework/docs/essifLab-glossary#issuer): a component that implements the [capability](https://essif-lab.github.io/framework/docs/terms/capability) to construct [credentials](https://essif-lab.github.io/framework/docs/terms/credential) from data objects, according to the content of its [principal](https://essif-lab.github.io/framework/docs/terms/principal)'s [issuer](https://essif-lab.github.io/framework/docs/terms/issuer)-Policy (specifically regarding the way in which the [credential](https://essif-lab.github.io/framework/docs/terms/credential) is to be digitally signed), and pass it to the [wallet](https://essif-lab.github.io/framework/docs/terms/wallet)-component of its [principal](https://essif-lab.github.io/framework/docs/terms/principal) allowing it to be issued.
- [W3C VC](https://www.w3.org/TR/vc-data-model/#terminology): A role an [entity](https://www.w3.org/TR/vc-data-model/#dfn-entities) can perform by asserting [claims](https://www.w3.org/TR/vc-data-model/#dfn-claims) about one or more [subjects](https://www.w3.org/TR/vc-data-model/#dfn-subjects), creating a [verifiable credential](https://www.w3.org/TR/vc-data-model/#dfn-verifiable-credentials) from these [claims](https://www.w3.org/TR/vc-data-model/#dfn-claims), and transmitting the [verifiable credential](https://www.w3.org/TR/vc-data-model/#dfn-verifiable-credentials) to a [holder](https://www.w3.org/TR/vc-data-model/#dfn-holders).

### Mental models
- [W3C Verifiable Credentials Data Model Roles & Information Flows](https://www.w3.org/TR/vc-data-model/#roles)

### Crosswalk references
- **NIST**: IA-5
- **ISO**: ISO/IEC 27001 A.5.16

</details>

---

*Generated from `glossary/terms/issuer.yaml`. Edit the source concept and regenerate rather than editing this page directly.*
