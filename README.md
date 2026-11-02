# Tokenomics from Scratch

> The unit of AI strategy is not the model. It is the task.

For finance leads, product managers and program managers who have to sign off on what an AI feature costs, and what it earns.

## The one idea: the Task Receipt

Every AI cost question comes down to the receipt of one completed task:

```text
C  Cost per completed task  = (P × T + O) × A  +  (1 − S) × F

P price per token · T tokens per attempt · O other cost per attempt
A attempts per task · S success rate · F cost of one failure

Margin per task = W − C, where W is what the done task is worth
```

A cheaper model lowers P, but it can raise T and A and lower S. In the repo's support example, 94% of the cost is human fallback and failures, not tokens.

Read the [Task Receipt](FRAMEWORK.md): three rules, two worked receipts, and the research behind each line.

## The ten problems

1. What does one completed task really cost us?
2. Will our AI bill shrink or grow next year?
3. Why is the bill bigger on a model that is cheaper per token?
4. Do we need an agent, or would a simple workflow do?
5. Should we price per seat, per use or per outcome?
6. Our heaviest users are eating our margin. What do we do?
7. When should we switch models?
8. What must we log before launch?
9. How do we check a vendor's "X% cheaper" claim?
10. What error rate can we afford?

[Each problem, mapped to the lines of the receipt it turns on](FRAMEWORK.md#the-ten-problems-mapped-to-the-receipt).

## Use it

- **Learn step by step:** [00 Foundations](lessons/00-foundations/README.md), [01 Token Math](lessons/01-token-math/README.md), [02 Cost Per Completed Task](lessons/02-cost-per-completed-task/README.md), [03 Model Pricing Intelligence](lessons/03-model-pricing-intelligence/README.md). Lessons 04 to 07 are drafts.
- **Fill in for your own feature:** [templates](templates/README.md): cost sheet, model scorecard, agent budget review, margin brief, launch checklist, review prompt.
- **Read what to trust:** [resources](resources/README.md), with five start-here picks, and the [graded evidence](resources/evidence.md) behind every claim.

## Run the calculator

Python 3.11+, no API keys, no network calls. Prices in [data/sample_pricing.json](data/sample_pricing.json) are illustrative.

```bash
python -m pip install -e ".[dev]"
python -m pytest
tokenomics estimate --workflow examples/support-agent-cost.json
tokenomics compare --workflow examples/support-agent-cost.json --models cheap-model,mid-model,frontier-model
tokenomics route --workflow examples/internal-copilot-cost.json --budget-per-task 0.05
```

## Contribute

Found evidence that moves a line of the receipt? See [CONTRIBUTING.md](CONTRIBUTING.md).

This repo is educational. Check prices and assumptions against your provider before making pricing, margin or routing decisions.
