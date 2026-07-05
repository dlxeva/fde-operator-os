---
name: mission-qualifier
description: Lightweight Applied AI qualification skill for deciding whether an opportunity is worth pursuing and what proof path would make it credible.
---

# Mission Qualifier

Use this skill when the main question is:

- is this worth doing at all
- who is the real operator
- what outcome would count as proof
- what would make this a no-go or not-now

## Scope

Stay narrow.

This skill is for upstream qualification, not full workflow design.

Primary output:

- `Mission Brief`

## What To Answer

- What problem class is this really in
- Is there recurring pain with consequence
- Who is the operator or accountable owner
- What success proof is observable inside a realistic time window
- What constraints or blockers could kill the opportunity

## Do Not Expand Into

- operational reality reconstruction
- full ontology or state modeling
- architecture promises
- expansion roadmap
- pricing or sales strategy

## Completion Standard

A reviewer should be able to say:

> I understand why this opportunity matters, who owns it, what proof looks like, and why we should proceed or stop.

## Output Style

- concise judgment first
- evidence versus inference separated
- explicit go / no-go posture
- explicit unknowns requiring validation

## Template Reference

This skill uses the core `assets/templates/mission-brief.md` template.

- **Hermes**: `skill_view(name='fde-operator-os', file_path='assets/templates/mission-brief.md')`
- **Codex**: `${CLAUDE_SKILL_DIR}/assets/templates/mission-brief.md`

