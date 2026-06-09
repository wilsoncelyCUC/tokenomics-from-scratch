from __future__ import annotations

from copy import deepcopy
from typing import Any

from .calculator import calculate_workflow_cost


def simulate_routing(
    workflow: dict[str, Any],
    pricing_catalog: dict[str, dict[str, Any]],
    budget_per_task: float,
) -> dict[str, Any]:
    """Pick the cheapest model assignment that satisfies the task budget."""

    model_ids = sorted(
        pricing_catalog,
        key=lambda model_id: (
            pricing_catalog[model_id]["input_price_per_million_tokens"]
            + pricing_catalog[model_id]["output_price_per_million_tokens"]
        ),
    )
    attempts: list[dict[str, Any]] = []

    for default_model in model_ids:
        candidate = deepcopy(workflow)
        for step in candidate["steps"]:
            if "model_id" in step:
                step["model_id"] = default_model
        result = calculate_workflow_cost(candidate, pricing_catalog)
        attempts.append(
            {
                "default_model": default_model,
                "cost_per_completed_task": result["cost_per_completed_task"],
                "within_budget": result["cost_per_completed_task"] <= budget_per_task,
            }
        )
        if result["cost_per_completed_task"] <= budget_per_task:
            return {
                "budget_per_task": budget_per_task,
                "selected_model": default_model,
                "selected_cost_per_completed_task": result["cost_per_completed_task"],
                "attempts": attempts,
            }

    cheapest = attempts[-1]
    return {
        "budget_per_task": budget_per_task,
        "selected_model": None,
        "selected_cost_per_completed_task": cheapest["cost_per_completed_task"],
        "attempts": attempts,
    }
