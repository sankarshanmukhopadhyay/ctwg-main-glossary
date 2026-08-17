---
title: "end-verifiability"
---

> Generated file. Update `glossary/terms/end-verifiability.yaml` and regenerate artifacts instead of editing this page directly.

# end-verifiability

## Concept Identity
- **Concept ID**: `urn:tig:concept:end-verifiability`
- **Editorial status**: `stable`
- **Provenance classification**: `locally_defined`
- **Source corpus**: Trust Infrastructure Glossary

## In Simple English
A simple-English summary has not yet been added for this term.

## Definition
a data item or statement may be cryptographically securely attributable to its source (party at the source end) by any recipient verifier (party at the destination end) without reliance on any infrastructure not under the verifier’s ultimate control.

## Reader Note
This term is provided as a controlled glossary entry for standards, governance, and implementation review.

## Implementation Relevance
Use this term consistently when mapping authority, evidence, reliance, and auditability across governance and implementation artifacts.

## Alternative Designations
- **end verifiability** (`en`, `alternative`)

## Legacy Aliases
end-verifiability, end verifiability

## Semantic Relations
- **related**: `urn:tig:concept:verification`
- **related**: `urn:tig:concept:verifier`
- **related**: `urn:tig:concept:relying-party`
- **related**: `urn:tig:concept:trust-decision`

## Cross-Vocabulary Mappings
Not specified

## See Also
- [verification]({{ '/terms/verification/' | relative_url }})
- [verifier]({{ '/terms/verifier/' | relative_url }})
- [relying-party]({{ '/terms/relying-party/' | relative_url }})
- [trust-decision]({{ '/terms/trust-decision/' | relative_url }})

## Standards and Source References
- Dr. S.Smith, 2024

## Governance Profile
- **Authority scope**: verification_and_reliance
- **Delegation mode**: direct
- **Revocation supported**: False
- **Lifecycle states**: documented, active, deprecated
- **Execution role**: runtime
- **Control-plane role**: decision_plane_component

## Enforcement Points
- reliance_decision

## Assurance
**Evidence artifacts**
- verification_log

- **Assurance level hint**: AL2+
- **Auditability**: high

## Control Plane
**Decision points**
- reliance_decision

- **Accountable entity**: verifier_operator

**Evidence produced**
- verification_log

## Notes
Not specified

## Supporting Definitions
- Also see [[ref: end-verifiable]]
- More in <a href="https://weboftrust.github.io/WOT-terms/docs/glossary/end-verifiability">extended KERI glossary</a>

## Mental Models
Not specified

## Crosswalk References
Not specified
