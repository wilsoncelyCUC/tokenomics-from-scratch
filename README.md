# Tokenomics from Scratch

> The unit of AI strategy is not the model. It is the task.

Tokenomics from Scratch is a practical open-source curriculum for understanding the economics of AI products.

Most AI teams ask: "Which model is smarter?"

This repo asks: "Which model completes the task with the best economics?"

You will learn how to estimate token costs, compare model pricing, evaluate cost-quality tradeoffs, budget agentic workflows, track spend in production, and design AI products that protect margin as usage scales.

Every lesson ships a practical artifact: a calculator, template, prompt, scorecard, dashboard, or small tool.

The goal is simple: make AI economics visible before it becomes expensive.

## Tokenomics Manifesto

In the era of long context windows, model routing, and autonomous agents, intelligence is easier to access than ever. Margin is not.

Raw model pricing is only one line item. A production AI task can also include retrieval, embeddings, tool calls, retries, evals, tracing, storage, human fallback, and failure handling. A cheap model can become expensive when it fails often. A frontier model can be economical when it resolves the task cleanly.

Do not optimize for the cheapest model.

Optimize for the cheapest reliable completed task.

## Who This Is For

- AI Product Managers designing AI features with measurable margins
- Forward Deployed Engineers scoping workflows before implementation
- AI startup founders pricing outcome-based products
- Product engineers building LLM workflows
- Solution architects comparing providers and routing strategies
- Technical business operators who need AI economics without becoming ML researchers

This is not a generic chatbot tutorial, an awesome-list, or a SaaS starter kit. It is a Markdown-first educational repository with small runnable examples where code clarifies the economics.

## Why Tokenomics Matters

Traditional software has low marginal cost after the feature ships. AI features often keep paying a variable inference cost every time they are used.

| Question | Weak answer | Better answer |
| --- | --- | --- |
| Which model should we use? | The smartest one. | The least expensive model that reliably completes this task. |
| What does this feature cost? | API price per token. | Cost per completed task, including retries and fallback. |
| When do agents get expensive? | When the model is pricey. | When loops, tools, context, and failures multiply. |
| How do we protect margin? | Negotiate provider pricing. | Route, budget, trace, evaluate, and price the feature deliberately. |

Core formula:

```text
Cost per completed task =
model inference
+ embeddings / retrieval
+ tool calls
+ storage / logging
+ evaluations
+ retries
+ human fallback
+ failure cost
```

## What You Will Build

- A task-level cost calculator
- A completed-task economics model
- A model comparison workflow
- A simple routing simulator
- PM and FDE templates for budget reviews
- Scorecards for launch readiness and model selection
- A vocabulary for discussing AI feature margin

## Repo Structure

```text
tokenomics-from-scratch/
├── README.md
├── ROADMAP.md
├── LESSON_TEMPLATE.md
├── CONTRIBUTING.md
├── data/
│   ├── sample_pricing.json
│   └── sample_workflows.json
├── examples/
│   ├── support-agent-cost.json
│   ├── document-summarization-cost.json
│   └── internal-copilot-cost.json
├── lessons/
│   ├── 00-foundations/
│   ├── 01-token-math/
│   ├── 02-cost-per-completed-task/
│   ├── 03-model-pricing-intelligence/
│   ├── 04-agent-economics/
│   ├── 05-routing-and-budgeting/
│   ├── 06-observability/
│   └── 07-ai-feature-margin/
├── outputs/
├── projects/
│   ├── cost-per-task-calculator/
│   └── model-routing-simulator/
├── resources/
├── src/tokenomics_from_scratch/
├── templates/
└── tests/
```

## Curriculum Map

| Phase | Lesson | Outcome |
| --- | --- | --- |
| 00 | [Foundations](lessons/00-foundations/README.md) | Learn the vocabulary of tokens, context, and AI cost drivers. |
| 01 | [Token Math](lessons/01-token-math/README.md) | Build the basic cost calculator. |
| 02 | [Cost Per Completed Task](lessons/02-cost-per-completed-task/README.md) | Move from API-call thinking to workflow economics. |
| 03 | [Model Pricing Intelligence](lessons/03-model-pricing-intelligence/README.md) | Compare models with changing prices and explicit assumptions. |
| 04 | [Agent Economics](lessons/04-agent-economics/README.md) | Budget retries, tool calls, long context, and human fallback. |
| 05 | [Routing and Budgeting](lessons/05-routing-and-budgeting/README.md) | Simulate model routing under a task budget. |
| 06 | [Observability](lessons/06-observability/README.md) | Turn traces and evals into cost controls. |
| 07 | [AI Feature Margin](lessons/07-ai-feature-margin/README.md) | Model feature-level P&L and produce an AI feature economics brief. |

## Quickstart

Requirements:

- Python 3.11+
- No API keys
- No external provider calls

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[dev]"
python -m pytest
```

Run the examples:

```bash
python -m tokenomics_from_scratch.cli estimate --workflow examples/support-agent-cost.json
python -m tokenomics_from_scratch.cli compare --workflow examples/document-summarization-cost.json --models cheap-model,mid-model,frontier-model
python -m tokenomics_from_scratch.cli route --workflow examples/internal-copilot-cost.json --budget-per-task 0.05
```

After installation, the console command is also available:

```bash
tokenomics estimate --workflow examples/support-agent-cost.json
```

## Example Output

```text
Workflow: support-agent-resolution
Cost per completed task: $0.1334
Monthly volume: 10000
Estimated monthly cost: $1334.2400
```

The numbers above use illustrative sample pricing from [data/sample_pricing.json](data/sample_pricing.json). Replace the data with provider-verified prices before using the calculator for production decisions.

## Resource Philosophy

The [resources](resources/README.md) folder is intentionally curated. A link belongs here only if it helps estimate real AI system cost, explain agentic workflow economics, provide reusable pricing data, evaluate cost-quality tradeoffs, or improve production cost governance.

This repo avoids stale price claims. When a resource or price needs validation, it is marked explicitly.

## Templates And Outputs

- PM/FDE templates live in [templates](templates/README.md).
- Reusable prompts, scorecards, and checklists live in [outputs](outputs/README.md).
- Small runnable demos live in [projects](projects/README.md).

## Contribution Rules

See [CONTRIBUTING.md](CONTRIBUTING.md). In short:

- Keep the repo Markdown-first.
- Prefer small transparent examples over frameworks.
- Mark sample pricing as illustrative unless provider-verified.
- Do not add live API keys, secrets, or vendor credentials.
- Add resources only when they pass the curation rules.

## Disclaimer

This repository is educational. Sample pricing data is illustrative unless explicitly marked as provider-verified. AI provider prices, caching rules, model names, rate limits, and billing policies change frequently. Always validate assumptions before making pricing, margin, or production routing decisions.
