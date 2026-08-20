---
title: Portfolio Vocabulary Gap Analysis
parent: Semantic authoring
nav_order: 90
permalink: /governance/portfolio-vocabulary-gap-analysis/
---

# Portfolio Vocabulary Gap Analysis

This document records vocabulary observed across the trust-infrastructure portfolio that is not yet represented as a first-class Trust Infrastructure Glossary (TIG) concept.

The analysis prioritizes reusable semantic and governance primitives over repository names, implementation brands, and protocol-specific labels. A term is a strong TIG candidate when it is used across multiple repositories, participates in authority or assurance reasoning, or is required to make machine-readable governance artifacts independently interpretable.

## First expansion tranche

The following concepts are added as `proposed` source artifacts in this change:

- accountability
- assurance
- decision
- effect
- evidence

These foundational concepts recur across TSMM, TIS, GAAM, RAHP, ARPA, ONDTF, PolicyMesh, TRQP, or the DTG ZKP implementation workspace. They are introduced before derivative concepts so that later additions can reference stable TIG identifiers.

## Next high-priority candidates

### Authority, delegation, and lifecycle

- authority boundary
- delegation lineage
- originating-principal continuity
- scope attenuation
- trust-domain transition
- branch convergence
- recognition
- recognition equivalence
- historical authority resolution
- requested-time state
- current state
- revocation convergence
- revocation propagation
- fail-closed lifecycle semantics

### Assurance and conformance

- assurance gap
- assurance proposition
- control credit
- residual assurance state
- review required
- not assessed
- decision receipt
- evidence bundle
- remediation manifest
- conformance class
- conformance declaration
- conformance target
- conformance adapter
- evidence gate
- promotion decision
- combined assurance manifest
- posture report
- control-coverage evidence
- integration invalidation condition

### Policy and distributed governance

- policy lifecycle
- policy-admission decision
- application-action decision
- quorum governance
- transparency checkpoint
- deterministic reconciliation
- fork detection
- trust anchor rotation
- authority context
- semantic drift

### Agent and registry infrastructure

- governed agent identity
- authority control plane
- discovery governance
- discovery-is-not-authority
- publication projection
- authorization overlay
- reconstruction quality
- selected-record provenance
- immutable snapshot
- registry publication profile

### Privacy and proof systems

- capture freshness
- attestation freshness
- proof freshness
- context binding
- audience binding
- correlation horizon
- privacy adversary
- scoped nullifier
- disclosure surface
- degraded mode

### Resilience and harms assurance

- pressure test
- assurance pattern
- guardrail pattern
- evidence pattern
- amplification risk
- retry storm
- remediation lifecycle
- evidence-based retest

## Admission rule

A candidate should become a TIG concept when its definition can be made portable across repositories without importing a repository's normative authority. Project-specific terms may be mapped to a broader TIG concept rather than adopted as preferred designations.

## Evidence and maintenance

Portfolio vocabulary should be re-audited when flagship repositories introduce new normative concepts or release new machine-readable contracts. Future automation should compare repository controlled vocabularies, schemas, requirement registries, and documentation headings against TIG concept identifiers and produce a machine-readable gap report.
