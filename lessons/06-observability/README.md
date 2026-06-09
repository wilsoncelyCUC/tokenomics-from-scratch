# 06: Observability

## Motto

You cannot control cost you cannot trace.

## Problem

Production AI workflows often hide cost across services, retries, tools, and fallbacks. Without traces, teams argue from averages and anecdotes.

## Concept

Cost observability connects events to a completed task:

- Request ID
- User or tenant
- Workflow ID
- Step names
- Model IDs
- Input and output tokens
- Cache hits
- Tool calls
- Retry count
- Fallback status
- Outcome quality

## Build It

Draft a trace schema and use [outputs/launch-readiness-checklist.md](../../outputs/launch-readiness-checklist.md) to decide what must be logged before launch.

## Use It

PMs should review cost dashboards by completed task, not only by total spend. Engineers should make every costly branch visible in traces.

## Ship It

A minimum trace schema for one AI workflow.

## Links

- Previous: [05 Routing And Budgeting](../05-routing-and-budgeting/README.md)
- Next: [07 AI Feature Margin](../07-ai-feature-margin/README.md)
