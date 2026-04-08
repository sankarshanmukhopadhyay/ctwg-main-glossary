# Main Glossary Review: Gaps and Improvement Areas

This review captures the main repository and content improvements needed to strengthen the glossary as an implementation asset, not only as a terminology reference.

| Category | Gap / Issue | Why It Matters | Proposed Improvement |
|---|---|---|---|
| Authority semantics | Core terms often describe actors but not the scope of authority they exercise | Implementers need to know who is permitted to decide, issue, revoke, or enforce | Add governance-aware metadata fields such as `authority_scope` and `accountable_actor` |
| Delegation semantics | Delegation is defined, but constraints, transfer boundaries, and revocation handling are not made explicit enough | Delegated authority without boundaries creates ambiguity and governance risk | Add explicit language around scope, duration, constraints, and revocation |
| Lifecycle semantics | Revocation, suspension, expiry, and replacement are unevenly represented | Glossary terms increasingly map to runtime systems where lifecycle state matters | Add lifecycle guidance and example machine-readable fields |
| Runtime enforcement | Terms often describe concepts statically rather than where enforcement happens | Governance becomes operational at execution time | Clarify control points, enforcement actors, and verification checkpoints |
| Evidence and auditability | Limited linkage from terms to audit evidence or proof artifacts | High-assurance deployments need evidence, not only shared vocabulary | Add example metadata for evidence artifacts and assurance-relevant signals |
| Trust registry specificity | Trust registries are defined at a high level but not strongly enough as governance decision-plane components | Trust registries frequently determine who is recognized, admitted, or relied upon | Expand trust-registry language to cover policy, criteria, publication, and lifecycle impact |
| Issuer and verifier roles | Roles are defined, but operational obligations and policy application could be sharper | These roles sit directly in the execution path of many trust decisions | Add clearer wording about policy application, acceptance criteria, and status checking |
| Policy model | Policy is present but does not fully foreground enforcement and machine readability | Modern trust systems increasingly depend on executable policy | Strengthen the definition so it supports both human and machine execution contexts |
| Developer guidance | Repository landing documentation is too thin for new contributors | Friction slows adoption and contribution quality | Expand README and add maintainer-facing guidance |
| Machine-readable pathway | The repo is human-readable first, but the extension path for machine-readable overlays is unclear | Machine-verifiable governance needs stable artifacts | Introduce schema and examples for governance-aware term profiles |
| Quality controls | There is no lightweight rubric for improving term quality consistently | Term quality can drift over time | Add a term-quality rubric and roadmap |
| Release discipline | Improvement work is not yet grouped into a structured incremental plan | Maintainers need a practical rollout path | Add a roadmap with phased adoption |
