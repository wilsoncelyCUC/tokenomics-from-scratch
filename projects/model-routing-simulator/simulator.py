from __future__ import annotations

import json
from copy import deepcopy
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
BUDGET_PER_TASK = 0.05


def load_json(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as file:
        return json.load(file)


def call_cost(step: dict, model: dict) -> float:
    input_cost = step.get("input_tokens", 0) / 1_000_000 * model["input_price_per_million_tokens"]
    output_cost = step.get("output_tokens", 0) / 1_000_000 * model["output_price_per_million_tokens"]
    return (input_cost + output_cost) * step.get("calls_per_task", 1)


def workflow_cost(workflow: dict, models: dict) -> float:
    base = 0.0
    for step in workflow["steps"]:
        base += step.get("fixed_cost_per_task", 0.0)
        if "model_id" in step:
            base += call_cost(step, models[step["model_id"]])
    base += base * workflow.get("retry_rate", 0)
    base += workflow.get("human_fallback_rate", 0) * workflow.get("human_fallback_cost", 0)
    base += workflow.get("failure_rate", 0) * workflow.get("failure_cost", 0)
    return base


def main() -> None:
    pricing = load_json(ROOT / "data/sample_pricing.json")
    workflow = load_json(ROOT / "examples/internal-copilot-cost.json")
    models = {model["id"]: model for model in pricing["models"]}
    cheapest_first = sorted(
        models,
        key=lambda model_id: (
            models[model_id]["input_price_per_million_tokens"]
            + models[model_id]["output_price_per_million_tokens"]
        ),
    )

    print(f"Workflow: {workflow['workflow_id']}")
    print(f"Budget per completed task: ${BUDGET_PER_TASK:.4f}")

    for model_id in cheapest_first:
        candidate = deepcopy(workflow)
        for step in candidate["steps"]:
            if "model_id" in step:
                step["model_id"] = model_id
        cost = workflow_cost(candidate, models)
        status = "within budget" if cost <= BUDGET_PER_TASK else "over budget"
        print(f"- Try {model_id}: ${cost:.4f} ({status})")
        if cost <= BUDGET_PER_TASK:
            print(f"Selected model: {model_id}")
            return

    print("Selected model: none fits budget")


if __name__ == "__main__":
    main()
