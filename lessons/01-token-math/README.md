# 01: Token Math

## Motto

Small token assumptions become large margin assumptions at scale.

## Problem

Teams frequently estimate AI cost from a single model call and forget volume. A cost that looks harmless at one request can become material at 10,000, 100,000, or 1,000,000 completed tasks per month.

## Concept

The basic model-call formula is:

```text
model_call_cost =
(input_tokens / 1,000,000 * input_price_per_million_tokens)
+ (output_tokens / 1,000,000 * output_price_per_million_tokens)
```

Monthly cost is:

```text
monthly_cost = cost_per_completed_task * monthly_completed_tasks
```

This lesson uses illustrative prices from [data/sample_pricing.json](../../data/sample_pricing.json). They are placeholders, not provider-verified prices.

## Build It

Run the first demo:

```bash
python projects/cost-per-task-calculator/calculator.py
```

Then run the package CLI:

```bash
python -m tokenomics_from_scratch.cli estimate --workflow examples/support-agent-cost.json
```

## Use It

Use token math for early sizing, not final procurement. The goal is to expose the shape of the economics:

- Which step dominates cost?
- Does output length matter more than input length?
- What happens when monthly volume doubles?
- How sensitive is the workflow to retries?

## Ship It

At the end of this lesson, you should have a working calculator and a written note describing the highest-cost step in one workflow.

## Links

- Previous: [00 Foundations](../00-foundations/README.md)
- Next: [02 Cost Per Completed Task](../02-cost-per-completed-task/README.md)
- Project: [Cost Per Task Calculator](../../projects/cost-per-task-calculator/README.md)
