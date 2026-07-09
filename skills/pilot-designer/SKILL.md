---
name: pilot-designer
description: Lightweight Applied AI skill for compressing a bounded loop into a credible pilot with acceptance and eval support.
---

# Pilot Designer

Use this skill when the main question is:

- what is the smallest credible pilot
- where should AI intervene
- what remains human-owned
- how will the pilot be judged

## Scope

Stay focused on bounded pilot design.

Primary outputs:

- `AI Intervention Design`
- `Minimum Viable Loop`
- `POC Acceptance Contract`
- `Eval Pack`

## What To Define

- target bottleneck
- narrow AI surface
- human confirmation boundary
- fallback path
- baseline manual path
- acceptance criteria
- eval cases and thresholds
- rollback condition

## Do Not Expand Into

- broad account strategy
- full platform architecture unless the loop is already proven
- organization-wide rollout
- detailed day-2 operations beyond what is needed for a credible pilot boundary

## Completion Standard

A reviewer should be able to say:

> I understand the bounded pilot, how AI participates, what humans still own, how we will test it, and what would make it acceptable or not.

## Output Style

- one narrow loop, not a feature bag
- explicit baseline and measurement window
- explicit failure and rollback conditions
- eval support included by default for credible pilots

## Template Reference

This skill uses four core templates:

- `assets/templates/ai-intervention-design.md`
- `assets/templates/minimum-viable-loop.md`
- `assets/templates/poc-acceptance-contract.md`
- `assets/templates/eval-pack.md`

**Hermes**: `skill_view(name='fde-operator-os', file_path='assets/templates/<template-name>')`
**Codex / others**: read `assets/templates/<template-name>` relative to the skill root.

