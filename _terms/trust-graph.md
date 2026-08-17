---
title: "trust-graph"
---

> Generated file. Update `glossary/terms/trust-graph.yaml` and regenerate artifacts instead of editing this page directly.

# trust-graph

## Concept Identity
- **Concept ID**: `urn:tig:concept:trust-graph`
- **Editorial status**: `stable`
- **Provenance classification**: `adapted`
- **Source corpus**: Trust over IP Main Glossary

## In Simple English
A simple-English summary has not yet been added for this term.

## Definition
A data structure describing the trust relationship between two or more entities. A simple trust graph may be expressed as a trust list. More complex trust graphs can be recorded or registered in and queried from a trust registry. Trust graphs can also be expressed using trust chains and chained credentials. Trust graphs can enable verifiers and relying parties to make transitive trust decisions.

## Reader Note
This term is provided as a controlled glossary entry for standards, governance, and implementation review.

## Implementation Relevance
Use this term consistently when mapping authority, evidence, reliance, and auditability across governance and implementation artifacts.

## Alternative Designations
- **trust graph** (`en`, `alternative`)
- **trust graphs** (`en`, `alternative`)

## Legacy Aliases
trust graph, trust graphs

## Semantic Relations
- **related**: `urn:tig:concept:authorization-graph`
- **related**: `urn:tig:concept:governance-graph`
- **related**: `urn:tig:concept:reputation-graph`

## Cross-Vocabulary Mappings
Not specified

## See Also
- [authorization graph]({{ '/terms/authorization-graph/' | relative_url }})
- [governance graph]({{ '/terms/governance-graph/' | relative_url }})
- [reputation graph]({{ '/terms/reputation-graph/' | relative_url }})

## Standards and Source References
- ToIP CTWG maintained glossary source: `spec/terms-definitions/trust-graph.md`

## Governance Profile
- **Authority scope**: credential_issuance, verification_and_reliance, registry_management
- **Delegation mode**: direct
- **Revocation supported**: True
- **Lifecycle states**: proposed, active, suspended, revoked, retired
- **Execution role**: runtime
- **Control-plane role**: decision_plane_component

## Enforcement Points
- registration_decision
- reliance_decision
- issuance_decision
- revocation_decision

## Assurance
**Evidence artifacts**
- registry_entry
- issuance_log
- verification_log

- **Assurance level hint**: AL2+
- **Auditability**: high

## Control Plane
**Decision points**
- registration_decision
- reliance_decision
- issuance_decision
- revocation_decision

- **Accountable entity**: verifier_operator

**Evidence produced**
- registry_entry
- issuance_log
- verification_log

## Notes
Not specified

## Supporting Definitions
Not specified

## Mental Models
Not specified

## Crosswalk References
Not specified
