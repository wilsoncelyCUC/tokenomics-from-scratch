# The evidence, line by line

The research behind the [Task Receipt](../FRAMEWORK.md). Each entry says which line it moves, how strong the evidence is, and when it was checked.

**Evidence grades**

| Grade | Means | Example |
| --- | --- | --- |
| **A** | Independent and tested: peer-reviewed, a randomised trial, or a court record | RouteLLM at ICLR 2025 |
| **B** | Independent, one source: a preprint or an independent benchmark | Epoch AI price data |
| **C** | Self-reported: a company measuring its own product, or an author who sells the fix | Anthropic's agent token figures |
| **D** | Argument: essay, trend estimate, playbook or secondary reporting | a16z on LLMflation |
| **$** | Published price: true on the date checked, goes stale fast | Gemini pricing page |

**Status**: ✓ primary source read, with the date · ⏳ only secondary reporting read, not yet verified · ⚠ superseded by newer evidence

## P: price per token

| Claim | Grade | Source | Status |
| --- | :---: | --- | :---: |
| The same quality gets 9× to 900× cheaper per year, depending on the task | B | [Epoch AI](https://epoch.ai/data-insights/llm-inference-price-trends), Mar 2025 | ✓ 30 Oct |
| For the same capability, price falls about 10× a year | D | [a16z, LLMflation](https://a16z.com/llmflation-llm-inference-cost/), Nov 2024 | ✓ 30 Oct |
| GPT-3.5-level quality got 280× cheaper from Nov 2022 to Oct 2024 | B | Stanford AI Index 2025 | ⏳ |
| Some prices jump for the whole request above a size threshold (a cliff, not a slope) | $ | Google Gemini pricing, via [the article](https://www.ai-revolution-hub.com/p/the-tokenomics-of-ai-product-strategy), May 2026 | ✓ 2 Nov |
| The same text can be split into tokens in different ways, so the same output can cost different amounts, especially outside English | B | [Chatzi et al.](https://arxiv.org/abs/2506.06446), 2025 | ✓ 2 Nov |

## T: tokens per attempt

| Claim | Grade | Source | Status |
| --- | :---: | --- | :---: |
| Each token is cheaper, but each task uses far more tokens, so flat subscriptions get squeezed | D | [Ethan Ding](https://ethanding.substack.com/p/ai-subscriptions-get-short-squeezed), Aug 2025 | ✓ 30 Oct |
| Models doing the same work used 3.3× different output tokens (22M to 73M) | B | Artificial Analysis, via [the article](https://www.ai-revolution-hub.com/p/the-tokenomics-of-ai-product-strategy), Jun 2026 | ✓ 2 Nov |
| Reasoning models spend heavily on easy problems for little benefit | B | [Chen et al., "Do NOT think that much for 2+3=?"](https://arxiv.org/abs/2412.21187), Dec 2024 | ✓ 2 Nov |
| Prompts can be compressed up to 20× with little quality loss | A | [LLMLingua](https://arxiv.org/abs/2310.05736), EMNLP 2023 | ✓ 30 Oct |
| Reliability drops as input grows, across 18 models, even on simple tasks. The authors sell retrieval, the alternative to long context | C | [Chroma, Context Rot](https://www.trychroma.com/research/context-rot), Jul 2025 | ✓ 2 Nov |

## A: attempts per task

| Claim | Grade | Source | Status |
| --- | :---: | --- | :---: |
| Start with one call, then a fixed workflow, and use an agent only when the task needs it | D | [Anthropic, Building effective agents](https://www.anthropic.com/engineering/building-effective-agents), Dec 2024 | ✓ 30 Oct |
| Agents used about 4× the tokens of a chat; multi-agent systems about 15× | C | [Anthropic, multi-agent research system](https://www.anthropic.com/engineering/multi-agent-research-system), Jun 2025 | ✓ 30 Oct |
| Simple baselines often match complex agents at a fraction of the cost | A | [AI Agents That Matter](https://arxiv.org/abs/2407.01502), TMLR 2025 | ✓ 30 Oct |

## S: success rate

| Claim | Grade | Source | Status |
| --- | :---: | --- | :---: |
| Measure the expected cost of one correct answer. Reasoning models can be the cheapest per correct answer on hard problems, despite a higher token price | B | [Cost-of-Pass](https://arxiv.org/abs/2504.13359), Apr 2025 | ✓ 2 Nov |
| Across 21,730 agent runs (about $40,000), higher reasoning effort reduced accuracy in most runs | A | [HAL, Princeton](https://arxiv.org/abs/2510.11977), ICLR 2026 | ✓ 2 Nov |
| A trained router was more than 2× cheaper with no loss of quality | A | [RouteLLM](https://arxiv.org/abs/2406.18665), ICLR 2025 | ✓ 30 Oct |
| A cheap-model-first cascade matched GPT-4 at up to 98% lower cost | B | [FrugalGPT](https://arxiv.org/abs/2305.05176), 2023 | ✓ 30 Oct |

## F: cost of one failure

| Claim | Grade | Source | Status |
| --- | :---: | --- | :---: |
| A company is liable for what its chatbot tells customers | A | [Moffatt v. Air Canada, 2024 BCCRT 149](https://decisions.civilresolutionbc.ca/crt/crtd/en/525448/1/document.do), Feb 2024 | ⏳ |
| In a support workflow, human fallback and failures can be 94% of the cost of a task | Our numbers | [examples/support-agent-cost.json](../examples/support-agent-cost.json), illustrative | ✓ 2 Nov |

## W: value per completed task

| Claim | Grade | Source | Status |
| --- | :---: | --- | :---: |
| Developers felt 20% faster with AI and were measured 19% slower | A | [METR randomised trial](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/), Jul 2025 | ⚠ METR published newer data in Feb 2026 |
| AI gross margins run 50–60% against 80–90% for SaaS; price on value, not cost-plus | D | [Bessemer, AI pricing playbook](https://www.bvp.com/atlas/the-ai-pricing-and-monetization-playbook), Feb 2026 | ✓ 2 Nov |
| Outcome pricing exists: $0.99 per resolved conversation | $ | Intercom Fin, via [Bessemer](https://www.bvp.com/atlas/the-ai-pricing-and-monetization-playbook), Feb 2026 | ⏳ |
| The fastest-growing AI startups run about 25% gross margin, steadier ones about 60% | D | Bessemer, State of AI 2025 | ⏳ |

## How a claim gets in

The process is public, so you can see why each claim is trusted.

```text
 someone opens an "Add evidence" issue
        │
        ▼
 ⏳ pending ── a maintainer reads the primary source, not a write-up
        │
        ├─ tags the line it moves (P T O A S F W)
        ├─ grades it (A B C D $)
        └─ stamps the date checked
        │
        ▼
 ✓ on the page ── re-checked when it goes stale (prices: 90 days)
        │
        ▼ newer evidence breaks it
 ⚠ superseded ── kept on the page, with what changed and why
```

Claims are never deleted when they break. A superseded row that stays on the page, with the reason, does more for trust than a clean list.

Checked on 2 November 2026.
