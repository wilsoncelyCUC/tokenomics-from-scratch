from __future__ import annotations

import argparse

from .calculator import compare_models_for_workflow, calculate_workflow_cost
from .pricing import load_pricing_catalog, load_workflow
from .routing import simulate_routing


def money(value: float) -> str:
    return f"${value:.4f}"


def estimate(args: argparse.Namespace) -> None:
    pricing = load_pricing_catalog(args.pricing)
    workflow = load_workflow(args.workflow)
    result = calculate_workflow_cost(workflow, pricing)

    print(f"Workflow: {result['workflow_id']}")
    print(f"Cost per completed task: {money(result['cost_per_completed_task'])}")
    print(f"Monthly volume: {result['monthly_volume']}")
    print(f"Estimated monthly cost: {money(result['monthly_cost'])}")
    print()
    print("Step costs:")
    for step in result["step_costs"]:
        print(f"- {step['name']}: {money(step['cost'])}")


def compare(args: argparse.Namespace) -> None:
    pricing = load_pricing_catalog(args.pricing)
    workflow = load_workflow(args.workflow)
    model_ids = [model.strip() for model in args.models.split(",") if model.strip()]
    results = compare_models_for_workflow(workflow, pricing, model_ids)

    print(f"Workflow: {workflow['workflow_id']}")
    print("Model comparison:")
    for result in results:
        print(
            f"- {result['model_id']}: "
            f"{money(result['cost_per_completed_task'])}/task, "
            f"{money(result['monthly_cost'])}/month"
        )


def route(args: argparse.Namespace) -> None:
    pricing = load_pricing_catalog(args.pricing)
    workflow = load_workflow(args.workflow)
    result = simulate_routing(workflow, pricing, args.budget_per_task)

    print(f"Workflow: {workflow['workflow_id']}")
    print(f"Budget per task: {money(result['budget_per_task'])}")
    if result["selected_model"]:
        print(
            f"Selected model: {result['selected_model']} "
            f"at {money(result['selected_cost_per_completed_task'])}/task"
        )
    else:
        print("Selected model: none fits budget")
    print()
    print("Routing attempts:")
    for attempt in result["attempts"]:
        status = "within budget" if attempt["within_budget"] else "over budget"
        print(f"- {attempt['default_model']}: {money(attempt['cost_per_completed_task'])} ({status})")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="tokenomics")
    parser.add_argument("--pricing", default="data/sample_pricing.json")
    subparsers = parser.add_subparsers(dest="command", required=True)

    estimate_parser = subparsers.add_parser("estimate", help="Estimate cost per completed task")
    estimate_parser.add_argument("--workflow", required=True)
    estimate_parser.set_defaults(func=estimate)

    compare_parser = subparsers.add_parser("compare", help="Compare model options for a workflow")
    compare_parser.add_argument("--workflow", required=True)
    compare_parser.add_argument("--models", required=True)
    compare_parser.set_defaults(func=compare)

    route_parser = subparsers.add_parser("route", help="Simulate simple budget-aware routing")
    route_parser.add_argument("--workflow", required=True)
    route_parser.add_argument("--budget-per-task", type=float, required=True)
    route_parser.set_defaults(func=route)

    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
