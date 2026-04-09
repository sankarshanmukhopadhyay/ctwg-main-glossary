---
title: "federation-assurance-level"
---

> Generated file. Update `glossary/terms/federation-assurance-level.yaml` and regenerate artifacts instead of editing this page directly.

# federation-assurance-level

## Definition
A category that describes the federation protocol used to communicate an assertion containing authentication) and attribute information (if applicable) to a relying party, as defined in NIST SP 800-63-3 in terms of three levels: FAL 1 (Some confidence), FAL 2 (High confidence), FAL 3 (Very high confidence).

## Aliases
federation assurance level, federation assurance levels, FAL, FALs

## Governance Profile
- **Authority scope**: verification_and_reliance, access_decisioning, assurance_and_audit
- **Delegation mode**: direct
- **Revocation supported**: False
- **Lifecycle states**: documented, active, deprecated
- **Execution role**: runtime
- **Control-plane role**: decision_plane_component

## Enforcement Points
- reliance_decision
- access_decision

## Assurance
**Evidence artifacts**
- verification_log
- attestation
- access_decision_log

- **Assurance level hint**: AL2+
- **Auditability**: high

## Control Plane
**Decision points**
- reliance_decision
- access_decision

- **Accountable entity**: glossary_maintainers

**Evidence produced**
- verification_log
- attestation
- access_decision_log

## Notes
Not specified

## Supporting Definitions
Not specified

## Mental Models
Not specified

## See Also
- authenticator assurance level
- identity assurance level.

## Crosswalk References
Not specified
