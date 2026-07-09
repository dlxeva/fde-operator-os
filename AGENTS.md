# AGENTS.md

Repository instructions for Codex, Hermes, OpenClaw, Claude Code, and other coding agents working on this repo.

## Mission

Maintain `fde-operator-os` as a compact Applied AI Operator OS for qualifying AI opportunities, reconstructing operational reality, designing bounded pilots, and distilling reusable delivery assets.

This repository is a skill / playbook package, not an application implementation repo.

## Read First

Before editing behavior, structure, or templates, read:

1. `README.md`
2. `SKILL.md`
3. `references/doctrine.md`
4. the relevant child skill under `skills/`
5. the relevant template under `assets/templates/`

For changes involving failure modes, also read:

- `references/failure-patterns.md`
- `references/operator-heuristics.md`

For runtime or packaging changes, also read:

- `references/runtime-portability.md`
- `aliases/fde/SKILL.md`

## Hard Boundaries

Do not turn this repository into:

- a web app
- a backend service
- a frontend implementation
- an OCR/PDF parser
- a meeting recorder
- an ASR/TTS app
- a production browser automation project
- a generic AI prompt collection
- a broad consulting template dump

Do not add domain-specific private customer material to the core skill. Domain cases should live as examples, benchmark packs, or private local working context.

## Repository Shape

Keep the current structure stable:

- `SKILL.md` — root doctrine and router
- `skills/` — lighter leaf skills for common request shapes
- `references/` — reusable doctrine, heuristics, failure patterns, and portability guidance
- `assets/templates/` — operator artifacts and support artifacts
- `examples/` — synthetic or reusable case demonstrations
- `aliases/` — runtime aliases and wrappers
- `agents/` — host-facing metadata

Add a new top-level directory only when the existing structure clearly cannot hold the work.

## Editing Discipline

Prefer small, reviewable changes.

When editing the root skill, check whether child skills need the same change.

When editing child skills, check whether the root skill still routes to them correctly.

When adding or renaming a template, update all relevant references in:

- `README.md`
- `SKILL.md`
- child skill `SKILL.md` files
- `references/runtime-portability.md` when runtime loading is affected

When keeping a legacy filename for compatibility, state the alias explicitly inside the file.

## Output Discipline

Artifacts should be operator-grade:

- judgment first
- evidence versus inference separated
- explicit unknowns and risks
- staged next action
- concrete owner, trigger, object, output, acceptance, fallback, and evidence where relevant

Do not reward polished guessing. Mark gaps as gaps.

## Case Discipline

Keep core doctrine cross-industry.

A case may enter the repository only if it is:

- synthetic
- public
- sanitized
- separated from core doctrine
- useful for demonstrating or validating the skill

Do not let one case contaminate the generic method.

## Validation Checklist

Before finishing a repo change, check:

1. README links still resolve.
2. Template names match artifact names or clearly state aliases.
3. Root skill and child skills do not contradict each other.
4. New behavior has a clear use condition and stop condition.
5. The change reduces ambiguity for the next operator or coding agent.

If validation cannot be run through a local tool, state what was manually inspected.
