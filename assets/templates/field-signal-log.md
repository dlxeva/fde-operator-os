# Field Signal Log

## Use

Use throughout discovery, pilot, launch, and day-2 operations to turn field observations into high-signal delivery corrections, reusable assets, and product-roadmap inputs.

## Required Fields

- Signal ID and date
- Source and workflow context
- Operator or stakeholder
- Observation and source evidence
- Impact, severity, and frequency
- Constraint class
- Current workaround
- Reusable pattern hypothesis
- Product, skill, or delivery implication
- Destination and promotion status
- Owner and next proof

## Optional Fields

- Related incident or eval case
- Affected object, state, or action
- Confidence level
- Cross-customer recurrence count
- Decision date

## Typical Anti-Pattern

Field feedback remains inside chat logs or recap decks, mixes product gaps with integration and change-management constraints, and reaches the roadmap without evidence or recurrence criteria.

## Completion Standard

Another operator can understand the signal, inspect its evidence, classify the constraint, decide where it belongs, and identify what proof is needed before promotion.

## Constraint Classes

- `product-capability`
- `model-or-eval`
- `data-readiness`
- `integration`
- `policy-or-compliance`
- `change-management`
- `delivery-execution`
- `operating-model`

## Promotion Status

- `observe` — one signal, evidence retained
- `validate` — recurrence or impact needs further proof
- `promote` — sufficient evidence for a reusable asset or roadmap item
- `reject` — local anomaly, invalid signal, or poor evidence

## Template

```md
# Field Signal Log

- **Signal ID and date**:
- **Source and workflow context**:
- **Operator or stakeholder**:
- **Observation and source evidence**:
- **Impact, severity, and frequency**:
- **Constraint class**:
- **Current workaround**:
- **Reusable pattern hypothesis**:
- **Product, skill, or delivery implication**:
- **Destination and promotion status**:
- **Owner and next proof**:

## Related Evidence

- Incident / eval case:
- Affected object, state, or action:
- Trace / artifact pointer:
- Confidence:
- Cross-customer recurrence:
```
