---
title: "data-integrity-proof"
---

> Generated file. Update `glossary/terms/data-integrity-proof.yaml` and regenerate artifacts instead of editing this page directly.

# data-integrity-proof

## Concept Identity
- **Concept ID**: `urn:tig:concept:data-integrity-proof`
- **Editorial status**: `stable`
- **Provenance classification**: `locally_defined`
- **Source corpus**: Trust Infrastructure Glossary

## In Simple English
A cryptographic proof mechanism used to protect the authenticity and integrity of verifiable credentials and similar constrained digital documents.

## Definition
A cryptographic proof mechanism used to protect the authenticity and integrity of verifiable credentials and similar constrained digital documents.

## Reader Note
This term is provided as a controlled glossary entry for standards, governance, and implementation review.

## Implementation Relevance
Use this term consistently when mapping authority, evidence, reliance, and auditability across governance and implementation artifacts.

## Alternative Designations
- **Data Integrity proof** (`en`, `alternative`)
- **VC Data Integrity proof** (`en`, `alternative`)

## Legacy Aliases
Data Integrity proof, VC Data Integrity proof

## Semantic Relations
- **related**: `urn:tig:concept:digital-signature`
- **related**: `urn:tig:concept:cryptographic-verifiability`
- **related**: `urn:tig:concept:verifiable-credential`
- **related**: `urn:tig:concept:proof`

## Cross-Vocabulary Mappings
Not specified

## See Also
- [digital-signature]({{ '/terms/digital-signature/' | relative_url }})
- [cryptographic-verifiability]({{ '/terms/cryptographic-verifiability/' | relative_url }})
- [verifiable-credential]({{ '/terms/verifiable-credential/' | relative_url }})
- [proof]({{ '/terms/proof/' | relative_url }})

## Standards and Source References
- [Verifiable Credential Data Integrity 1.0](https://www.w3.org/TR/vc-data-integrity/) (W3C; Recommendation; 1.0; 2025-05-15) — normative

## Governance Profile
- **Authority scope**: verification_and_reliance, assurance_and_audit
- **Delegation mode**: direct
- **Revocation supported**: False
- **Lifecycle states**: proposed, active, retired
- **Execution role**: hybrid
- **Control-plane role**: decision_plane_component

## Enforcement Points
- reliance_decision

## Assurance
**Evidence artifacts**
- verification_log
- audit_log
- attestation

- **Assurance level hint**: AL2+
- **Auditability**: high

## Control Plane
**Decision points**
- reliance_decision

- **Accountable entity**: glossary_maintainers

**Evidence produced**
- verification_log
- audit_log
- attestation

## Notes
Not specified

## Supporting Definitions
Not specified

## Mental Models
Not specified

## Crosswalk References
- **W3C**: Verifiable Credential Data Integrity 1.0
