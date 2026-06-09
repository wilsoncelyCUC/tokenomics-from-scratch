# Cost Review Prompt

Use this prompt to review an AI workflow before launch.

```text
You are reviewing an AI workflow for product economics.

Task:
[describe the completed user task]

Workflow:
[list model calls, retrieval, tools, retries, fallbacks, and logging]

Pricing assumptions:
[list model prices, source, and date checked]

Volume assumptions:
[monthly completed tasks]

Review the workflow for:
1. Cost per completed task
2. Steps that dominate cost
3. Retry and fallback sensitivity
4. Routing opportunities
5. Observability gaps
6. Margin risks

Return a concise recommendation with assumptions, risks, and next actions.
```
