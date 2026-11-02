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
python -m tokenomics_from_scratch.cli compare --workflow examples/support-agent-cost.json --models cheap-model,mid-model,frontier-model
```

The first comparison assumes every model behaves the same on the task, so the cheapest price wins. The output says so.

The second uses `model_behavior` in [examples/support-agent-cost.json](../../examples/support-agent-cost.json): how often each model retries, goes to a human or fails on this task. The cheap model now costs the most per completed task, and the frontier model the least. A model can also use more tokens than another for the same work: set `input_token_multiplier` or `output_token_multiplier`.

Replace the illustrative behavior with numbers from your own evals before you trust the ranking.

Then complete [templates/model-selection-scorecard.md](../../templates/model-selection-scorecard.md).

## Use It

Use this lesson before committing a workflow to one model or provider. The cheapest model-call price is not always the cheapest completed-task price.

## Ship It

A model selection scorecard with pricing assumptions, quality tradeoffs, and a recommended review date.

## Links

- Previous: [02 Cost Per Completed Task](../02-cost-per-completed-task/README.md)
- Next: [04 Agent Economics](../04-agent-economics/README.md)
