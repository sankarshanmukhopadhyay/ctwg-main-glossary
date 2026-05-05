---
title: "Review and Gap Analysis"
parent: Governance Documentation
nav_order: 45
---

# Main Glossary Review: Gaps and Improvement Areas

This review tracks remaining improvement areas after the v1.1.0 assurance-ready infrastructure increment.

| Priority | Area | Gap / Issue | Why It Matters | Proposed Improvement |
|---|---|---|---|---|
| P0 | Source attribution | Many term artifacts still have empty `sources`. | Assurance consumers need provenance, especially for high-impact governance terms. | Prioritize source references for `core-operational` and revocation-sensitive terms. |
| P0 | Cross-reference quality | Many terms have empty `see_also`. | Readers and machines both need adjacency signals to interpret terms correctly. | Add cross-references for terms that participate in authority, delegation, reliance, or revocation semantics. |
| P0 | Revocation evidence | Some revocation-sensitive terms require stronger status, audit, verification, or registry evidence. | Revocation without inspectable evidence weakens execution-time governance. | Use the quality report to prioritize terms flagged with `weak_revocation_evidence`. |
| P1 | Assurance-level calibration | Some decision-plane terms need review to ensure `AL1+` and `AL2+` are consistently applied. | Assurance hints influence downstream prioritization. | Review decision-plane terms by authority scope and evidence artifact. |
| P1 | Definition quality | Some definitions may be circular or too close to the term label. | Circular definitions reduce adoption and weaken machine-assisted documentation. | Rewrite flagged terms to explain operational meaning and boundary. |
| P1 | JSON-LD semantics | JSON-LD publication currently uses a pragmatic schema.org mapping. | Advanced consumers may need a richer context. | Add a dedicated context after downstream usage patterns stabilize. |
| P2 | External compatibility | Consumers need clearer versioning expectations for generated artifacts. | Tooling integrations need stable contracts. | Add artifact compatibility and versioning policy. |

## Operational review source

Use `generated/json/governance-quality-report.json` as the machine-readable backlog and `governance/quality-report.md` as the maintainer-facing review surface.
