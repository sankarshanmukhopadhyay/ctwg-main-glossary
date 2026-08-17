---
title: "federation-assurance-level"
---

> Generated file. Update `glossary/terms/federation-assurance-level.yaml` and regenerate artifacts instead of editing this page directly.

# federation-assurance-level

## Concept Identity
- **Concept ID**: `urn:tig:concept:federation-assurance-level`
- **Editorial status**: `stable`
- **Provenance classification**: `locally_defined`
- **Source corpus**: Trust Infrastructure Glossary

## In Simple English
A simple-English summary has not yet been added for this term.

## Definition
A category that describes the federation protocol used to communicate an assertion containing authentication) and attribute information (if applicable) to a relying party, as defined in NIST SP 800-63-3 in terms of three levels: FAL 1 (Some confidence), FAL 2 (High confidence), FAL 3 (Very high confidence).

## Reader Note
This term is provided as a controlled glossary entry for standards, governance, and implementation review.

## Implementation Relevance
Use this term consistently when mapping authority, evidence, reliance, and auditability across governance and implementation artifacts.

## Alternative Designations
- **federation assurance level** (`en`, `alternative`)
- **federation assurance levels** (`en`, `alternative`)
- **FAL** (`en`, `alternative`)
- **FALs** (`en`, `alternative`)

## Legacy Aliases
federation assurance level, federation assurance levels, FAL, FALs

## Semantic Relations
- **related**: `urn:tig:concept:authenticator-assurance-level`
- **related**: `urn:tig:concept:identity-assurance-level`

## Cross-Vocabulary Mappings
Not specified

## See Also
- [authenticator assurance level]({{ '/terms/authenticator-assurance-level/' | relative_url }})
- [identity assurance level]({{ '/terms/identity-assurance-level/' | relative_url }})

## Standards and Source References
- [NIST-CSRC](https://csrc.nist.gov/glossary/term/federation_assurance_level).

## Governance Profile
- **Authority scope**: verification_and_reliance, access_decisioning, assurance_and_audit
- **Delegation mode**: direct
- **Revocation supported**: False
- **Lifecycle states**: documented, active, deprecated
- **Execution role**: runtime
- **Control-plane role**: decision_plane_component

## Enforcement Points
- reliance_decision
- access_decision

## Assurance
**Evidence artifacts**
- verification_log
- attestation
- access_decision_log

- **Assurance level hint**: AL2+
- **Auditability**: high

## Control Plane
**Decision points**
- reliance_decision
- access_decision

- **Accountable entity**: glossary_maintainers

**Evidence produced**
- verification_log
- attestation
- access_decision_log

## Notes
Not specified

## Supporting Definitions
Not specified

## Mental Models
Not specified

## Crosswalk References
Not specified
