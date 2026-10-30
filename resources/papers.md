# Papers

Research you can quote when someone asks "does this cost lever really work?"

**[FrugalGPT](https://arxiv.org/abs/2305.05176)** (Stanford, 2023) · *Job: cut model spend without losing quality.*
Try a cheap model first and escalate to an expensive one only when the answer is not good enough. It matched GPT-4's performance with up to 98% lower cost.
Why it matters: the founding paper behind every "cascade" and model-routing product.

**[RouteLLM](https://arxiv.org/abs/2406.18665)** (LMSYS / UC Berkeley, ICLR 2025) · *Job: decide per request which model to pay for.*
Trains a small router on human preferences to pick the cheap or the strong model. More than 2× cheaper on public benchmarks without losing response quality.
Why it matters: shows routing works in practice, with open code ([see tools](open-source-tools.md)).

**[AI Agents That Matter](https://arxiv.org/abs/2407.01502)** (Princeton, TMLR 2025) · *Job: judge an agent on cost, not only accuracy.*
Most agent leaderboards ignore cost, so teams build agents that are needlessly expensive. Simple baselines often match complex agents at a fraction of the cost.
Why it matters: gives you the question to ask any vendor: "accurate, at what cost per task?"

**[LLMLingua](https://arxiv.org/abs/2310.05736)** (Microsoft Research, EMNLP 2023) · *Job: pay for fewer input tokens.*
Removes the words a model does not need from long prompts, compressing them up to 20× with little loss in quality.
Why it matters: the reference for prompt compression; the code is in [tools](open-source-tools.md).
