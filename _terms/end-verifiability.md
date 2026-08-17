---
title: "end-verifiability"
---

# end-verifiability

A simple-English summary has not yet been added for this concept.

## Formal definition
a data item or statement may be cryptographically securely attributable to its source (party at the source end) by any recipient verifier (party at the destination end) without reliance on any infrastructure not under the verifier’s ultimate control.

## Why this concept matters
This concept is provided as a controlled glossary entry for standards, governance, and implementation review.

Use this concept consistently when mapping authority, evidence, reliance, and auditability across governance and implementation artifacts.

## Names and relationships

### Alternative designations
- **end verifiability** (`en`, `alternative`)

### Related concepts
- [verification]({{ '/terms/verification/' | relative_url }})
- [verifier]({{ '/terms/verifier/' | relative_url }})
- [relying-party]({{ '/terms/relying-party/' | relative_url }})
- [trust-decision]({{ '/terms/trust-decision/' | relative_url }})

### Semantic relations
- **related**: `urn:tig:concept:verification`
- **related**: `urn:tig:concept:verifier`
- **related**: `urn:tig:concept:relying-party`
- **related**: `urn:tig:concept:trust-decision`

### Cross-vocabulary mappings
Not specified

## Provenance and identity
- **Concept ID**: `urn:tig:concept:end-verifiability`
- **Editorial status**: `stable`
- **Provenance classification**: `locally_defined`
- **Source corpus**: Trust Infrastructure Glossary

### Standards and source references
- Dr. S.Smith, 2024

<details markdown="1">
<summary><strong>Implementation and governance metadata</strong></summary>

### Legacy aliases
end-verifiability, end verifiability

### Governance profile
- **Authority scope**: verification_and_reliance
- **Delegation mode**: direct
- **Revocation supported**: False
- **Lifecycle states**: documented, active, deprecated
- **Execution role**: runtime
- **Control-plane role**: decision_plane_component

### Enforcement points
- reliance_decision

### Assurance
**Evidence artifacts**
- verification_log

- **Assurance level hint**: AL2+
- **Auditability**: high

### Control plane
**Decision points**
- reliance_decision

- **Accountable entity**: verifier_operator

**Evidence produced**
- verification_log

### Notes
Not specified

### Supporting definitions
- Also see [[ref: end-verifiable]]
- More in <a href="https://weboftrust.github.io/WOT-terms/docs/glossary/end-verifiability">extended KERI glossary</a>

### Mental models
Not specified

### Crosswalk references
Not specified

</details>

---

*Generated from `glossary/terms/end-verifiability.yaml`. Edit the source concept and regenerate rather than editing this page directly.*
