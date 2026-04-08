# Publication Integration

The governance-executable layer is designed to coexist with the current Spec-Up publication workflow.

## Integration pattern

1. maintain `spec/terms-definitions/*.md` as the editorial source
2. maintain or regenerate `glossary/terms/*.yaml` as the machine-readable governance layer
3. validate structured artifacts in CI before publication
4. publish generated bundles as downloadable artifacts for assurance and interoperability tooling

## Compatibility rule

Human-readable publication remains authoritative for prose. Machine-readable governance overlays are authoritative for executable metadata fields.
