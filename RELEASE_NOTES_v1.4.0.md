# CTWG Main Glossary v1.4.0 Release Notes

## Release summary

Version 1.4.0 closes a terminology gap between the CTWG Main Glossary and four actively evolving trust-infrastructure repositories: the Trust Systems Meta-Model, Trust Infrastructure Schemas, Trust Graph Artifacts, and the DTG ZKP Task Force workspace.

The release adds 36 normalized terms that are reusable across specifications, implementations, assurance profiles, and governance artifacts. It deliberately avoids turning every repository-local artifact name into a shared term. The inclusion threshold is cross-repository utility, stable semantics, and relevance to executable governance.

## New terminology coverage

### Runtime and interaction governance

The release adds terms for agent class, attention policy, authorization checkpoint, content provenance policy, control mode, dynamic authorization, extension contract, interaction context, interaction task, observability mode, opacity boundary, peer trust relation, service descriptor, skill contract, discovery governance, capability negotiation, and task evidence lifecycle.

### Authority and delegation

New terms cover delegation lineage, aggregation amplification, monotonic attenuation, authority boundary, runtime governance envelope, agent mandate envelope, and runtime authority envelope.

These definitions make delegation inspectable as a bounded chain of authority rather than a generic relationship between actors.

### Evidence and executable governance

The glossary now includes evidence artifact, decision receipt, evidence bundle, trust task execution receipt, proof-carrying commitment receipt, legitimacy gap, and control-plane shift.

These terms support machine-verifiable records of who had authority, what policy applied, what evidence was considered, what decision was made, and how that decision can be audited or revoked.

### Privacy-preserving proofs

The release adds personhood, nullifier, issuer concealment, unlinkability, and predicate proof. The definitions distinguish cryptographic proof properties from broader legal, civil-identity, or governance conclusions.

## GitHub Pages and Jekyll improvements

The generated Glossary Terms page is now a foldable navigation parent. Alphabet pages are visible, ordered children with deterministic `nav_order` values. Individual generated term pages remain excluded from the primary navigation to avoid an unusable 599-item sidebar.

The resulting navigation model is:

1. Home
2. Glossary Terms
   - Terms: A
   - Terms: B
   - continuing alphabetically
3. Governance Documentation
4. Machine-readable Artifacts

## Machine-readable artifacts

All new terms are included in the generated JSON and JSON-LD bundles, catalog, artifact manifest, governance inventory, Markdown exports, and Jekyll pages. Each term includes governance scope, lifecycle, revocation posture, evidence expectations, decision points, and accountability metadata.

## Assurance and validation

The release completed the following checks:

- 599 structured term files validated;
- 1,155 aliases checked for collisions;
- 80 structured source citations checked;
- schema and controlled vocabularies confirmed aligned;
- 599 Jekyll term pages regenerated;
- generated quality report completed with zero findings;
- quality score remained 100.0 out of 100; and
- GitHub Pages site built successfully with Jekyll.

## Adoption impact

Downstream repositories can now reference a shared vocabulary for runtime authority, interaction governance, delegation attenuation, decision evidence, privacy-proof properties, and control-plane legitimacy. This reduces semantic drift and makes cross-repository mappings more testable, reviewable, and automatable.
