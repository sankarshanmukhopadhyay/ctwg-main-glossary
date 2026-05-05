# Governance Quality Report

> Generated file. Update `glossary/terms/` or `tools/build_quality_report.py` and regenerate artifacts instead of editing this report directly.

This report is an assurance-readiness view over the structured glossary source layer. It does not certify the glossary. It identifies evidence, attribution, cross-reference, revocation, and assurance-quality gaps that maintainers can prioritize.

## Summary

- Terms evaluated: **534**
- Quality score: **85.6 / 100**
- Total findings: **987**

## Severity counts

- `high`: 78
- `medium`: 515
- `low`: 394

## Coverage

- `decision_plane_component`: 306
- `revocation_supported`: 108
- `with_evidence`: 534
- `with_see_also`: 140
- `with_sources`: 158

## Finding categories

- `missing_sources`: 376 — No source references are present.
- `missing_see_also`: 394 — No cross-reference terms are present.
- `missing_evidence`: 0 — No evidence artifacts are present.
- `generic_evidence`: 136 — Only generic definition-change evidence is present for a non-descriptive term.
- `weak_revocation_evidence`: 78 — Revocation semantics are not backed by revocation-relevant evidence.
- `decision_plane_low_assurance`: 0 — Decision-plane role is paired with a low assurance hint.
- `high_impact_informative`: 3 — High-impact decision point is paired with informative assurance.
- `decision_without_enforcement`: 0 — Decision points are not paired with enforcement points.
- `possibly_circular_definition`: 0 — Definition appears too close to the term label.

## Prioritized findings

### accreditation — `weak_revocation_evidence`

- Severity: **high**
- Source: `glossary/terms/accreditation.yaml`
- Finding: Revocation is supported but evidence does not include status, audit, verification, or registry evidence.
- Recommended action: Add status_record, audit_log, verification_log, or registry_entry to make revocation independently inspectable.

### administering-authority — `weak_revocation_evidence`

- Severity: **high**
- Source: `glossary/terms/administering-authority.yaml`
- Finding: Revocation is supported but evidence does not include status, audit, verification, or registry evidence.
- Recommended action: Add status_record, audit_log, verification_log, or registry_entry to make revocation independently inspectable.

### administering-body — `weak_revocation_evidence`

- Severity: **high**
- Source: `glossary/terms/administering-body.yaml`
- Finding: Revocation is supported but evidence does not include status, audit, verification, or registry evidence.
- Recommended action: Add status_record, audit_log, verification_log, or registry_entry to make revocation independently inspectable.

### agent — `weak_revocation_evidence`

- Severity: **high**
- Source: `glossary/terms/agent.yaml`
- Finding: Revocation is supported but evidence does not include status, audit, verification, or registry evidence.
- Recommended action: Add status_record, audit_log, verification_log, or registry_entry to make revocation independently inspectable.

### assurance-level — `weak_revocation_evidence`

- Severity: **high**
- Source: `glossary/terms/assurance-level.yaml`
- Finding: Revocation is supported but evidence does not include status, audit, verification, or registry evidence.
- Recommended action: Add status_record, audit_log, verification_log, or registry_entry to make revocation independently inspectable.

### authentic-chained-data-container — `weak_revocation_evidence`

- Severity: **high**
- Source: `glossary/terms/authentic-chained-data-container.yaml`
- Finding: Revocation is supported but evidence does not include status, audit, verification, or registry evidence.
- Recommended action: Add status_record, audit_log, verification_log, or registry_entry to make revocation independently inspectable.

### authentication — `weak_revocation_evidence`

- Severity: **high**
- Source: `glossary/terms/authentication.yaml`
- Finding: Revocation is supported but evidence does not include status, audit, verification, or registry evidence.
- Recommended action: Add status_record, audit_log, verification_log, or registry_entry to make revocation independently inspectable.

### authenticator — `weak_revocation_evidence`

- Severity: **high**
- Source: `glossary/terms/authenticator.yaml`
- Finding: Revocation is supported but evidence does not include status, audit, verification, or registry evidence.
- Recommended action: Add status_record, audit_log, verification_log, or registry_entry to make revocation independently inspectable.

### authoritative — `weak_revocation_evidence`

- Severity: **high**
- Source: `glossary/terms/authoritative.yaml`
- Finding: Revocation is supported but evidence does not include status, audit, verification, or registry evidence.
- Recommended action: Add status_record, audit_log, verification_log, or registry_entry to make revocation independently inspectable.

### authorization — `weak_revocation_evidence`

- Severity: **high**
- Source: `glossary/terms/authorization.yaml`
- Finding: Revocation is supported but evidence does not include status, audit, verification, or registry evidence.
- Recommended action: Add status_record, audit_log, verification_log, or registry_entry to make revocation independently inspectable.

### authorization-graph — `weak_revocation_evidence`

- Severity: **high**
- Source: `glossary/terms/authorization-graph.yaml`
- Finding: Revocation is supported but evidence does not include status, audit, verification, or registry evidence.
- Recommended action: Add status_record, audit_log, verification_log, or registry_entry to make revocation independently inspectable.

### authorized-organizational-representative — `weak_revocation_evidence`

- Severity: **high**
- Source: `glossary/terms/authorized-organizational-representative.yaml`
- Finding: Revocation is supported but evidence does not include status, audit, verification, or registry evidence.
- Recommended action: Add status_record, audit_log, verification_log, or registry_entry to make revocation independently inspectable.

### autonomic-namespace — `weak_revocation_evidence`

- Severity: **high**
- Source: `glossary/terms/autonomic-namespace.yaml`
- Finding: Revocation is supported but evidence does not include status, audit, verification, or registry evidence.
- Recommended action: Add status_record, audit_log, verification_log, or registry_entry to make revocation independently inspectable.

### bola — `weak_revocation_evidence`

- Severity: **high**
- Source: `glossary/terms/bola.yaml`
- Finding: Revocation is supported but evidence does not include status, audit, verification, or registry evidence.
- Recommended action: Add status_record, audit_log, verification_log, or registry_entry to make revocation independently inspectable.

### broken-object-level-authorization — `weak_revocation_evidence`

- Severity: **high**
- Source: `glossary/terms/broken-object-level-authorization.yaml`
- Finding: Revocation is supported but evidence does not include status, audit, verification, or registry evidence.
- Recommended action: Add status_record, audit_log, verification_log, or registry_entry to make revocation independently inspectable.

### ca — `weak_revocation_evidence`

- Severity: **high**
- Source: `glossary/terms/ca.yaml`
- Finding: Revocation is supported but evidence does not include status, audit, verification, or registry evidence.
- Recommended action: Add status_record, audit_log, verification_log, or registry_entry to make revocation independently inspectable.

### capability — `weak_revocation_evidence`

- Severity: **high**
- Source: `glossary/terms/capability.yaml`
- Finding: Revocation is supported but evidence does not include status, audit, verification, or registry evidence.
- Recommended action: Add status_record, audit_log, verification_log, or registry_entry to make revocation independently inspectable.

### certificate-authority — `weak_revocation_evidence`

- Severity: **high**
- Source: `glossary/terms/certificate-authority.yaml`
- Finding: Revocation is supported but evidence does not include status, audit, verification, or registry evidence.
- Recommended action: Add status_record, audit_log, verification_log, or registry_entry to make revocation independently inspectable.

### certification-authority — `weak_revocation_evidence`

- Severity: **high**
- Source: `glossary/terms/certification-authority.yaml`
- Finding: Revocation is supported but evidence does not include status, audit, verification, or registry evidence.
- Recommended action: Add status_record, audit_log, verification_log, or registry_entry to make revocation independently inspectable.

### chained-credentials — `weak_revocation_evidence`

- Severity: **high**
- Source: `glossary/terms/chained-credentials.yaml`
- Finding: Revocation is supported but evidence does not include status, audit, verification, or registry evidence.
- Recommended action: Add status_record, audit_log, verification_log, or registry_entry to make revocation independently inspectable.

### control-authority — `weak_revocation_evidence`

- Severity: **high**
- Source: `glossary/terms/control-authority.yaml`
- Finding: Revocation is supported but evidence does not include status, audit, verification, or registry evidence.
- Recommended action: Add status_record, audit_log, verification_log, or registry_entry to make revocation independently inspectable.

### controlled-document — `weak_revocation_evidence`

- Severity: **high**
- Source: `glossary/terms/controlled-document.yaml`
- Finding: Revocation is supported but evidence does not include status, audit, verification, or registry evidence.
- Recommended action: Add status_record, audit_log, verification_log, or registry_entry to make revocation independently inspectable.

### credential — `weak_revocation_evidence`

- Severity: **high**
- Source: `glossary/terms/credential.yaml`
- Finding: Revocation is supported but evidence does not include status, audit, verification, or registry evidence.
- Recommended action: Add status_record, audit_log, verification_log, or registry_entry to make revocation independently inspectable.

### credential-family — `weak_revocation_evidence`

- Severity: **high**
- Source: `glossary/terms/credential-family.yaml`
- Finding: Revocation is supported but evidence does not include status, audit, verification, or registry evidence.
- Recommended action: Add status_record, audit_log, verification_log, or registry_entry to make revocation independently inspectable.

### credential-governance-framework — `weak_revocation_evidence`

- Severity: **high**
- Source: `glossary/terms/credential-governance-framework.yaml`
- Finding: Revocation is supported but evidence does not include status, audit, verification, or registry evidence.
- Recommended action: Add status_record, audit_log, verification_log, or registry_entry to make revocation independently inspectable.

### credential-offer — `weak_revocation_evidence`

- Severity: **high**
- Source: `glossary/terms/credential-offer.yaml`
- Finding: Revocation is supported but evidence does not include status, audit, verification, or registry evidence.
- Recommended action: Add status_record, audit_log, verification_log, or registry_entry to make revocation independently inspectable.

### credential-request — `weak_revocation_evidence`

- Severity: **high**
- Source: `glossary/terms/credential-request.yaml`
- Finding: Revocation is supported but evidence does not include status, audit, verification, or registry evidence.
- Recommended action: Add status_record, audit_log, verification_log, or registry_entry to make revocation independently inspectable.

### credential-schema — `weak_revocation_evidence`

- Severity: **high**
- Source: `glossary/terms/credential-schema.yaml`
- Finding: Revocation is supported but evidence does not include status, audit, verification, or registry evidence.
- Recommended action: Add status_record, audit_log, verification_log, or registry_entry to make revocation independently inspectable.

### cryptographically-verifiable — `weak_revocation_evidence`

- Severity: **high**
- Source: `glossary/terms/cryptographically-verifiable.yaml`
- Finding: Revocation is supported but evidence does not include status, audit, verification, or registry evidence.
- Recommended action: Add status_record, audit_log, verification_log, or registry_entry to make revocation independently inspectable.

### data-schema — `weak_revocation_evidence`

- Severity: **high**
- Source: `glossary/terms/data-schema.yaml`
- Finding: Revocation is supported but evidence does not include status, audit, verification, or registry evidence.
- Recommended action: Add status_record, audit_log, verification_log, or registry_entry to make revocation independently inspectable.

### dead-drop — `weak_revocation_evidence`

- Severity: **high**
- Source: `glossary/terms/dead-drop.yaml`
- Finding: Revocation is supported but evidence does not include status, audit, verification, or registry evidence.
- Recommended action: Add status_record, audit_log, verification_log, or registry_entry to make revocation independently inspectable.

### decentralized-identifier — `weak_revocation_evidence`

- Severity: **high**
- Source: `glossary/terms/decentralized-identifier.yaml`
- Finding: Revocation is supported but evidence does not include status, audit, verification, or registry evidence.
- Recommended action: Add status_record, audit_log, verification_log, or registry_entry to make revocation independently inspectable.

### delegatee — `weak_revocation_evidence`

- Severity: **high**
- Source: `glossary/terms/delegatee.yaml`
- Finding: Revocation is supported but evidence does not include status, audit, verification, or registry evidence.
- Recommended action: Add status_record, audit_log, verification_log, or registry_entry to make revocation independently inspectable.

### delegation — `weak_revocation_evidence`

- Severity: **high**
- Source: `glossary/terms/delegation.yaml`
- Finding: Revocation is supported but evidence does not include status, audit, verification, or registry evidence.
- Recommended action: Add status_record, audit_log, verification_log, or registry_entry to make revocation independently inspectable.

### delegation-credential — `weak_revocation_evidence`

- Severity: **high**
- Source: `glossary/terms/delegation-credential.yaml`
- Finding: Revocation is supported but evidence does not include status, audit, verification, or registry evidence.
- Recommended action: Add status_record, audit_log, verification_log, or registry_entry to make revocation independently inspectable.

### delegator — `weak_revocation_evidence`

- Severity: **high**
- Source: `glossary/terms/delegator.yaml`
- Finding: Revocation is supported but evidence does not include status, audit, verification, or registry evidence.
- Recommended action: Add status_record, audit_log, verification_log, or registry_entry to make revocation independently inspectable.

### did-document — `weak_revocation_evidence`

- Severity: **high**
- Source: `glossary/terms/did-document.yaml`
- Finding: Revocation is supported but evidence does not include status, audit, verification, or registry evidence.
- Recommended action: Add status_record, audit_log, verification_log, or registry_entry to make revocation independently inspectable.

### digital-agent — `weak_revocation_evidence`

- Severity: **high**
- Source: `glossary/terms/digital-agent.yaml`
- Finding: Revocation is supported but evidence does not include status, audit, verification, or registry evidence.
- Recommended action: Add status_record, audit_log, verification_log, or registry_entry to make revocation independently inspectable.

### ecosystem-governance-framework — `weak_revocation_evidence`

- Severity: **high**
- Source: `glossary/terms/ecosystem-governance-framework.yaml`
- Finding: Revocation is supported but evidence does not include status, audit, verification, or registry evidence.
- Recommended action: Add status_record, audit_log, verification_log, or registry_entry to make revocation independently inspectable.

### foundational-identity — `weak_revocation_evidence`

- Severity: **high**
- Source: `glossary/terms/foundational-identity.yaml`
- Finding: Revocation is supported but evidence does not include status, audit, verification, or registry evidence.
- Recommended action: Add status_record, audit_log, verification_log, or registry_entry to make revocation independently inspectable.

### functional-identity — `weak_revocation_evidence`

- Severity: **high**
- Source: `glossary/terms/functional-identity.yaml`
- Finding: Revocation is supported but evidence does not include status, audit, verification, or registry evidence.
- Recommended action: Add status_record, audit_log, verification_log, or registry_entry to make revocation independently inspectable.

### governance-framework — `weak_revocation_evidence`

- Severity: **high**
- Source: `glossary/terms/governance-framework.yaml`
- Finding: Revocation is supported but evidence does not include status, audit, verification, or registry evidence.
- Recommended action: Add status_record, audit_log, verification_log, or registry_entry to make revocation independently inspectable.

### governing-authority — `weak_revocation_evidence`

- Severity: **high**
- Source: `glossary/terms/governing-authority.yaml`
- Finding: Revocation is supported but evidence does not include status, audit, verification, or registry evidence.
- Recommended action: Add status_record, audit_log, verification_log, or registry_entry to make revocation independently inspectable.

### governing-body — `weak_revocation_evidence`

- Severity: **high**
- Source: `glossary/terms/governing-body.yaml`
- Finding: Revocation is supported but evidence does not include status, audit, verification, or registry evidence.
- Recommended action: Add status_record, audit_log, verification_log, or registry_entry to make revocation independently inspectable.

### guardian — `weak_revocation_evidence`

- Severity: **high**
- Source: `glossary/terms/guardian.yaml`
- Finding: Revocation is supported but evidence does not include status, audit, verification, or registry evidence.
- Recommended action: Add status_record, audit_log, verification_log, or registry_entry to make revocation independently inspectable.

### guardianship-credential — `weak_revocation_evidence`

- Severity: **high**
- Source: `glossary/terms/guardianship-credential.yaml`
- Finding: Revocation is supported but evidence does not include status, audit, verification, or registry evidence.
- Recommended action: Add status_record, audit_log, verification_log, or registry_entry to make revocation independently inspectable.

### holder — `weak_revocation_evidence`

- Severity: **high**
- Source: `glossary/terms/holder.yaml`
- Finding: Revocation is supported but evidence does not include status, audit, verification, or registry evidence.
- Recommended action: Add status_record, audit_log, verification_log, or registry_entry to make revocation independently inspectable.

### identity-binding — `weak_revocation_evidence`

- Severity: **high**
- Source: `glossary/terms/identity-binding.yaml`
- Finding: Revocation is supported but evidence does not include status, audit, verification, or registry evidence.
- Recommended action: Add status_record, audit_log, verification_log, or registry_entry to make revocation independently inspectable.

### identity-document — `weak_revocation_evidence`

- Severity: **high**
- Source: `glossary/terms/identity-document.yaml`
- Finding: Revocation is supported but evidence does not include status, audit, verification, or registry evidence.
- Recommended action: Add status_record, audit_log, verification_log, or registry_entry to make revocation independently inspectable.

### issuance — `weak_revocation_evidence`

- Severity: **high**
- Source: `glossary/terms/issuance.yaml`
- Finding: Revocation is supported but evidence does not include status, audit, verification, or registry evidence.
- Recommended action: Add status_record, audit_log, verification_log, or registry_entry to make revocation independently inspectable.

### issuance-request — `weak_revocation_evidence`

- Severity: **high**
- Source: `glossary/terms/issuance-request.yaml`
- Finding: Revocation is supported but evidence does not include status, audit, verification, or registry evidence.
- Recommended action: Add status_record, audit_log, verification_log, or registry_entry to make revocation independently inspectable.

### legitimized-human-meaningful-identifier — `weak_revocation_evidence`

- Severity: **high**
- Source: `glossary/terms/legitimized-human-meaningful-identifier.yaml`
- Finding: Revocation is supported but evidence does not include status, audit, verification, or registry evidence.
- Recommended action: Add status_record, audit_log, verification_log, or registry_entry to make revocation independently inspectable.

### organizational-authority — `weak_revocation_evidence`

- Severity: **high**
- Source: `glossary/terms/organizational-authority.yaml`
- Finding: Revocation is supported but evidence does not include status, audit, verification, or registry evidence.
- Recommended action: Add status_record, audit_log, verification_log, or registry_entry to make revocation independently inspectable.

### password — `weak_revocation_evidence`

- Severity: **high**
- Source: `glossary/terms/password.yaml`
- Finding: Revocation is supported but evidence does not include status, audit, verification, or registry evidence.
- Recommended action: Add status_record, audit_log, verification_log, or registry_entry to make revocation independently inspectable.

### permission — `weak_revocation_evidence`

- Severity: **high**
- Source: `glossary/terms/permission.yaml`
- Finding: Revocation is supported but evidence does not include status, audit, verification, or registry evidence.
- Recommended action: Add status_record, audit_log, verification_log, or registry_entry to make revocation independently inspectable.

### physical-credential — `weak_revocation_evidence`

- Severity: **high**
- Source: `glossary/terms/physical-credential.yaml`
- Finding: Revocation is supported but evidence does not include status, audit, verification, or registry evidence.
- Recommended action: Add status_record, audit_log, verification_log, or registry_entry to make revocation independently inspectable.

### proof — `weak_revocation_evidence`

- Severity: **high**
- Source: `glossary/terms/proof.yaml`
- Finding: Revocation is supported but evidence does not include status, audit, verification, or registry evidence.
- Recommended action: Add status_record, audit_log, verification_log, or registry_entry to make revocation independently inspectable.

### public-key-certificate — `weak_revocation_evidence`

- Severity: **high**
- Source: `glossary/terms/public-key-certificate.yaml`
- Finding: Revocation is supported but evidence does not include status, audit, verification, or registry evidence.
- Recommended action: Add status_record, audit_log, verification_log, or registry_entry to make revocation independently inspectable.

### registration-agent — `weak_revocation_evidence`

- Severity: **high**
- Source: `glossary/terms/registration-agent.yaml`
- Finding: Revocation is supported but evidence does not include status, audit, verification, or registry evidence.
- Recommended action: Add status_record, audit_log, verification_log, or registry_entry to make revocation independently inspectable.

### role-based-access-control — `weak_revocation_evidence`

- Severity: **high**
- Source: `glossary/terms/role-based-access-control.yaml`
- Finding: Revocation is supported but evidence does not include status, audit, verification, or registry evidence.
- Recommended action: Add status_record, audit_log, verification_log, or registry_entry to make revocation independently inspectable.

### role-credential — `weak_revocation_evidence`

- Severity: **high**
- Source: `glossary/terms/role-credential.yaml`
- Finding: Revocation is supported but evidence does not include status, audit, verification, or registry evidence.
- Recommended action: Add status_record, audit_log, verification_log, or registry_entry to make revocation independently inspectable.

### schema — `weak_revocation_evidence`

- Severity: **high**
- Source: `glossary/terms/schema.yaml`
- Finding: Revocation is supported but evidence does not include status, audit, verification, or registry evidence.
- Recommended action: Add status_record, audit_log, verification_log, or registry_entry to make revocation independently inspectable.

### second-party — `weak_revocation_evidence`

- Severity: **high**
- Source: `glossary/terms/second-party.yaml`
- Finding: Revocation is supported but evidence does not include status, audit, verification, or registry evidence.
- Recommended action: Add status_record, audit_log, verification_log, or registry_entry to make revocation independently inspectable.

### self-asserted — `weak_revocation_evidence`

- Severity: **high**
- Source: `glossary/terms/self-asserted.yaml`
- Finding: Revocation is supported but evidence does not include status, audit, verification, or registry evidence.
- Recommended action: Add status_record, audit_log, verification_log, or registry_entry to make revocation independently inspectable.

### self-sovereign-identity — `weak_revocation_evidence`

- Severity: **high**
- Source: `glossary/terms/self-sovereign-identity.yaml`
- Finding: Revocation is supported but evidence does not include status, audit, verification, or registry evidence.
- Recommended action: Add status_record, audit_log, verification_log, or registry_entry to make revocation independently inspectable.

### subject — `weak_revocation_evidence`

- Severity: **high**
- Source: `glossary/terms/subject.yaml`
- Finding: Revocation is supported but evidence does not include status, audit, verification, or registry evidence.
- Recommended action: Add status_record, audit_log, verification_log, or registry_entry to make revocation independently inspectable.

### timestamp — `weak_revocation_evidence`

- Severity: **high**
- Source: `glossary/terms/timestamp.yaml`
- Finding: Revocation is supported but evidence does not include status, audit, verification, or registry evidence.
- Recommended action: Add status_record, audit_log, verification_log, or registry_entry to make revocation independently inspectable.

### transitive-trust-decision — `weak_revocation_evidence`

- Severity: **high**
- Source: `glossary/terms/transitive-trust-decision.yaml`
- Finding: Revocation is supported but evidence does not include status, audit, verification, or registry evidence.
- Recommended action: Add status_record, audit_log, verification_log, or registry_entry to make revocation independently inspectable.

### trust-chain — `weak_revocation_evidence`

- Severity: **high**
- Source: `glossary/terms/trust-chain.yaml`
- Finding: Revocation is supported but evidence does not include status, audit, verification, or registry evidence.
- Recommended action: Add status_record, audit_log, verification_log, or registry_entry to make revocation independently inspectable.

### trust-establishment — `weak_revocation_evidence`

- Severity: **high**
- Source: `glossary/terms/trust-establishment.yaml`
- Finding: Revocation is supported but evidence does not include status, audit, verification, or registry evidence.
- Recommended action: Add status_record, audit_log, verification_log, or registry_entry to make revocation independently inspectable.

### trusted-timestamp-authority — `weak_revocation_evidence`

- Severity: **high**
- Source: `glossary/terms/trusted-timestamp-authority.yaml`
- Finding: Revocation is supported but evidence does not include status, audit, verification, or registry evidence.
- Recommended action: Add status_record, audit_log, verification_log, or registry_entry to make revocation independently inspectable.

### tta — `weak_revocation_evidence`

- Severity: **high**
- Source: `glossary/terms/tta.yaml`
- Finding: Revocation is supported but evidence does not include status, audit, verification, or registry evidence.
- Recommended action: Add status_record, audit_log, verification_log, or registry_entry to make revocation independently inspectable.

### utility-governance-framework — `weak_revocation_evidence`

- Severity: **high**
- Source: `glossary/terms/utility-governance-framework.yaml`
- Finding: Revocation is supported but evidence does not include status, audit, verification, or registry evidence.
- Recommended action: Add status_record, audit_log, verification_log, or registry_entry to make revocation independently inspectable.

### vc — `weak_revocation_evidence`

- Severity: **high**
- Source: `glossary/terms/vc.yaml`
- Finding: Revocation is supported but evidence does not include status, audit, verification, or registry evidence.
- Recommended action: Add status_record, audit_log, verification_log, or registry_entry to make revocation independently inspectable.

### verifiable — `weak_revocation_evidence`

- Severity: **high**
- Source: `glossary/terms/verifiable.yaml`
- Finding: Revocation is supported but evidence does not include status, audit, verification, or registry evidence.
- Recommended action: Add status_record, audit_log, verification_log, or registry_entry to make revocation independently inspectable.

### verifiable-credential — `weak_revocation_evidence`

- Severity: **high**
- Source: `glossary/terms/verifiable-credential.yaml`
- Finding: Revocation is supported but evidence does not include status, audit, verification, or registry evidence.
- Recommended action: Add status_record, audit_log, verification_log, or registry_entry to make revocation independently inspectable.

### virtual-credential — `weak_revocation_evidence`

- Severity: **high**
- Source: `glossary/terms/virtual-credential.yaml`
- Finding: Revocation is supported but evidence does not include status, audit, verification, or registry evidence.
- Recommended action: Add status_record, audit_log, verification_log, or registry_entry to make revocation independently inspectable.

### w3c-verifiable-credentials-data-model-specification — `weak_revocation_evidence`

- Severity: **high**
- Source: `glossary/terms/w3c-verifiable-credentials-data-model-specification.yaml`
- Finding: Revocation is supported but evidence does not include status, audit, verification, or registry evidence.
- Recommended action: Add status_record, audit_log, verification_log, or registry_entry to make revocation independently inspectable.

### abac — `generic_evidence`

- Severity: **medium**
- Source: `glossary/terms/abac.yaml`
- Finding: Operational or governance-supporting term only references generic definition-change evidence.
- Recommended action: Add operational evidence such as policy_document, registry_entry, verification_log, status_record, audit_log, or delegation_record as applicable.

### acceptance — `generic_evidence`

- Severity: **medium**
- Source: `glossary/terms/acceptance.yaml`
- Finding: Operational or governance-supporting term only references generic definition-change evidence.
- Recommended action: Add operational evidence such as policy_document, registry_entry, verification_log, status_record, audit_log, or delegation_record as applicable.

### acceptance-network — `generic_evidence`

- Severity: **medium**
- Source: `glossary/terms/acceptance-network.yaml`
- Finding: Operational or governance-supporting term only references generic definition-change evidence.
- Recommended action: Add operational evidence such as policy_document, registry_entry, verification_log, status_record, audit_log, or delegation_record as applicable.

### accreditation — `generic_evidence`

- Severity: **medium**
- Source: `glossary/terms/accreditation.yaml`
- Finding: Operational or governance-supporting term only references generic definition-change evidence.
- Recommended action: Add operational evidence such as policy_document, registry_entry, verification_log, status_record, audit_log, or delegation_record as applicable.

### administering-authority — `generic_evidence`

- Severity: **medium**
- Source: `glossary/terms/administering-authority.yaml`
- Finding: Operational or governance-supporting term only references generic definition-change evidence.
- Recommended action: Add operational evidence such as policy_document, registry_entry, verification_log, status_record, audit_log, or delegation_record as applicable.

### appropriate-friction — `generic_evidence`

- Severity: **medium**
- Source: `glossary/terms/appropriate-friction.yaml`
- Finding: Operational or governance-supporting term only references generic definition-change evidence.
- Recommended action: Add operational evidence such as policy_document, registry_entry, verification_log, status_record, audit_log, or delegation_record as applicable.

### attributional-trust — `generic_evidence`

- Severity: **medium**
- Source: `glossary/terms/attributional-trust.yaml`
- Finding: Operational or governance-supporting term only references generic definition-change evidence.
- Recommended action: Add operational evidence such as policy_document, registry_entry, verification_log, status_record, audit_log, or delegation_record as applicable.

### authenticity — `generic_evidence`

- Severity: **medium**
- Source: `glossary/terms/authenticity.yaml`
- Finding: Operational or governance-supporting term only references generic definition-change evidence.
- Recommended action: Add operational evidence such as policy_document, registry_entry, verification_log, status_record, audit_log, or delegation_record as applicable.

### authoritative — `generic_evidence`

- Severity: **medium**
- Source: `glossary/terms/authoritative.yaml`
- Finding: Operational or governance-supporting term only references generic definition-change evidence.
- Recommended action: Add operational evidence such as policy_document, registry_entry, verification_log, status_record, audit_log, or delegation_record as applicable.

### autonomic-identity-system — `generic_evidence`

- Severity: **medium**
- Source: `glossary/terms/autonomic-identity-system.yaml`
- Finding: Operational or governance-supporting term only references generic definition-change evidence.
- Recommended action: Add operational evidence such as policy_document, registry_entry, verification_log, status_record, audit_log, or delegation_record as applicable.

### autonomic-namespace — `generic_evidence`

- Severity: **medium**
- Source: `glossary/terms/autonomic-namespace.yaml`
- Finding: Operational or governance-supporting term only references generic definition-change evidence.
- Recommended action: Add operational evidence such as policy_document, registry_entry, verification_log, status_record, audit_log, or delegation_record as applicable.

### broadcast-address — `generic_evidence`

- Severity: **medium**
- Source: `glossary/terms/broadcast-address.yaml`
- Finding: Operational or governance-supporting term only references generic definition-change evidence.
- Recommended action: Add operational evidence such as policy_document, registry_entry, verification_log, status_record, audit_log, or delegation_record as applicable.

### ca — `generic_evidence`

- Severity: **medium**
- Source: `glossary/terms/ca.yaml`
- Finding: Operational or governance-supporting term only references generic definition-change evidence.
- Recommended action: Add operational evidence such as policy_document, registry_entry, verification_log, status_record, audit_log, or delegation_record as applicable.

### certification — `generic_evidence`

- Severity: **medium**
- Source: `glossary/terms/certification.yaml`
- Finding: Operational or governance-supporting term only references generic definition-change evidence.
- Recommended action: Add operational evidence such as policy_document, registry_entry, verification_log, status_record, audit_log, or delegation_record as applicable.

### certification-authority — `generic_evidence`

- Severity: **medium**
- Source: `glossary/terms/certification-authority.yaml`
- Finding: Operational or governance-supporting term only references generic definition-change evidence.
- Recommended action: Add operational evidence such as policy_document, registry_entry, verification_log, status_record, audit_log, or delegation_record as applicable.

### chain-of-trust — `generic_evidence`

- Severity: **medium**
- Source: `glossary/terms/chain-of-trust.yaml`
- Finding: Operational or governance-supporting term only references generic definition-change evidence.
- Recommended action: Add operational evidence such as policy_document, registry_entry, verification_log, status_record, audit_log, or delegation_record as applicable.

### chaining — `generic_evidence`

- Severity: **medium**
- Source: `glossary/terms/chaining.yaml`
- Finding: Operational or governance-supporting term only references generic definition-change evidence.
- Recommended action: Add operational evidence such as policy_document, registry_entry, verification_log, status_record, audit_log, or delegation_record as applicable.

### confidentiality — `generic_evidence`

- Severity: **medium**
- Source: `glossary/terms/confidentiality.yaml`
- Finding: Operational or governance-supporting term only references generic definition-change evidence.
- Recommended action: Add operational evidence such as policy_document, registry_entry, verification_log, status_record, audit_log, or delegation_record as applicable.

### control-authority — `generic_evidence`

- Severity: **medium**
- Source: `glossary/terms/control-authority.yaml`
- Finding: Operational or governance-supporting term only references generic definition-change evidence.
- Recommended action: Add operational evidence such as policy_document, registry_entry, verification_log, status_record, audit_log, or delegation_record as applicable.

### controlled-document — `generic_evidence`

- Severity: **medium**
- Source: `glossary/terms/controlled-document.yaml`
- Finding: Operational or governance-supporting term only references generic definition-change evidence.
- Recommended action: Add operational evidence such as policy_document, registry_entry, verification_log, status_record, audit_log, or delegation_record as applicable.

### correlation-privacy — `generic_evidence`

- Severity: **medium**
- Source: `glossary/terms/correlation-privacy.yaml`
- Finding: Operational or governance-supporting term only references generic definition-change evidence.
- Recommended action: Add operational evidence such as policy_document, registry_entry, verification_log, status_record, audit_log, or delegation_record as applicable.

### cryptographic-trust — `generic_evidence`

- Severity: **medium**
- Source: `glossary/terms/cryptographic-trust.yaml`
- Finding: Operational or governance-supporting term only references generic definition-change evidence.
- Recommended action: Add operational evidence such as policy_document, registry_entry, verification_log, status_record, audit_log, or delegation_record as applicable.

### custodial-wallet — `generic_evidence`

- Severity: **medium**
- Source: `glossary/terms/custodial-wallet.yaml`
- Finding: Operational or governance-supporting term only references generic definition-change evidence.
- Recommended action: Add operational evidence such as policy_document, registry_entry, verification_log, status_record, audit_log, or delegation_record as applicable.

### custodian — `generic_evidence`

- Severity: **medium**
- Source: `glossary/terms/custodian.yaml`
- Finding: Operational or governance-supporting term only references generic definition-change evidence.
- Recommended action: Add operational evidence such as policy_document, registry_entry, verification_log, status_record, audit_log, or delegation_record as applicable.

### data-packet — `generic_evidence`

- Severity: **medium**
- Source: `glossary/terms/data-packet.yaml`
- Finding: Operational or governance-supporting term only references generic definition-change evidence.
- Recommended action: Add operational evidence such as policy_document, registry_entry, verification_log, status_record, audit_log, or delegation_record as applicable.

### decentralized-identifier — `generic_evidence`

- Severity: **medium**
- Source: `glossary/terms/decentralized-identifier.yaml`
- Finding: Operational or governance-supporting term only references generic definition-change evidence.
- Recommended action: Add operational evidence such as policy_document, registry_entry, verification_log, status_record, audit_log, or delegation_record as applicable.

### decentralized-identity — `generic_evidence`

- Severity: **medium**
- Source: `glossary/terms/decentralized-identity.yaml`
- Finding: Operational or governance-supporting term only references generic definition-change evidence.
- Recommended action: Add operational evidence such as policy_document, registry_entry, verification_log, status_record, audit_log, or delegation_record as applicable.

### device-controller — `generic_evidence`

- Severity: **medium**
- Source: `glossary/terms/device-controller.yaml`
- Finding: Operational or governance-supporting term only references generic definition-change evidence.
- Recommended action: Add operational evidence such as policy_document, registry_entry, verification_log, status_record, audit_log, or delegation_record as applicable.

### digital-rights-management — `generic_evidence`

- Severity: **medium**
- Source: `glossary/terms/digital-rights-management.yaml`
- Finding: Operational or governance-supporting term only references generic definition-change evidence.
- Recommended action: Add operational evidence such as policy_document, registry_entry, verification_log, status_record, audit_log, or delegation_record as applicable.

### end-verifiable — `generic_evidence`

- Severity: **medium**
- Source: `glossary/terms/end-verifiable.yaml`
- Finding: Operational or governance-supporting term only references generic definition-change evidence.
- Recommended action: Add operational evidence such as policy_document, registry_entry, verification_log, status_record, audit_log, or delegation_record as applicable.

### enterprise-data-vault — `generic_evidence`

- Severity: **medium**
- Source: `glossary/terms/enterprise-data-vault.yaml`
- Finding: Operational or governance-supporting term only references generic definition-change evidence.
- Recommended action: Add operational evidence such as policy_document, registry_entry, verification_log, status_record, audit_log, or delegation_record as applicable.

### enterprise-wallet — `generic_evidence`

- Severity: **medium**
- Source: `glossary/terms/enterprise-wallet.yaml`
- Finding: Operational or governance-supporting term only references generic definition-change evidence.
- Recommended action: Add operational evidence such as policy_document, registry_entry, verification_log, status_record, audit_log, or delegation_record as applicable.

### federated-identity — `generic_evidence`

- Severity: **medium**
- Source: `glossary/terms/federated-identity.yaml`
- Finding: Operational or governance-supporting term only references generic definition-change evidence.
- Recommended action: Add operational evidence such as policy_document, registry_entry, verification_log, status_record, audit_log, or delegation_record as applicable.

### fiduciary — `generic_evidence`

- Severity: **medium**
- Source: `glossary/terms/fiduciary.yaml`
- Finding: Operational or governance-supporting term only references generic definition-change evidence.
- Recommended action: Add operational evidence such as policy_document, registry_entry, verification_log, status_record, audit_log, or delegation_record as applicable.

### first-party — `generic_evidence`

- Severity: **medium**
- Source: `glossary/terms/first-party.yaml`
- Finding: Operational or governance-supporting term only references generic definition-change evidence.
- Recommended action: Add operational evidence such as policy_document, registry_entry, verification_log, status_record, audit_log, or delegation_record as applicable.

### fourth-party — `generic_evidence`

- Severity: **medium**
- Source: `glossary/terms/fourth-party.yaml`
- Finding: Operational or governance-supporting term only references generic definition-change evidence.
- Recommended action: Add operational evidence such as policy_document, registry_entry, verification_log, status_record, audit_log, or delegation_record as applicable.

### general-data-protection-regulation — `generic_evidence`

- Severity: **medium**
- Source: `glossary/terms/general-data-protection-regulation.yaml`
- Finding: Operational or governance-supporting term only references generic definition-change evidence.
- Recommended action: Add operational evidence such as policy_document, registry_entry, verification_log, status_record, audit_log, or delegation_record as applicable.

### governance — `generic_evidence`

- Severity: **medium**
- Source: `glossary/terms/governance.yaml`
- Finding: Operational or governance-supporting term only references generic definition-change evidence.
- Recommended action: Add operational evidence such as policy_document, registry_entry, verification_log, status_record, audit_log, or delegation_record as applicable.

### governance-risk-management-compliance — `generic_evidence`

- Severity: **medium**
- Source: `glossary/terms/governance-risk-management-compliance.yaml`
- Finding: Operational or governance-supporting term only references generic definition-change evidence.
- Recommended action: Add operational evidence such as policy_document, registry_entry, verification_log, status_record, audit_log, or delegation_record as applicable.

### governing-authority — `generic_evidence`

- Severity: **medium**
- Source: `glossary/terms/governing-authority.yaml`
- Finding: Operational or governance-supporting term only references generic definition-change evidence.
- Recommended action: Add operational evidence such as policy_document, registry_entry, verification_log, status_record, audit_log, or delegation_record as applicable.

### grc — `generic_evidence`

- Severity: **medium**
- Source: `glossary/terms/grc.yaml`
- Finding: Operational or governance-supporting term only references generic definition-change evidence.
- Recommended action: Add operational evidence such as policy_document, registry_entry, verification_log, status_record, audit_log, or delegation_record as applicable.

### holder-binding — `generic_evidence`

- Severity: **medium**
- Source: `glossary/terms/holder-binding.yaml`
- Finding: Operational or governance-supporting term only references generic definition-change evidence.
- Recommended action: Add operational evidence such as policy_document, registry_entry, verification_log, status_record, audit_log, or delegation_record as applicable.

### human-experience — `generic_evidence`

- Severity: **medium**
- Source: `glossary/terms/human-experience.yaml`
- Finding: Operational or governance-supporting term only references generic definition-change evidence.
- Recommended action: Add operational evidence such as policy_document, registry_entry, verification_log, status_record, audit_log, or delegation_record as applicable.

### identity-controller — `generic_evidence`

- Severity: **medium**
- Source: `glossary/terms/identity-controller.yaml`
- Finding: Operational or governance-supporting term only references generic definition-change evidence.
- Recommended action: Add operational evidence such as policy_document, registry_entry, verification_log, status_record, audit_log, or delegation_record as applicable.

### intermediary-system — `generic_evidence`

- Severity: **medium**
- Source: `glossary/terms/intermediary-system.yaml`
- Finding: Operational or governance-supporting term only references generic definition-change evidence.
- Recommended action: Add operational evidence such as policy_document, registry_entry, verification_log, status_record, audit_log, or delegation_record as applicable.

### jurisdiction — `generic_evidence`

- Severity: **medium**
- Source: `glossary/terms/jurisdiction.yaml`
- Finding: Operational or governance-supporting term only references generic definition-change evidence.
- Recommended action: Add operational evidence such as policy_document, registry_entry, verification_log, status_record, audit_log, or delegation_record as applicable.

### key-management-system — `generic_evidence`

- Severity: **medium**
- Source: `glossary/terms/key-management-system.yaml`
- Finding: Operational or governance-supporting term only references generic definition-change evidence.
- Recommended action: Add operational evidence such as policy_document, registry_entry, verification_log, status_record, audit_log, or delegation_record as applicable.

### legal-entity — `generic_evidence`

- Severity: **medium**
- Source: `glossary/terms/legal-entity.yaml`
- Finding: Operational or governance-supporting term only references generic definition-change evidence.
- Recommended action: Add operational evidence such as policy_document, registry_entry, verification_log, status_record, audit_log, or delegation_record as applicable.

### legal-entity-identifier — `generic_evidence`

- Severity: **medium**
- Source: `glossary/terms/legal-entity-identifier.yaml`
- Finding: Operational or governance-supporting term only references generic definition-change evidence.
- Recommended action: Add operational evidence such as policy_document, registry_entry, verification_log, status_record, audit_log, or delegation_record as applicable.

### locus-of-control — `generic_evidence`

- Severity: **medium**
- Source: `glossary/terms/locus-of-control.yaml`
- Finding: Operational or governance-supporting term only references generic definition-change evidence.
- Recommended action: Add operational evidence such as policy_document, registry_entry, verification_log, status_record, audit_log, or delegation_record as applicable.

### multi-party-control — `generic_evidence`

- Severity: **medium**
- Source: `glossary/terms/multi-party-control.yaml`
- Finding: Operational or governance-supporting term only references generic definition-change evidence.
- Recommended action: Add operational evidence such as policy_document, registry_entry, verification_log, status_record, audit_log, or delegation_record as applicable.

### non-custodial-wallet — `generic_evidence`

- Severity: **medium**
- Source: `glossary/terms/non-custodial-wallet.yaml`
- Finding: Operational or governance-supporting term only references generic definition-change evidence.
- Recommended action: Add operational evidence such as policy_document, registry_entry, verification_log, status_record, audit_log, or delegation_record as applicable.

### non-transferable — `generic_evidence`

- Severity: **medium**
- Source: `glossary/terms/non-transferable.yaml`
- Finding: Operational or governance-supporting term only references generic definition-change evidence.
- Recommended action: Add operational evidence such as policy_document, registry_entry, verification_log, status_record, audit_log, or delegation_record as applicable.

### non-transferable-identifier — `generic_evidence`

- Severity: **medium**
- Source: `glossary/terms/non-transferable-identifier.yaml`
- Finding: Operational or governance-supporting term only references generic definition-change evidence.
- Recommended action: Add operational evidence such as policy_document, registry_entry, verification_log, status_record, audit_log, or delegation_record as applicable.

### organization — `generic_evidence`

- Severity: **medium**
- Source: `glossary/terms/organization.yaml`
- Finding: Operational or governance-supporting term only references generic definition-change evidence.
- Recommended action: Add operational evidence such as policy_document, registry_entry, verification_log, status_record, audit_log, or delegation_record as applicable.

### organizational-authority — `generic_evidence`

- Severity: **medium**
- Source: `glossary/terms/organizational-authority.yaml`
- Finding: Operational or governance-supporting term only references generic definition-change evidence.
- Recommended action: Add operational evidence such as policy_document, registry_entry, verification_log, status_record, audit_log, or delegation_record as applicable.

### owner — `generic_evidence`

- Severity: **medium**
- Source: `glossary/terms/owner.yaml`
- Finding: Operational or governance-supporting term only references generic definition-change evidence.
- Recommended action: Add operational evidence such as policy_document, registry_entry, verification_log, status_record, audit_log, or delegation_record as applicable.

### personal-data-vault — `generic_evidence`

- Severity: **medium**
- Source: `glossary/terms/personal-data-vault.yaml`
- Finding: Operational or governance-supporting term only references generic definition-change evidence.
- Recommended action: Add operational evidence such as policy_document, registry_entry, verification_log, status_record, audit_log, or delegation_record as applicable.

### personal-wallet — `generic_evidence`

- Severity: **medium**
- Source: `glossary/terms/personal-wallet.yaml`
- Finding: Operational or governance-supporting term only references generic definition-change evidence.
- Recommended action: Add operational evidence such as policy_document, registry_entry, verification_log, status_record, audit_log, or delegation_record as applicable.

### private-key — `generic_evidence`

- Severity: **medium**
- Source: `glossary/terms/private-key.yaml`
- Finding: Operational or governance-supporting term only references generic definition-change evidence.
- Recommended action: Add operational evidence such as policy_document, registry_entry, verification_log, status_record, audit_log, or delegation_record as applicable.

### proof-of-control — `generic_evidence`

- Severity: **medium**
- Source: `glossary/terms/proof-of-control.yaml`
- Finding: Operational or governance-supporting term only references generic definition-change evidence.
- Recommended action: Add operational evidence such as policy_document, registry_entry, verification_log, status_record, audit_log, or delegation_record as applicable.

### protected-data — `generic_evidence`

- Severity: **medium**
- Source: `glossary/terms/protected-data.yaml`
- Finding: Operational or governance-supporting term only references generic definition-change evidence.
- Recommended action: Add operational evidence such as policy_document, registry_entry, verification_log, status_record, audit_log, or delegation_record as applicable.

### public-key — `generic_evidence`

- Severity: **medium**
- Source: `glossary/terms/public-key.yaml`
- Finding: Operational or governance-supporting term only references generic definition-change evidence.
- Recommended action: Add operational evidence such as policy_document, registry_entry, verification_log, status_record, audit_log, or delegation_record as applicable.

### public-key-certificate — `generic_evidence`

- Severity: **medium**
- Source: `glossary/terms/public-key-certificate.yaml`
- Finding: Operational or governance-supporting term only references generic definition-change evidence.
- Recommended action: Add operational evidence such as policy_document, registry_entry, verification_log, status_record, audit_log, or delegation_record as applicable.

### rbac — `generic_evidence`

- Severity: **medium**
- Source: `glossary/terms/rbac.yaml`
- Finding: Operational or governance-supporting term only references generic definition-change evidence.
- Recommended action: Add operational evidence such as policy_document, registry_entry, verification_log, status_record, audit_log, or delegation_record as applicable.

### relationship-context — `generic_evidence`

- Severity: **medium**
- Source: `glossary/terms/relationship-context.yaml`
- Finding: Operational or governance-supporting term only references generic definition-change evidence.
- Recommended action: Add operational evidence such as policy_document, registry_entry, verification_log, status_record, audit_log, or delegation_record as applicable.

### reputation — `generic_evidence`

- Severity: **medium**
- Source: `glossary/terms/reputation.yaml`
- Finding: Operational or governance-supporting term only references generic definition-change evidence.
- Recommended action: Add operational evidence such as policy_document, registry_entry, verification_log, status_record, audit_log, or delegation_record as applicable.

### reputation-graph — `generic_evidence`

- Severity: **medium**
- Source: `glossary/terms/reputation-graph.yaml`
- Finding: Operational or governance-supporting term only references generic definition-change evidence.
- Recommended action: Add operational evidence such as policy_document, registry_entry, verification_log, status_record, audit_log, or delegation_record as applicable.

### reputation-system — `generic_evidence`

- Severity: **medium**
- Source: `glossary/terms/reputation-system.yaml`
- Finding: Operational or governance-supporting term only references generic definition-change evidence.
- Recommended action: Add operational evidence such as policy_document, registry_entry, verification_log, status_record, audit_log, or delegation_record as applicable.

### requirement — `generic_evidence`

- Severity: **medium**
- Source: `glossary/terms/requirement.yaml`
- Finding: Operational or governance-supporting term only references generic definition-change evidence.
- Recommended action: Add operational evidence such as policy_document, registry_entry, verification_log, status_record, audit_log, or delegation_record as applicable.

### resolver — `generic_evidence`

- Severity: **medium**
- Source: `glossary/terms/resolver.yaml`
- Finding: Operational or governance-supporting term only references generic definition-change evidence.
- Recommended action: Add operational evidence such as policy_document, registry_entry, verification_log, status_record, audit_log, or delegation_record as applicable.

### risk-assessment — `generic_evidence`

- Severity: **medium**
- Source: `glossary/terms/risk-assessment.yaml`
- Finding: Operational or governance-supporting term only references generic definition-change evidence.
- Recommended action: Add operational evidence such as policy_document, registry_entry, verification_log, status_record, audit_log, or delegation_record as applicable.

### risk-decision — `generic_evidence`

- Severity: **medium**
- Source: `glossary/terms/risk-decision.yaml`
- Finding: Operational or governance-supporting term only references generic definition-change evidence.
- Recommended action: Add operational evidence such as policy_document, registry_entry, verification_log, status_record, audit_log, or delegation_record as applicable.

### risk-mitigation — `generic_evidence`

- Severity: **medium**
- Source: `glossary/terms/risk-mitigation.yaml`
- Finding: Operational or governance-supporting term only references generic definition-change evidence.
- Recommended action: Add operational evidence such as policy_document, registry_entry, verification_log, status_record, audit_log, or delegation_record as applicable.

### secure-enclave — `generic_evidence`

- Severity: **medium**
- Source: `glossary/terms/secure-enclave.yaml`
- Finding: Operational or governance-supporting term only references generic definition-change evidence.
- Recommended action: Add operational evidence such as policy_document, registry_entry, verification_log, status_record, audit_log, or delegation_record as applicable.

### single-signature-identifier — `generic_evidence`

- Severity: **medium**
- Source: `glossary/terms/single-signature-identifier.yaml`
- Finding: Operational or governance-supporting term only references generic definition-change evidence.
- Recommended action: Add operational evidence such as policy_document, registry_entry, verification_log, status_record, audit_log, or delegation_record as applicable.

### supporting-system — `generic_evidence`

- Severity: **medium**
- Source: `glossary/terms/supporting-system.yaml`
- Finding: Operational or governance-supporting term only references generic definition-change evidence.
- Recommended action: Add operational evidence such as policy_document, registry_entry, verification_log, status_record, audit_log, or delegation_record as applicable.

### technical-requirement — `generic_evidence`

- Severity: **medium**
- Source: `glossary/terms/technical-requirement.yaml`
- Finding: Operational or governance-supporting term only references generic definition-change evidence.
- Recommended action: Add operational evidence such as policy_document, registry_entry, verification_log, status_record, audit_log, or delegation_record as applicable.

### tee — `generic_evidence`

- Severity: **medium**
- Source: `glossary/terms/tee.yaml`
- Finding: Operational or governance-supporting term only references generic definition-change evidence.
- Recommended action: Add operational evidence such as policy_document, registry_entry, verification_log, status_record, audit_log, or delegation_record as applicable.

### third-party — `generic_evidence`

- Severity: **medium**
- Source: `glossary/terms/third-party.yaml`
- Finding: Operational or governance-supporting term only references generic definition-change evidence.
- Recommended action: Add operational evidence such as policy_document, registry_entry, verification_log, status_record, audit_log, or delegation_record as applicable.

### toip — `generic_evidence`

- Severity: **medium**
- Source: `glossary/terms/toip.yaml`
- Finding: Operational or governance-supporting term only references generic definition-change evidence.
- Recommended action: Add operational evidence such as policy_document, registry_entry, verification_log, status_record, audit_log, or delegation_record as applicable.

### toip-application — `generic_evidence`

- Severity: **medium**
- Source: `glossary/terms/toip-application.yaml`
- Finding: Operational or governance-supporting term only references generic definition-change evidence.
- Recommended action: Add operational evidence such as policy_document, registry_entry, verification_log, status_record, audit_log, or delegation_record as applicable.

### toip-controller — `generic_evidence`

- Severity: **medium**
- Source: `glossary/terms/toip-controller.yaml`
- Finding: Operational or governance-supporting term only references generic definition-change evidence.
- Recommended action: Add operational evidence such as policy_document, registry_entry, verification_log, status_record, audit_log, or delegation_record as applicable.

### toip-endpoint — `generic_evidence`

- Severity: **medium**
- Source: `glossary/terms/toip-endpoint.yaml`
- Finding: Operational or governance-supporting term only references generic definition-change evidence.
- Recommended action: Add operational evidence such as policy_document, registry_entry, verification_log, status_record, audit_log, or delegation_record as applicable.

### toip-foundation — `generic_evidence`

- Severity: **medium**
- Source: `glossary/terms/toip-foundation.yaml`
- Finding: Operational or governance-supporting term only references generic definition-change evidence.
- Recommended action: Add operational evidence such as policy_document, registry_entry, verification_log, status_record, audit_log, or delegation_record as applicable.

### toip-governance-architecture-specification — `generic_evidence`

- Severity: **medium**
- Source: `glossary/terms/toip-governance-architecture-specification.yaml`
- Finding: Operational or governance-supporting term only references generic definition-change evidence.
- Recommended action: Add operational evidence such as policy_document, registry_entry, verification_log, status_record, audit_log, or delegation_record as applicable.

### toip-governance-stack — `generic_evidence`

- Severity: **medium**
- Source: `glossary/terms/toip-governance-stack.yaml`
- Finding: Operational or governance-supporting term only references generic definition-change evidence.
- Recommended action: Add operational evidence such as policy_document, registry_entry, verification_log, status_record, audit_log, or delegation_record as applicable.

### toip-layer-1 — `generic_evidence`

- Severity: **medium**
- Source: `glossary/terms/toip-layer-1.yaml`
- Finding: Operational or governance-supporting term only references generic definition-change evidence.
- Recommended action: Add operational evidence such as policy_document, registry_entry, verification_log, status_record, audit_log, or delegation_record as applicable.

### toip-layer-2 — `generic_evidence`

- Severity: **medium**
- Source: `glossary/terms/toip-layer-2.yaml`
- Finding: Operational or governance-supporting term only references generic definition-change evidence.
- Recommended action: Add operational evidence such as policy_document, registry_entry, verification_log, status_record, audit_log, or delegation_record as applicable.

### toip-layer-3 — `generic_evidence`

- Severity: **medium**
- Source: `glossary/terms/toip-layer-3.yaml`
- Finding: Operational or governance-supporting term only references generic definition-change evidence.
- Recommended action: Add operational evidence such as policy_document, registry_entry, verification_log, status_record, audit_log, or delegation_record as applicable.

### toip-layer-4 — `generic_evidence`

- Severity: **medium**
- Source: `glossary/terms/toip-layer-4.yaml`
- Finding: Operational or governance-supporting term only references generic definition-change evidence.
- Recommended action: Add operational evidence such as policy_document, registry_entry, verification_log, status_record, audit_log, or delegation_record as applicable.

### toip-message — `generic_evidence`

- Severity: **medium**
- Source: `glossary/terms/toip-message.yaml`
- Finding: Operational or governance-supporting term only references generic definition-change evidence.
- Recommended action: Add operational evidence such as policy_document, registry_entry, verification_log, status_record, audit_log, or delegation_record as applicable.

### toip-relationship — `generic_evidence`

- Severity: **medium**
- Source: `glossary/terms/toip-relationship.yaml`
- Finding: Operational or governance-supporting term only references generic definition-change evidence.
- Recommended action: Add operational evidence such as policy_document, registry_entry, verification_log, status_record, audit_log, or delegation_record as applicable.

### toip-stack — `generic_evidence`

- Severity: **medium**
- Source: `glossary/terms/toip-stack.yaml`
- Finding: Operational or governance-supporting term only references generic definition-change evidence.
- Recommended action: Add operational evidence such as policy_document, registry_entry, verification_log, status_record, audit_log, or delegation_record as applicable.

### toip-trust-network — `generic_evidence`

- Severity: **medium**
- Source: `glossary/terms/toip-trust-network.yaml`
- Finding: Operational or governance-supporting term only references generic definition-change evidence.
- Recommended action: Add operational evidence such as policy_document, registry_entry, verification_log, status_record, audit_log, or delegation_record as applicable.

### toip-trust-spanning-protocol — `generic_evidence`

- Severity: **medium**
- Source: `glossary/terms/toip-trust-spanning-protocol.yaml`
- Finding: Operational or governance-supporting term only references generic definition-change evidence.
- Recommended action: Add operational evidence such as policy_document, registry_entry, verification_log, status_record, audit_log, or delegation_record as applicable.

### transferable-identifier — `generic_evidence`

- Severity: **medium**
- Source: `glossary/terms/transferable-identifier.yaml`
- Finding: Operational or governance-supporting term only references generic definition-change evidence.
- Recommended action: Add operational evidence such as policy_document, registry_entry, verification_log, status_record, audit_log, or delegation_record as applicable.

### trust — `generic_evidence`

- Severity: **medium**
- Source: `glossary/terms/trust.yaml`
- Finding: Operational or governance-supporting term only references generic definition-change evidence.
- Recommended action: Add operational evidence such as policy_document, registry_entry, verification_log, status_record, audit_log, or delegation_record as applicable.

### trust-anchor — `generic_evidence`

- Severity: **medium**
- Source: `glossary/terms/trust-anchor.yaml`
- Finding: Operational or governance-supporting term only references generic definition-change evidence.
- Recommended action: Add operational evidence such as policy_document, registry_entry, verification_log, status_record, audit_log, or delegation_record as applicable.

### trust-application — `generic_evidence`

- Severity: **medium**
- Source: `glossary/terms/trust-application.yaml`
- Finding: Operational or governance-supporting term only references generic definition-change evidence.
- Recommended action: Add operational evidence such as policy_document, registry_entry, verification_log, status_record, audit_log, or delegation_record as applicable.

### trust-application-layer — `generic_evidence`

- Severity: **medium**
- Source: `glossary/terms/trust-application-layer.yaml`
- Finding: Operational or governance-supporting term only references generic definition-change evidence.
- Recommended action: Add operational evidence such as policy_document, registry_entry, verification_log, status_record, audit_log, or delegation_record as applicable.

### trust-basis — `generic_evidence`

- Severity: **medium**
- Source: `glossary/terms/trust-basis.yaml`
- Finding: Operational or governance-supporting term only references generic definition-change evidence.
- Recommended action: Add operational evidence such as policy_document, registry_entry, verification_log, status_record, audit_log, or delegation_record as applicable.

### trust-boundary — `generic_evidence`

- Severity: **medium**
- Source: `glossary/terms/trust-boundary.yaml`
- Finding: Operational or governance-supporting term only references generic definition-change evidence.
- Recommended action: Add operational evidence such as policy_document, registry_entry, verification_log, status_record, audit_log, or delegation_record as applicable.

### trust-decision — `generic_evidence`

- Severity: **medium**
- Source: `glossary/terms/trust-decision.yaml`
- Finding: Operational or governance-supporting term only references generic definition-change evidence.
- Recommended action: Add operational evidence such as policy_document, registry_entry, verification_log, status_record, audit_log, or delegation_record as applicable.

### trust-ecosystem — `generic_evidence`

- Severity: **medium**
- Source: `glossary/terms/trust-ecosystem.yaml`
- Finding: Operational or governance-supporting term only references generic definition-change evidence.
- Recommended action: Add operational evidence such as policy_document, registry_entry, verification_log, status_record, audit_log, or delegation_record as applicable.

### trust-factor — `generic_evidence`

- Severity: **medium**
- Source: `glossary/terms/trust-factor.yaml`
- Finding: Operational or governance-supporting term only references generic definition-change evidence.
- Recommended action: Add operational evidence such as policy_document, registry_entry, verification_log, status_record, audit_log, or delegation_record as applicable.

### trust-limit — `generic_evidence`

- Severity: **medium**
- Source: `glossary/terms/trust-limit.yaml`
- Finding: Operational or governance-supporting term only references generic definition-change evidence.
- Recommended action: Add operational evidence such as policy_document, registry_entry, verification_log, status_record, audit_log, or delegation_record as applicable.

### trust-objective — `generic_evidence`

- Severity: **medium**
- Source: `glossary/terms/trust-objective.yaml`
- Finding: Operational or governance-supporting term only references generic definition-change evidence.
- Recommended action: Add operational evidence such as policy_document, registry_entry, verification_log, status_record, audit_log, or delegation_record as applicable.

### trust-over-ip — `generic_evidence`

- Severity: **medium**
- Source: `glossary/terms/trust-over-ip.yaml`
- Finding: Operational or governance-supporting term only references generic definition-change evidence.
- Recommended action: Add operational evidence such as policy_document, registry_entry, verification_log, status_record, audit_log, or delegation_record as applicable.

### trust-relationship — `generic_evidence`

- Severity: **medium**
- Source: `glossary/terms/trust-relationship.yaml`
- Finding: Operational or governance-supporting term only references generic definition-change evidence.
- Recommended action: Add operational evidence such as policy_document, registry_entry, verification_log, status_record, audit_log, or delegation_record as applicable.

### trust-root — `generic_evidence`

- Severity: **medium**
- Source: `glossary/terms/trust-root.yaml`
- Finding: Operational or governance-supporting term only references generic definition-change evidence.
- Recommended action: Add operational evidence such as policy_document, registry_entry, verification_log, status_record, audit_log, or delegation_record as applicable.

### trust-spanning-layer — `generic_evidence`

- Severity: **medium**
- Source: `glossary/terms/trust-spanning-layer.yaml`
- Finding: Operational or governance-supporting term only references generic definition-change evidence.
- Recommended action: Add operational evidence such as policy_document, registry_entry, verification_log, status_record, audit_log, or delegation_record as applicable.

### trust-spanning-protocol — `generic_evidence`

- Severity: **medium**
- Source: `glossary/terms/trust-spanning-protocol.yaml`
- Finding: Operational or governance-supporting term only references generic definition-change evidence.
- Recommended action: Add operational evidence such as policy_document, registry_entry, verification_log, status_record, audit_log, or delegation_record as applicable.

### trust-support — `generic_evidence`

- Severity: **medium**
- Source: `glossary/terms/trust-support.yaml`
- Finding: Operational or governance-supporting term only references generic definition-change evidence.
- Recommended action: Add operational evidence such as policy_document, registry_entry, verification_log, status_record, audit_log, or delegation_record as applicable.

### trust-support-layer — `generic_evidence`

- Severity: **medium**
- Source: `glossary/terms/trust-support-layer.yaml`
- Finding: Operational or governance-supporting term only references generic definition-change evidence.
- Recommended action: Add operational evidence such as policy_document, registry_entry, verification_log, status_record, audit_log, or delegation_record as applicable.

### trust-task — `generic_evidence`

- Severity: **medium**
- Source: `glossary/terms/trust-task.yaml`
- Finding: Operational or governance-supporting term only references generic definition-change evidence.
- Recommended action: Add operational evidence such as policy_document, registry_entry, verification_log, status_record, audit_log, or delegation_record as applicable.

### trust-task-layer — `generic_evidence`

- Severity: **medium**
- Source: `glossary/terms/trust-task-layer.yaml`
- Finding: Operational or governance-supporting term only references generic definition-change evidence.
- Recommended action: Add operational evidence such as policy_document, registry_entry, verification_log, status_record, audit_log, or delegation_record as applicable.

### trust-task-protocol — `generic_evidence`

- Severity: **medium**
- Source: `glossary/terms/trust-task-protocol.yaml`
- Finding: Operational or governance-supporting term only references generic definition-change evidence.
- Recommended action: Add operational evidence such as policy_document, registry_entry, verification_log, status_record, audit_log, or delegation_record as applicable.

### trust-triangle — `generic_evidence`

- Severity: **medium**
- Source: `glossary/terms/trust-triangle.yaml`
- Finding: Operational or governance-supporting term only references generic definition-change evidence.
- Recommended action: Add operational evidence such as policy_document, registry_entry, verification_log, status_record, audit_log, or delegation_record as applicable.

### trusted-execution-environment — `generic_evidence`

- Severity: **medium**
- Source: `glossary/terms/trusted-execution-environment.yaml`
- Finding: Operational or governance-supporting term only references generic definition-change evidence.
- Recommended action: Add operational evidence such as policy_document, registry_entry, verification_log, status_record, audit_log, or delegation_record as applicable.

### trusted-role — `generic_evidence`

- Severity: **medium**
- Source: `glossary/terms/trusted-role.yaml`
- Finding: Operational or governance-supporting term only references generic definition-change evidence.
- Recommended action: Add operational evidence such as policy_document, registry_entry, verification_log, status_record, audit_log, or delegation_record as applicable.

### trusted-timestamp-authority — `generic_evidence`

- Severity: **medium**
- Source: `glossary/terms/trusted-timestamp-authority.yaml`
- Finding: Operational or governance-supporting term only references generic definition-change evidence.
- Recommended action: Add operational evidence such as policy_document, registry_entry, verification_log, status_record, audit_log, or delegation_record as applicable.

### trustworthiness — `generic_evidence`

- Severity: **medium**
- Source: `glossary/terms/trustworthiness.yaml`
- Finding: Operational or governance-supporting term only references generic definition-change evidence.
- Recommended action: Add operational evidence such as policy_document, registry_entry, verification_log, status_record, audit_log, or delegation_record as applicable.

### trustworthy — `generic_evidence`

- Severity: **medium**
- Source: `glossary/terms/trustworthy.yaml`
- Finding: Operational or governance-supporting term only references generic definition-change evidence.
- Recommended action: Add operational evidence such as policy_document, registry_entry, verification_log, status_record, audit_log, or delegation_record as applicable.

### tsp — `generic_evidence`

- Severity: **medium**
- Source: `glossary/terms/tsp.yaml`
- Finding: Operational or governance-supporting term only references generic definition-change evidence.
- Recommended action: Add operational evidence such as policy_document, registry_entry, verification_log, status_record, audit_log, or delegation_record as applicable.

### tta — `generic_evidence`

- Severity: **medium**
- Source: `glossary/terms/tta.yaml`
- Finding: Operational or governance-supporting term only references generic definition-change evidence.
- Recommended action: Add operational evidence such as policy_document, registry_entry, verification_log, status_record, audit_log, or delegation_record as applicable.

### ttp — `generic_evidence`

- Severity: **medium**
- Source: `glossary/terms/ttp.yaml`
- Finding: Operational or governance-supporting term only references generic definition-change evidence.
- Recommended action: Add operational evidence such as policy_document, registry_entry, verification_log, status_record, audit_log, or delegation_record as applicable.

### unicast — `generic_evidence`

- Severity: **medium**
- Source: `glossary/terms/unicast.yaml`
- Finding: Operational or governance-supporting term only references generic definition-change evidence.
- Recommended action: Add operational evidence such as policy_document, registry_entry, verification_log, status_record, audit_log, or delegation_record as applicable.

### verifiable-data — `generic_evidence`

- Severity: **medium**
- Source: `glossary/terms/verifiable-data.yaml`
- Finding: Operational or governance-supporting term only references generic definition-change evidence.
- Recommended action: Add operational evidence such as policy_document, registry_entry, verification_log, status_record, audit_log, or delegation_record as applicable.

### verifiable-identifier — `generic_evidence`

- Severity: **medium**
- Source: `glossary/terms/verifiable-identifier.yaml`
- Finding: Operational or governance-supporting term only references generic definition-change evidence.
- Recommended action: Add operational evidence such as policy_document, registry_entry, verification_log, status_record, audit_log, or delegation_record as applicable.

### vid-relationship — `generic_evidence`

- Severity: **medium**
- Source: `glossary/terms/vid-relationship.yaml`
- Finding: Operational or governance-supporting term only references generic definition-change evidence.
- Recommended action: Add operational evidence such as policy_document, registry_entry, verification_log, status_record, audit_log, or delegation_record as applicable.

### vid-to-vid — `generic_evidence`

- Severity: **medium**
- Source: `glossary/terms/vid-to-vid.yaml`
- Finding: Operational or governance-supporting term only references generic definition-change evidence.
- Recommended action: Add operational evidence such as policy_document, registry_entry, verification_log, status_record, audit_log, or delegation_record as applicable.

### witness — `generic_evidence`

- Severity: **medium**
- Source: `glossary/terms/witness.yaml`
- Finding: Operational or governance-supporting term only references generic definition-change evidence.
- Recommended action: Add operational evidence such as policy_document, registry_entry, verification_log, status_record, audit_log, or delegation_record as applicable.

### zero-knowledge-service — `generic_evidence`

- Severity: **medium**
- Source: `glossary/terms/zero-knowledge-service.yaml`
- Finding: Operational or governance-supporting term only references generic definition-change evidence.
- Recommended action: Add operational evidence such as policy_document, registry_entry, verification_log, status_record, audit_log, or delegation_record as applicable.

### zero-knowledge-service-provider — `generic_evidence`

- Severity: **medium**
- Source: `glossary/terms/zero-knowledge-service-provider.yaml`
- Finding: Operational or governance-supporting term only references generic definition-change evidence.
- Recommended action: Add operational evidence such as policy_document, registry_entry, verification_log, status_record, audit_log, or delegation_record as applicable.

### zero-trust-architecture — `generic_evidence`

- Severity: **medium**
- Source: `glossary/terms/zero-trust-architecture.yaml`
- Finding: Operational or governance-supporting term only references generic definition-change evidence.
- Recommended action: Add operational evidence such as policy_document, registry_entry, verification_log, status_record, audit_log, or delegation_record as applicable.

### biometric — `high_impact_informative`

- Severity: **medium**
- Source: `glossary/terms/biometric.yaml`
- Finding: High-impact decision point is paired with informative assurance hint.
- Recommended action: Use AL1+ or AL2+ when the term can affect authority, reliance, issuance, delegation, access, or revocation decisions.

### peer — `high_impact_informative`

- Severity: **medium**
- Source: `glossary/terms/peer.yaml`
- Finding: High-impact decision point is paired with informative assurance hint.
- Recommended action: Use AL1+ or AL2+ when the term can affect authority, reliance, issuance, delegation, access, or revocation decisions.

### self-certifying-identifier — `high_impact_informative`

- Severity: **medium**
- Source: `glossary/terms/self-certifying-identifier.yaml`
- Finding: High-impact decision point is paired with informative assurance hint.
- Recommended action: Use AL1+ or AL2+ when the term can affect authority, reliance, issuance, delegation, access, or revocation decisions.

### aal — `missing_sources`

- Severity: **medium**
- Source: `glossary/terms/aal.yaml`
- Finding: Term has no source references.
- Recommended action: Add a source reference, provenance note, or explicit maintainer rationale before relying on this term for assurance workflows.

### abac — `missing_sources`

- Severity: **medium**
- Source: `glossary/terms/abac.yaml`
- Finding: Term has no source references.
- Recommended action: Add a source reference, provenance note, or explicit maintainer rationale before relying on this term for assurance workflows.

### acceptance — `missing_sources`

- Severity: **medium**
- Source: `glossary/terms/acceptance.yaml`
- Finding: Term has no source references.
- Recommended action: Add a source reference, provenance note, or explicit maintainer rationale before relying on this term for assurance workflows.

### acceptance-network — `missing_sources`

- Severity: **medium**
- Source: `glossary/terms/acceptance-network.yaml`
- Finding: Term has no source references.
- Recommended action: Add a source reference, provenance note, or explicit maintainer rationale before relying on this term for assurance workflows.

### acdc — `missing_sources`

- Severity: **medium**
- Source: `glossary/terms/acdc.yaml`
- Finding: Term has no source references.
- Recommended action: Add a source reference, provenance note, or explicit maintainer rationale before relying on this term for assurance workflows.

### address — `missing_sources`

- Severity: **medium**
- Source: `glossary/terms/address.yaml`
- Finding: Term has no source references.
- Recommended action: Add a source reference, provenance note, or explicit maintainer rationale before relying on this term for assurance workflows.

### administering-authority — `missing_sources`

- Severity: **medium**
- Source: `glossary/terms/administering-authority.yaml`
- Finding: Term has no source references.
- Recommended action: Add a source reference, provenance note, or explicit maintainer rationale before relying on this term for assurance workflows.

### administering-body — `missing_sources`

- Severity: **medium**
- Source: `glossary/terms/administering-body.yaml`
- Finding: Term has no source references.
- Recommended action: Add a source reference, provenance note, or explicit maintainer rationale before relying on this term for assurance workflows.

### agency — `missing_sources`

- Severity: **medium**
- Source: `glossary/terms/agency.yaml`
- Finding: Term has no source references.
- Recommended action: Add a source reference, provenance note, or explicit maintainer rationale before relying on this term for assurance workflows.

### aid — `missing_sources`

- Severity: **medium**
- Source: `glossary/terms/aid.yaml`
- Finding: Term has no source references.
- Recommended action: Add a source reference, provenance note, or explicit maintainer rationale before relying on this term for assurance workflows.

### anonymous — `missing_sources`

- Severity: **medium**
- Source: `glossary/terms/anonymous.yaml`
- Finding: Term has no source references.
- Recommended action: Add a source reference, provenance note, or explicit maintainer rationale before relying on this term for assurance workflows.

### anycast-address — `missing_sources`

- Severity: **medium**
- Source: `glossary/terms/anycast-address.yaml`
- Finding: Term has no source references.
- Recommended action: Add a source reference, provenance note, or explicit maintainer rationale before relying on this term for assurance workflows.

### appraisability — `missing_sources`

- Severity: **medium**
- Source: `glossary/terms/appraisability.yaml`
- Finding: Term has no source references.
- Recommended action: Add a source reference, provenance note, or explicit maintainer rationale before relying on this term for assurance workflows.

### assurance-level — `missing_sources`

- Severity: **medium**
- Source: `glossary/terms/assurance-level.yaml`
- Finding: Term has no source references.
- Recommended action: Add a source reference, provenance note, or explicit maintainer rationale before relying on this term for assurance workflows.

### attribute — `missing_sources`

- Severity: **medium**
- Source: `glossary/terms/attribute.yaml`
- Finding: Term has no source references.
- Recommended action: Add a source reference, provenance note, or explicit maintainer rationale before relying on this term for assurance workflows.

### attributional-trust — `missing_sources`

- Severity: **medium**
- Source: `glossary/terms/attributional-trust.yaml`
- Finding: Term has no source references.
- Recommended action: Add a source reference, provenance note, or explicit maintainer rationale before relying on this term for assurance workflows.

### auditor — `missing_sources`

- Severity: **medium**
- Source: `glossary/terms/auditor.yaml`
- Finding: Term has no source references.
- Recommended action: Add a source reference, provenance note, or explicit maintainer rationale before relying on this term for assurance workflows.

### authentic-chained-data-container — `missing_sources`

- Severity: **medium**
- Source: `glossary/terms/authentic-chained-data-container.yaml`
- Finding: Term has no source references.
- Recommended action: Add a source reference, provenance note, or explicit maintainer rationale before relying on this term for assurance workflows.

### authoritative — `missing_sources`

- Severity: **medium**
- Source: `glossary/terms/authoritative.yaml`
- Finding: Term has no source references.
- Recommended action: Add a source reference, provenance note, or explicit maintainer rationale before relying on this term for assurance workflows.

### authoritative-source — `missing_sources`

- Severity: **medium**
- Source: `glossary/terms/authoritative-source.yaml`
- Finding: Term has no source references.
- Recommended action: Add a source reference, provenance note, or explicit maintainer rationale before relying on this term for assurance workflows.

### authorization-graph — `missing_sources`

- Severity: **medium**
- Source: `glossary/terms/authorization-graph.yaml`
- Finding: Term has no source references.
- Recommended action: Add a source reference, provenance note, or explicit maintainer rationale before relying on this term for assurance workflows.

### autonomic-identifier — `missing_sources`

- Severity: **medium**
- Source: `glossary/terms/autonomic-identifier.yaml`
- Finding: Term has no source references.
- Recommended action: Add a source reference, provenance note, or explicit maintainer rationale before relying on this term for assurance workflows.

### binding — `missing_sources`

- Severity: **medium**
- Source: `glossary/terms/binding.yaml`
- Finding: Term has no source references.
- Recommended action: Add a source reference, provenance note, or explicit maintainer rationale before relying on this term for assurance workflows.

### bola — `missing_sources`

- Severity: **medium**
- Source: `glossary/terms/bola.yaml`
- Finding: Term has no source references.
- Recommended action: Add a source reference, provenance note, or explicit maintainer rationale before relying on this term for assurance workflows.

### broken-object-level-authorization — `missing_sources`

- Severity: **medium**
- Source: `glossary/terms/broken-object-level-authorization.yaml`
- Finding: Term has no source references.
- Recommended action: Add a source reference, provenance note, or explicit maintainer rationale before relying on this term for assurance workflows.

### c2pa — `missing_sources`

- Severity: **medium**
- Source: `glossary/terms/c2pa.yaml`
- Finding: Term has no source references.
- Recommended action: Add a source reference, provenance note, or explicit maintainer rationale before relying on this term for assurance workflows.

### ca — `missing_sources`

- Severity: **medium**
- Source: `glossary/terms/ca.yaml`
- Finding: Term has no source references.
- Recommended action: Add a source reference, provenance note, or explicit maintainer rationale before relying on this term for assurance workflows.

### cai — `missing_sources`

- Severity: **medium**
- Source: `glossary/terms/cai.yaml`
- Finding: Term has no source references.
- Recommended action: Add a source reference, provenance note, or explicit maintainer rationale before relying on this term for assurance workflows.

### capability — `missing_sources`

- Severity: **medium**
- Source: `glossary/terms/capability.yaml`
- Finding: Term has no source references.
- Recommended action: Add a source reference, provenance note, or explicit maintainer rationale before relying on this term for assurance workflows.

### certificate — `missing_sources`

- Severity: **medium**
- Source: `glossary/terms/certificate.yaml`
- Finding: Term has no source references.
- Recommended action: Add a source reference, provenance note, or explicit maintainer rationale before relying on this term for assurance workflows.

### certification-authority — `missing_sources`

- Severity: **medium**
- Source: `glossary/terms/certification-authority.yaml`
- Finding: Term has no source references.
- Recommended action: Add a source reference, provenance note, or explicit maintainer rationale before relying on this term for assurance workflows.

### certification-body — `missing_sources`

- Severity: **medium**
- Source: `glossary/terms/certification-body.yaml`
- Finding: Term has no source references.
- Recommended action: Add a source reference, provenance note, or explicit maintainer rationale before relying on this term for assurance workflows.

### chain-of-trust — `missing_sources`

- Severity: **medium**
- Source: `glossary/terms/chain-of-trust.yaml`
- Finding: Term has no source references.
- Recommended action: Add a source reference, provenance note, or explicit maintainer rationale before relying on this term for assurance workflows.

Additional findings omitted from this markdown view: **737**. See `generated/json/governance-quality-report.json` for the complete machine-readable report.
