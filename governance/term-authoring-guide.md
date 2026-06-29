---
title: "Term Authoring Guide"
parent: Governance Documentation
nav_order: 25
---

# Term Authoring Guide

This guide explains how to add or update governance-executable glossary terms.

## Minimum workflow

1. Create or edit a YAML file under `glossary/terms/`.
2. Keep the filename slug aligned with the `term` value.
3. Use only values defined in `schemas/governance-vocabularies.yaml`.
4. Validate and regenerate artifacts.
5. Review generated diffs before committing.

```bash
pip install pyyaml jsonschema
python tools/validate_governance_glossary.py
python tools/build_governance_glossary.py
python tools/build_quality_report.py
python tools/build_jekyll_site.py
```

## Required structure

Each term must include:

```yaml
term: example-term
aliases: []
definition: A precise operational definition.
notes: []
see_also: []
sources:
  - title: Example Standard or Specification
    url: https://example.org/specification
    publisher: Example Publisher
    status: Published
    version: "1.0"
    date: "2026-01-01"
    normative: true
source_file: spec/terms-definitions/example-term.md
governance_profile: descriptive
governance:
  authority_scope:
    - terminology_definition
  delegation_mode: direct
  revocation_supported: false
  lifecycle_states:
    - active
    - documented
    - deprecated
  execution_role: design
  control_plane_role: reference_term
  enforcement_points:
    - definition_approval
assurance:
  evidence_artifacts:
    - definition_change_record
  assurance_level_hint: informative
  auditability: basic
control_plane:
  decision_points:
    - definition_approval
  accountable_entity: glossary_maintainers
  evidence_produced:
    - definition_change_record
crosswalk:
  nist: []
  iso: []
```

## Choosing `governance_profile`

| Value | Use when |
|---|---|
| `descriptive` | The term primarily explains language and does not itself drive authority, recognition, reliance, issuance, access, or revocation. |
| `governance-supporting` | The term helps describe governance operations but is not normally a direct runtime decision component. |
| `core-operational` | The term can affect authority, policy, delegation, verification, reliance, issuance, registry management, access, or revocation. |

## Choosing assurance hints

| Hint | Use when |
|---|---|
| `informative` | The term is primarily descriptive and usually only needs definition-change evidence. |
| `AL1+` | The term is governance-relevant and should be traceable in documentation or policy. |
| `AL2+` | The term may affect operational decisions and should produce inspectable evidence. |

## Revocation guidance

Set `revocation_supported: true` only when the term describes something whose status, authorization, recognition, delegation, or operational validity can be suspended, revoked, or retired.

When revocation is supported:

- include `revoked` in `lifecycle_states`;
- include `revocation_decision` where appropriate;
- include evidence such as `status_record`, `audit_log`, `verification_log`, or `registry_entry`; and
- identify the accountable entity.

## Evidence guidance

Evidence artifacts should be specific enough for downstream systems to test or inspect.

| Evidence artifact | Typical use |
|---|---|
| `definition_change_record` | Maintainer review and glossary change evidence. |
| `policy_document` | Policy, governance framework, or rule evidence. |
| `delegation_record` | Delegation grant, scope, or constraint evidence. |
| `status_record` | Suspension, revocation, retirement, or validity status. |
| `verification_log` | Runtime verification or reliance evidence. |
| `registry_entry` | Registry inclusion, recognition, or status evidence. |
| `audit_log` | Auditable event trail. |
| `issuance_log` | Issuance or credential lifecycle evidence. |
| `access_decision_log` | Access-control decision evidence. |
| `attestation` | Signed or declared assertion evidence. |

## Crosswalk guidance

Crosswalk references should be conservative. A crosswalk means the term is relevant to a cited framework or control family. It does not mean the glossary term satisfies that control.

## Structured source guidance

Use structured citations for standards, specifications, and normative references. Legacy source strings remain supported for backward compatibility, but new standards-backed terms should use citation objects so downstream tools can inspect source title, URL, publisher, status, version, date, and whether the citation is normative.

```yaml
sources:
  - title: OpenID for Verifiable Presentations 1.0
    url: https://openid.net/specs/openid-4-verifiable-presentations-1_0.html
    publisher: OpenID Foundation
    status: Final Specification
    version: "1.0"
    date: "2025-07-09"
    normative: true
```

Keep `see_also` values resolvable to local term names or aliases. Use `crosswalk` for framework mappings and `sources` for citation provenance.

## Examples

Use `examples/governance-term/` for schema-aligned examples.
