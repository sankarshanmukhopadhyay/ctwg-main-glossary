---
title: "Assurance Model"
parent: Governance Documentation
nav_order: 26
---

# Assurance Model

The glossary includes assurance metadata so terms can be sorted, reviewed, and consumed by downstream governance and conformance systems.

## What assurance hints mean

Assurance hints are not certifications. They are term-level indicators that help maintainers and downstream consumers understand how operationally significant a term may be.

| Hint | Meaning | Typical evidence expectation |
|---|---|---|
| `informative` | Descriptive term; no direct operational assurance implication. | `definition_change_record` is usually sufficient. |
| `AL1+` | Governance-relevant term; useful for policy interpretation, documentation, and review. | Definition-change evidence plus relevant policy or documentation evidence. |
| `AL2+` | Operationally relevant term; may affect authority, verification, evidence, reliance, issuance, access, delegation, or revocation. | Specific evidence such as policy documents, registry entries, status records, logs, attestations, or delegation records. |

## What assurance hints do not mean

An assurance hint does not certify:

- an implementation;
- a governance framework;
- a registry;
- a relying party;
- a credential ecosystem; or
- an operational control.

It only describes the expected assurance relevance of the term inside this glossary.

## Evidence and auditability

The `assurance.evidence_artifacts` and `control_plane.evidence_produced` fields identify the kinds of artifacts that should exist when the term participates in governance decisions.

Auditability values are intentionally simple:

| Value | Meaning |
|---|---|
| `basic` | The term is mostly documentary. |
| `moderate` | The term has governance relevance and should be traceable. |
| `high` | The term may affect runtime or control-plane decisions and should produce inspectable evidence. |

## Review expectations

Terms with `control_plane_role: decision_plane_component` should normally avoid `informative` assurance unless the documentation clearly explains why the term does not affect execution or reliance.

Terms with `revocation_supported: true` should normally include revocation-relevant evidence such as `status_record`, `audit_log`, `verification_log`, or `registry_entry`.
