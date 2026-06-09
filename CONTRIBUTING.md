# Contributing

Tokenomics from Scratch is a portfolio-grade educational repo about AI product economics.

## What Belongs Here

- Clear lessons about cost per completed task, model routing, agent economics, AI feature margin, and production cost governance
- Small runnable examples that clarify the lesson
- PM and FDE templates that produce reusable artifacts
- High-signal resources with explicit notes about why they matter

## What Does Not Belong Here

- Generic AI news links
- Unverified model price claims presented as current facts
- Vendor secrets, API keys, or live credentials
- Full SaaS scaffolding
- Large framework demos that distract from the economics

## Pricing Rules

Use illustrative prices unless a price is verified against a provider source. Mark illustrative data clearly.

Provider pricing changes frequently. Contributions that add pricing data should include:

- Source link
- Date checked
- Scope of the price claim
- Any caveats for context length, caching, batch pricing, regions, or model version

## Lesson Rules

Use [LESSON_TEMPLATE.md](LESSON_TEMPLATE.md). Every lesson should produce a reusable artifact: a calculator, worksheet, scorecard, checklist, prompt, or implementation pattern.

## Code Rules

- Keep examples small.
- Prefer the Python standard library.
- Do not make network calls in tests.
- Do not require API keys.
- Add or update tests when changing calculator behavior.
