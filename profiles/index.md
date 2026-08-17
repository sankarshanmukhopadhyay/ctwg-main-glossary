---
title: "Vocabulary Profiles"
parent: "Use TIG"
nav_order: 1
---

# Vocabulary Profiles

Profiles provide curated, versionable subsets of TIG for downstream systems. They identify concepts by stable `concept_id` and do not redefine their meaning.

| Profile | Intended use | Source |
|---|---|---|
| **Core Trust Infrastructure** | Foundational authority, governance, evidence, registry and trust-decision concepts | `profiles/core-trust-infrastructure.yaml` |
| **Agent Governance** | Delegation, agent authority and governed-action concepts | `profiles/agent-governance.yaml` |
| **Assurance and Conformance** | Assurance, evidence, conformance and interoperability concepts | `profiles/assurance-and-conformance.yaml` |

Profiles are deliberately small enough to be inspectable and composable. A consuming project should identify the TIG release and profile version it depends on.

For profile semantics and authoring rules, see [Profile Governance]({{ '/governance/vocabulary-profiles/' | relative_url }}).
