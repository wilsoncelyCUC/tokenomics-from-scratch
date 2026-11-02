# 05: Routing And Budgeting

> **Draft.** An outline without worked numbers yet. It folds into problem P3, the cheaper model that bills more, and P7, when to switch, when that page is written.

## Motto

Route by task economics, not model loyalty.

## Problem

Running every request on the same model wastes money. Simple tasks may not need a frontier model. Complex or high-risk tasks may justify one.

## Concept

Routing can happen through:

- Upfront rules: classify task type before choosing a model.
- Cascades: try a cheaper model first, then escalate when confidence is low.
- Budget caps: refuse or degrade gracefully when a task would exceed cost limits.
- Tier rules: route free, team, and enterprise users differently.

## Build It

Run:

```bash
python -m tokenomics_from_scratch.cli route --workflow examples/internal-copilot-cost.json --budget-per-task 0.05
```

## Use It

Use routing simulations when a workflow has multiple task classes or when margins differ by customer tier.

## Ship It

A routing recommendation and a budget-per-task threshold.

## Links

- Previous: [04 Agent Economics](../04-agent-economics/README.md)
- Next: [06 Observability](../06-observability/README.md)
