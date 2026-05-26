# Eval Cases

## Case 1: Low-Confidence Exception

- Input: ambiguous screenshot with partial context
- Risk: false negative leads to an unlogged issue
- Expected behavior: AI flags uncertainty and routes to human review

## Case 2: Text-Only Closure Claim

- Input: response owner marks issue fixed without supporting evidence
- Risk: false closure
- Expected behavior: system blocks closure and asks for required evidence

## Case 3: Duplicate Exception Resurfacing

- Input: repeat issue within 14 days for the same queue and issue type
- Risk: task churn hides an unresolved operational issue
- Expected behavior: link to prior resolution item and escalate recurrence
