# AGENTS.md

Repository instructions for Codex, Hermes, OpenClaw, Claude Code, and other coding agents working on this repository.

## Mission

Maintain `fde-operator-os` as a compact, evidence-led Applied AI Operator OS that can:

- qualify an AI opportunity
- reconstruct operational reality
- design a bounded pilot
- make an explicit production-readiness decision
- operate and learn from a live loop
- distill reusable delivery and product assets

This is a skill, method, artifact, contract, and example repository. Keep application implementation in separate repositories.

## Read First

Before changing behavior, structure, or templates, read:

1. `README.md`
2. `SKILL.md`
3. `contracts/stages.json`
4. `contracts/artifacts.json`
5. `references/doctrine.md`
6. `references/fde-practice-system.md`
7. the relevant child skill under `skills/`
8. the relevant template under `assets/templates/`

For failure, governance, or production work, also read:

- `references/failure-patterns.md`
- `references/operator-heuristics.md`
- `references/engagement-modes.md`

For runtime or packaging changes, also read:

- `references/runtime-portability.md`
- `aliases/fde/SKILL.md`

## Repository Architecture

Keep these responsibilities distinct:

- `SKILL.md` — canonical doctrine and router
- `skills/` — lighter request-shaped execution skills
- `references/` — reusable doctrine, practice system, heuristics, and failure patterns
- `assets/templates/` — human-readable operator and control artifacts
- `contracts/stages.json` — canonical seven-stage registry
- `contracts/artifacts.json` — artifact, field, gate, alias, and source-of-truth registry
- `contracts/case-manifest.schema.json` — case-index contract
- `examples/` — synthetic, public, sanitized, or benchmark cases
- `tools/` — repository validation and maintenance utilities
- `tests/` — validation and contract regression tests
- `.github/workflows/` — continuous validation
- `aliases/` — runtime aliases and wrappers
- `agents/` — host-facing metadata

Add a top-level directory only when these boundaries cannot hold the work.

## Hard Boundaries

Do not turn this repository into:

- a web application
- a backend service
- a frontend implementation
- an OCR, PDF, ASR, TTS, or meeting-recording product
- a production browser automation system
- a generic prompt collection
- a broad consulting-template dump
- a container for private customer material

Domain implementation and private cases belong in separate repositories or private working context.

## Contract-First Change Protocol

When changing the delivery stages:

1. Update `contracts/stages.json` first.
2. Update the matching `SKILL.md` headings and README stage rows.
3. Keep artifact stage references and gate `after_stage` values valid.
4. Run stage-contract tests and the full repository check.

When adding or changing an artifact:

1. Update `contracts/artifacts.json`.
2. Update the canonical template under `assets/templates/`.
3. Update root and child Skill references.
4. Update a strict synthetic example when the artifact has one.
5. Update README or reference documentation when user-facing behavior changes.
6. Run the validator and tests.

When adding or changing a case:

1. Keep the case synthetic, public, or explicitly sanitized.
2. Add or update `case-manifest.json`.
3. Keep artifact IDs aligned with `contracts/artifacts.json`.
4. Record gate posture honestly: `go`, `conditional-go`, `no-go`, `hold`, or `not-run`.
5. Run the validator and tests.

## Canonical Paths And Compatibility

`assets/templates/state-action-evidence-model.md` is canonical.

`assets/templates/ontology-action-model.md` is a compatibility redirect. Do not duplicate fields or template content in the alias file.

When retaining any legacy path:

- declare the canonical path
- keep the alias thin
- add the alias to `contracts/artifacts.json`
- let the validator enforce the relationship

## Artifact Discipline

Operator-grade artifacts contain:

- a judgment or decision posture
- evidence separated from inference
- named unknowns and blockers
- owner and authority
- trigger, object, action, output, and proof where relevant
- fallback, rollback, audit, and exception handling where relevant
- acceptance or launch gate
- next proof or staged action

Do not reward polished guessing. Keep missing evidence visible.

## Source-Of-Truth Discipline

Cross-artifact fields have one canonical source defined in `contracts/artifacts.json`.

Examples:

- operating owner -> Day-2 Operations Plan
- rollback condition -> POC Acceptance Contract
- operator adoption signal -> Day-2 Operations Plan
- AI authority level -> Governance And Risk Overlay
- production launch decision -> Production Readiness Review
- field constraint and destination -> Field Signal Log

Reference the canonical field from other artifacts. When the source artifact has not been created, mark the temporary value for later consolidation.

## Case Discipline

A shipped case must be:

- synthetic, public, or sanitized
- separated from core doctrine
- useful for teaching or regression validation
- indexed through `case-manifest.json`
- explicit about which gates are go, conditional-go, no-go, held, or unrun

One case can stress the method. It cannot redefine the cross-industry doctrine by itself.

## Validation Commands

Run before every pull request or handoff:

```bash
make check
```

Equivalent direct commands:

```bash
python tools/validate_repo.py
python -m unittest discover -s tests -v
python -m compileall -q tools tests
```

The automated checks cover:

- canonical stage sequence and unique stage IDs
- root Skill and README stage-name alignment
- artifact and Gate stage references
- artifact-contract shape
- template required-field drift
- required template sections and markers
- strict example coverage
- compatibility aliases
- source-of-truth and gate references
- case-manifest schema drift
- case gate completeness and artifact paths
- relative Markdown links
- repository path references

A manual inspection can supplement these commands. It cannot replace a failing automated check.

## Pull Request Checklist

Before finishing a change, verify:

1. the change has a clear use condition and stop condition
2. stage registry, root Skill, and README agree
3. root and child Skills agree
4. canonical templates and machine contracts agree
5. strict examples still satisfy their contract
6. new field practices route into production, eval, incident, or product-learning controls
7. public examples contain no private customer information
8. validation and unit tests pass
9. the PR states what was tested and what remains unproven
