# Governance-Aware Glossary Extension Model

## Purpose

This document defines a practical extension model for enriching glossary terms with governance and assurance semantics while preserving the current markdown-based publication flow.

## Design goals

- preserve the current glossary authoring model
- support gradual adoption
- add machine-readable structure for high-value terms
- make authority, delegation, lifecycle, and evidence semantics clearer

## Suggested extension fields

| Field | Meaning |
|---|---|
| `term_id` | Stable identifier for the glossary term |
| `display_name` | Human-readable display name |
| `authority_scope` | Scope of authority associated with the term |
| `delegation_supported` | Whether authority may be delegated |
| `delegation_constraints` | Conditions or boundaries on delegation |
| `lifecycle_states` | Operational states relevant to the term |
| `revocation_supported` | Whether revocation applies |
| `revocation_actor` | Who can revoke or invalidate |
| `policy_artifacts` | Policies, frameworks, or rules governing the term |
| `evidence_artifacts` | Logs, attestations, proofs, registries, or records produced |
| `verification_points` | Where or when the term is evaluated or enforced |
| `accountable_actor` | Party answerable for misuse or invalid state |
| `cross_refs` | Related glossary or standards references |

## Suggested usage model

1. Keep the markdown term definition as the canonical human-readable source.
2. Add optional governance-aware JSON documents for terms with significant operational impact.
3. Use the JSON artifacts for validation, crosswalks, and future API exports.

## Initial target terms

- authority
- delegation
- delegator
- delegatee
- control-authority
- policy
- issuer
- verifier
- revocation
- trust-registry
- assurance-level

## Validation path

The schema in `schemas/governance-term.schema.json` is intended as a lightweight validation baseline for future CI checks.
