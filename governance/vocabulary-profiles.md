---
title: "Vocabulary Profiles"
parent: "Operations & Evolution"
nav_order: 5
grand_parent: "Govern TIG"
---

# Vocabulary Profiles

Profiles allow downstream systems to consume a bounded subset of TIG without copying the full vocabulary.

A profile identifies concepts by stable `concept_id`. It may also record a purpose and minimum TIG release.

Profiles are **selection artifacts**, not independent definitions. They do not redefine concept meaning.

## Included profiles

- `profiles/core-trust-infrastructure.yaml`
- `profiles/agent-governance.yaml`
- `profiles/assurance-and-conformance.yaml`

Profiles are validated against the live concept corpus by `tools/validate_profiles.py`.

## Downstream pattern

A project should pin a TIG release and profile when reproducibility matters. Projects with additional local terminology should keep those local concepts in their own namespace and map them back to TIG where appropriate.
