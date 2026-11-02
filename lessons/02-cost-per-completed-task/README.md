# 02: Cost Per Completed Task

## Motto

The workflow is the economic unit.

## Problem

An AI feature rarely consists of one model call. A real workflow may classify a request, retrieve context, draft an answer, check quality, retry on failure, escalate uncertain cases, and log traces for review.

If you only price the first call, you understate the actual cost.

## Concept

Cost per completed task includes:

- Model inference
- Retrieval and embeddings
- Tool execution
- Storage and logging
- Evals and quality checks
- Retries
- Human fallback
- Failure cost

The calculator in this repo makes those line items visible:

```bash
python -m tokenomics_from_scratch.cli estimate --workflow examples/support-agent-cost.json
```

## Build It

Use [examples/support-agent-cost.json](../../examples/support-agent-cost.json) as a baseline. Change one assumption at a time:

- Increase `retry_rate`
- Increase `human_fallback_rate`
- Swap `generate_answer` to `frontier-model`
- Double `monthly_volume`

Record what changed and why.

## Use It

PMs can use cost per completed task to decide whether a feature should be bundled, metered, limited, or repriced. Engineering leads can use it to decide where effort should go first: prompt shortening, routing, caching, evals, retrieval design, or fallback reduction.

## Ship It

At the end of this lesson, you should have a before-and-after workflow estimate and a recommendation for the highest-leverage cost control.

## Links

- Previous: [01 Token Math](../01-token-math/README.md)
- Next: [03 Model Pricing Intelligence](../03-model-pricing-intelligence/README.md)
- Template: [Cost Review Prompt](../../templates/cost-review-prompt.md)
