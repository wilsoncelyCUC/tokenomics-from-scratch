from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


def load_json(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as file:
        return json.load(file)


def model_call_cost(step: dict, model: dict) -> float:
    input_cost = step.get("input_tokens", 0) / 1_000_000 * model["input_price_per_million_tokens"]
    output_cost = step.get("output_tokens", 0) / 1_000_000 * model["output_price_per_million_tokens"]
    return (input_cost + output_cost) * step.get("calls_per_task", 1)


def main() -> None:
    pricing = load_json(ROOT / "data/sample_pricing.json")
    workflow = load_json(ROOT / "examples/support-agent-cost.json")
    models = {model["id"]: model for model in pricing["models"]}

    base_cost = 0.0
    for step in workflow["steps"]:
        if "fixed_cost_per_task" in step:
            base_cost += step["fixed_cost_per_task"]
        if "model_id" in step:
            base_cost += model_call_cost(step, models[step["model_id"]])

    retry_cost = base_cost * workflow.get("retry_rate", 0)
    fallback_cost = workflow.get("human_fallback_rate", 0) * workflow.get("human_fallback_cost", 0)
    failure_cost = workflow.get("failure_rate", 0) * workflow.get("failure_cost", 0)
    cost_per_task = base_cost + retry_cost + fallback_cost + failure_cost
    monthly_cost = cost_per_task * workflow["monthly_volume"]

    print(f"Workflow: {workflow['workflow_id']}")
    print(f"Cost per completed task: ${cost_per_task:.4f}")
    print(f"Monthly cost: ${monthly_cost:.2f}")
    print("Pricing: illustrative placeholder data, not provider-verified.")


if __name__ == "__main__":
    main()
