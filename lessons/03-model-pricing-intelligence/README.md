# 03: Model Pricing Intelligence

## Motto

Treat model prices as changing inputs, not permanent truths.

## Problem

Model pricing changes often. Providers add new model tiers, caching discounts, context-window rules, batch discounts, and regional billing differences. Static price claims become stale quickly.

## Concept

Pricing intelligence is the practice of comparing model options with visible assumptions:

- Source of price
- Date checked
- Input and output pricing
- Cache or batch rules
- Quality expectations
- Latency expectations
- Failure and fallback impact

## Build It

Run:

```bash
python -m tokenomics_from_scratch.cli compare --workflow examples/document-summarization-cost.json --models cheap-model,mid-model,frontier-model
```

Then complete [templates/model-selection-scorecard.md](../../templates/model-selection-scorecard.md).

## Use It

Use this lesson before committing a workflow to one model or provider. The cheapest model-call price is not always the cheapest completed-task price.

## Ship It

A model selection scorecard with pricing assumptions, quality tradeoffs, and a recommended review date.

## Links

- Previous: [02 Cost Per Completed Task](../02-cost-per-completed-task/README.md)
- Next: [04 Agent Economics](../04-agent-economics/README.md)
