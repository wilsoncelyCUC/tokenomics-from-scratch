from __future__ import annotations

from copy import deepcopy
from typing import Any


def calculate_model_call_cost(
    input_tokens: int,
    output_tokens: int,
    input_price_per_million: float,
    output_price_per_million: float,
) -> float:
    input_cost = (input_tokens / 1_000_000) * input_price_per_million
    output_cost = (output_tokens / 1_000_000) * output_price_per_million
    return input_cost + output_cost


def calculate_step_cost(step: dict[str, Any], pricing_catalog: dict[str, dict[str, Any]]) -> float:
    fixed_cost = float(step.get("fixed_cost_per_task", 0.0))
    if "model_id" not in step:
        return fixed_cost

    model = pricing_catalog[step["model_id"]]
    call_cost = calculate_model_call_cost(
        input_tokens=int(step.get("input_tokens", 0)),
        output_tokens=int(step.get("output_tokens", 0)),
        input_price_per_million=float(model["input_price_per_million_tokens"]),
        output_price_per_million=float(model["output_price_per_million_tokens"]),
    )
    return fixed_cost + call_cost * float(step.get("calls_per_task", 1))


def calculate_monthly_cost(cost_per_task: float, monthly_volume: int) -> float:
    return cost_per_task * monthly_volume


def calculate_workflow_cost(
    workflow: dict[str, Any],
    pricing_catalog: dict[str, dict[str, Any]],
) -> dict[str, Any]:
    step_costs = [
        {
            "name": step["name"],
            "cost": calculate_step_cost(step, pricing_catalog),
        }
        for step in workflow["steps"]
    ]
    base_cost = sum(step["cost"] for step in step_costs)
    retry_cost = base_cost * float(workflow.get("retry_rate", 0.0))
    human_fallback_cost = float(workflow.get("human_fallback_rate", 0.0)) * float(
        workflow.get("human_fallback_cost", 0.0)
    )
    failure_cost = float(workflow.get("failure_rate", 0.0)) * float(workflow.get("failure_cost", 0.0))
    cost_per_task = base_cost + retry_cost + human_fallback_cost + failure_cost
    monthly_volume = int(workflow.get("monthly_volume", 0))

    return {
        "workflow_id": workflow["workflow_id"],
        "base_cost_per_task": base_cost,
        "retry_cost_per_task": retry_cost,
        "human_fallback_cost_per_task": human_fallback_cost,
        "failure_cost_per_task": failure_cost,
        "cost_per_completed_task": cost_per_task,
        "monthly_volume": monthly_volume,
        "monthly_cost": calculate_monthly_cost(cost_per_task, monthly_volume),
        "step_costs": step_costs,
    }


BEHAVIOR_RATES = ("retry_rate", "human_fallback_rate", "failure_rate")


def assign_model(workflow: dict[str, Any], model_id: str) -> dict[str, Any]:
    """Run every model step on one model, using how that model behaves on this task.

    A cheaper model can write more tokens, retry more and fail more. The optional
    workflow["model_behavior"][model_id] entry says so; without it, the model is
    assumed to behave exactly like the workflow's baseline.
    """
    behavior = workflow.get("model_behavior", {}).get(model_id, {})
    candidate = deepcopy(workflow)
    for step in candidate["steps"]:
        if "model_id" in step:
            step["model_id"] = model_id
            for side in ("input", "output"):
                multiplier = float(behavior.get(f"{side}_token_multiplier", 1.0))
                step[f"{side}_tokens"] = round(step.get(f"{side}_tokens", 0) * multiplier)
    for rate in BEHAVIOR_RATES:
        if rate in behavior:
            candidate[rate] = behavior[rate]
    return candidate


def compare_models_for_workflow(
    workflow: dict[str, Any],
    pricing_catalog: dict[str, dict[str, Any]],
    model_ids: list[str],
) -> list[dict[str, Any]]:
    comparisons: list[dict[str, Any]] = []

    for model_id in model_ids:
        result = calculate_workflow_cost(assign_model(workflow, model_id), pricing_catalog)
        comparisons.append(
            {
                "model_id": model_id,
                "cost_per_completed_task": result["cost_per_completed_task"],
                "monthly_cost": result["monthly_cost"],
                "behavior_assumed": model_id not in workflow.get("model_behavior", {}),
            }
        )

    return sorted(comparisons, key=lambda item: item["cost_per_completed_task"])
