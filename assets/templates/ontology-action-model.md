# State, Action & Evidence Model

Alias: `Ontology & Action Model`

## Use

Use when turning the business world into a run-capable system definition.

## Required Fields

- Objects
- Relationships
- States
- Actions
- Rules
- Events / triggers
- Permissions / authorities
- Evidence for state change

## Optional Fields

- Confidence fields
- Rollback rules
- Derived entities

## Typical Anti-Pattern

The artifact lists entities and categories but does not define actions, ownership, or proof of transition.

## Completion Standard

A technical team can infer what the system reads, what it can change, and what proof is needed to advance the loop.

## Template

```md
# State, Action & Evidence Model

## Business Objects

- ...

## Relationships

- ...

## States

- ...

## Actions

- Action:
  - Owner:
  - Type: advisory / gated / write
  - Output:

## Rules

- ...

## Events / Triggers

- ...

## Permissions

- ...

## Evidence For State Change

- ...
```
