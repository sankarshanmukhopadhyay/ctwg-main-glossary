---
title: "verifier"
---

# verifier

A simple-English summary has not yet been added for this concept.

## Formal definition
A role an agent performs to verify one or more proofs of the claims in a digital credential or other verifiable data, and to evaluate whether the presented material satisfies applicable verification and policy criteria.

## Why this concept matters
This concept is provided as a controlled glossary entry for standards, governance, and implementation review.

Use this concept consistently when mapping authority, evidence, reliance, and auditability across governance and implementation artifacts.

## Names and relationships

### Alternative designations
- **verifiers** (`en`, `alternative`)

### Related concepts
- [relying-party]({{ '/terms/relying-party/' | relative_url }})
- [issuer]({{ '/terms/issuer/' | relative_url }})
- [holder]({{ '/terms/holder/' | relative_url }})
- [verification]({{ '/terms/verification/' | relative_url }})
- [openid4vp]({{ '/terms/openid4vp/' | relative_url }})

### Semantic relations
- **related**: `urn:tig:concept:relying-party`
- **related**: `urn:tig:concept:issuer`
- **related**: `urn:tig:concept:holder`
- **related**: `urn:tig:concept:verification`
- **related**: `urn:tig:concept:openid4vp`

### Cross-vocabulary mappings
Not specified

## Provenance and identity
- **Concept ID**: `urn:tig:concept:verifier`
- **Editorial status**: `stable`
- **Provenance classification**: `adapted`
- **Source corpus**: Trust over IP Main Glossary

### Standards and source references
- ToIP CTWG maintained glossary source: `spec/terms-definitions/verifier.md`

<details markdown="1">
<summary><strong>Implementation and governance metadata</strong></summary>

### Legacy aliases
verifier, verifiers

### Governance profile
- **Authority scope**: credential_issuance, verification_and_reliance, policy_definition, delegation_and_scope
- **Delegation mode**: direct_or_constrained
- **Revocation supported**: True
- **Lifecycle states**: proposed, active, suspended, revoked, retired
- **Execution role**: runtime
- **Control-plane role**: decision_plane_component

### Enforcement points
- policy_approval
- delegation_grant
- reliance_decision
- issuance_decision
- revocation_decision

### Assurance
**Evidence artifacts**
- policy_document
- delegation_record
- issuance_log
- verification_log

- **Assurance level hint**: AL2+
- **Auditability**: high

### Control plane
**Decision points**
- policy_approval
- delegation_grant
- reliance_decision
- issuance_decision
- revocation_decision

- **Accountable entity**: verifier_operator

**Evidence produced**
- policy_document
- delegation_record
- issuance_log
- verification_log

### Notes
- A verifier may function as an execution-time decision point because verification outcomes can determine whether access, acceptance, recognition, or reliance is granted.

### Supporting definitions
- [W3C VC](https://www.w3.org/TR/vc-data-model/#terminology): A role an [entity](https://www.w3.org/TR/vc-data-model/#dfn-entities) performs by receiving one or more [verifiable credentials](https://www.w3.org/TR/vc-data-model/#dfn-verifiable-credentials), optionally inside a [verifiable presentation](https://www.w3.org/TR/vc-data-model/#dfn-verifiable-presentations) for processing. Other specifications might refer to this concept as a [[ref: relying party]].
- [eSSIF-Lab](https://essif-lab.github.io/framework/docs/essifLab-glossary#verifier): a component that implements the [capability](https://essif-lab.github.io/framework/docs/terms/capability) to request [peer agents](https://essif-lab.github.io/framework/docs/terms/peer-agent) to present (provide) data from credentials (of a specified kind, issued by specified [parties](https://essif-lab.github.io/framework/docs/terms/party)), and to verify such responses (check structure, signatures, dates), according to its [principal](https://essif-lab.github.io/framework/docs/terms/principal)'s [verifier policy](https://essif-lab.github.io/framework/docs/terms/verifier-policy).
- [NIST](https://csrc.nist.gov/glossary/term/verifier) The entity that verifies the authenticity of a digital signature using the public key.

### Mental models
- [W3C Verifiable Credentials Data Model Roles & Information Flows](https://www.w3.org/TR/vc-data-model/#roles)

### Crosswalk references
- **NIST**: AU-10
- **ISO**: ISO/IEC 27001 A.8.15

</details>

---

*Generated from `glossary/terms/verifier.yaml`. Edit the source concept and regenerate rather than editing this page directly.*
