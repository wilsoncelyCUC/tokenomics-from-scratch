from __future__ import annotations

from typing import Any

from .calculator import assign_model, calculate_workflow_cost


def simulate_routing(
    workflow: dict[str, Any],
    pricing_catalog: dict[str, dict[str, Any]],
    budget_per_task: float,
) -> dict[str, Any]:
    """Pick the model with the cheapest completed task that fits the budget.

    Every model is tried, because the cheapest price per token is not always the
    cheapest completed task once retries and failures are counted.
    """

    model_ids = sorted(
        pricing_catalog,
        key=lambda model_id: (
            pricing_catalog[model_id]["input_price_per_million_tokens"]
            + pricing_catalog[model_id]["output_price_per_million_tokens"]
        ),
    )
    attempts: list[dict[str, Any]] = []

    for default_model in model_ids:
        result = calculate_workflow_cost(assign_model(workflow, default_model), pricing_catalog)
        attempts.append(
            {
                "default_model": default_model,
                "cost_per_completed_task": result["cost_per_completed_task"],
                "within_budget": result["cost_per_completed_task"] <= budget_per_task,
            }
        )

    best = min(attempts, key=lambda attempt: attempt["cost_per_completed_task"])
    return {
        "budget_per_task": budget_per_task,
        "selected_model": best["default_model"] if best["within_budget"] else None,
        "selected_cost_per_completed_task": best["cost_per_completed_task"],
        "attempts": attempts,
    }
