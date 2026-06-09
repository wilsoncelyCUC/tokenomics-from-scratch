# 07: AI Feature Margin And Capstone

## Motto

AI features need their own unit economics.

## Problem

A feature can be loved by users and still damage gross margin if its variable inference cost is not reflected in packaging, usage limits, or pricing. The capstone is to turn that analysis into a reusable AI feature economics brief.

## Concept

Feature margin connects task economics to revenue:

```text
feature_margin = feature_revenue - ai_variable_cost - support_cost - infrastructure_cost
```

Important questions:

- Is the feature bundled or metered?
- Does usage correlate with willingness to pay?
- Do high-usage customers create negative margin?
- Are fallback and failure costs priced in?

## Build It

Use [templates/ai-feature-margin-brief.md](../../templates/ai-feature-margin-brief.md) to create a feature-level P&L. Then combine the cost sheet, routing recommendation, observability plan, and launch checklist into one economics brief.

## Use It

Use margin analysis before launch, before expanding usage limits, and whenever model prices or workflow design changes.

## Ship It

A feature economics brief with pricing, volume, cost, routing, observability, and risk assumptions.

## Links

- Previous: [06 Observability](../06-observability/README.md)
- Templates: [Templates](../../templates/README.md)
