---
title: "Term Quality Rubric"
parent: Governance Documentation
nav_order: 30
---

# Term Quality Rubric

Use this rubric when creating or refining glossary terms.

| Check | Question | Evidence of quality |
|---|---|---|
| Clarity | Is the definition precise and readable without circularity? | The definition explains the concept rather than restating the label. |
| Scope | Does the definition make clear what is in and out of scope? | Boundaries, role, or context are explicit. |
| Operational relevance | Would an implementer understand where this term matters in a real system? | The governance profile and execution role match the definition. |
| Authority | If the term involves decision rights, is the actor and authority boundary clear? | `authority_scope` and `accountable_entity` are specific. |
| Delegation | If delegation is possible, is it stated and bounded? | `delegation_mode` and `enforcement_points` are coherent. |
| Lifecycle | Are issuance, update, expiry, suspension, revocation, or replacement relevant? | `lifecycle_states` and `revocation_supported` are aligned. |
| Evidence | Does the term imply logs, attestations, proofs, records, or policy artifacts? | `evidence_artifacts` and `evidence_produced` are specific and inspectable. |
| Cross-reference quality | Are related terms linked cleanly and usefully? | `see_also` improves interpretation and navigation. |
| Source quality | Are references authoritative and current enough for glossary use? | `sources`, `supporting_definitions`, or `mental_models` explain provenance. |
| Machine readability | Can downstream systems use the term without guessing? | Values conform to the schema and controlled vocabularies. |

## Prioritization rule

Prioritize governance-heavy terms first. These are terms that shape who may act, who may decide, who may revoke, and what evidence can later be inspected.

## Quality-report relationship

The generated governance quality report operationalizes this rubric. It flags missing sources, missing cross-references, weak evidence, revocation-evidence gaps, and assurance-level mismatches.
