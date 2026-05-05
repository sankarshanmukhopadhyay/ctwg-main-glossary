# Governance term examples

This directory contains schema-aligned examples for governance-executable glossary terms. These files mirror the authoritative term artifact shape used under `glossary/terms/` and can be copied when adding or refactoring terms.

## Example coverage

| Example | Primary purpose |
|---|---|
| `authority.yaml` | Authority scope, delegation, revocation, and policy evidence. |
| `delegation.yaml` | Delegation grant and revocation decision semantics. |
| `revocation.yaml` | Runtime status and reliance-decision evidence. |
| `trust-registry.yaml` | Registry-management and governance-recognition control-plane role. |
| `verifier.yaml` | Verification and reliance role with execution-time evidence. |

## Authoring checklist

A high-quality term artifact should:

1. define the term in operational language;
2. identify whether the term is descriptive, governance-supporting, or core-operational;
3. state the authority scope and execution role;
4. identify whether revocation is supported and which lifecycle states are relevant;
5. include evidence artifacts that can be inspected by downstream assurance tooling;
6. pair decision points with enforcement points;
7. include source references or an explicit maintainer rationale; and
8. include `see_also` links where interpretation depends on adjacent concepts.

Validate examples and source terms with:

```bash
python tools/validate_governance_glossary.py
```
