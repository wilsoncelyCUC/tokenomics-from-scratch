# Open-Source Tools

Software you can run yourself to see, test and control what AI costs. One tool per job.

**[LiteLLM](https://github.com/BerriAI/litellm)** · *Job: see and cap what each team or app spends.*
One front door for calls to 100+ models. Set a budget per team or API key, log every call's cost, fall back to another model when one fails.
Why trust it: about 62k stars, updated daily, the default choice for this job.

**[Langfuse](https://github.com/langfuse/langfuse)** · *Job: know what each feature, user or task costs.*
Records every step an AI feature takes, with its tokens and cost, so you can answer "what does one completed task cost us?" with data.
Why trust it: about 37k stars, self-hostable, widely used for tracing and evals.

**[Promptfoo](https://github.com/promptfoo/promptfoo)** · *Job: prove the cheaper model is good enough before you switch.*
Runs the same test cases against several models side by side and shows quality, speed and cost together.
Why trust it: about 27k stars, MIT licence.

**[RouteLLM](https://github.com/lm-sys/RouteLLM)** · *Job: send easy requests to a cheap model automatically.*
A router that decides, per request, whether the cheap or the strong model should answer. The team reports up to 85% lower cost while keeping 95% of GPT-4 quality on MT Bench.
Why trust it: from LMSYS (the Chatbot Arena team), peer-reviewed at ICLR 2025. Not updated since 2024: learn the idea here, use a maintained router in production.

**[LLMLingua](https://github.com/microsoft/LLMLingua)** · *Job: shrink long prompts you pay for on every call.*
Compresses long inputs (documents, retrieved context) before they reach the model, so you pay for fewer tokens.
Why trust it: Microsoft Research, about 7k stars, papers at EMNLP 2023 and ACL 2024. Always re-test quality after compressing.

## Same job, other good options

[Helicone](https://github.com/Helicone/helicone) and [Arize Phoenix](https://github.com/Arize-ai/phoenix) do what Langfuse does. [Portkey Gateway](https://github.com/Portkey-AI/gateway) does what LiteLLM does. Pick one per job, not all of them.
