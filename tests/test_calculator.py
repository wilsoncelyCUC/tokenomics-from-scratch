from tokenomics_from_scratch.calculator import (
    calculate_model_call_cost,
    calculate_monthly_cost,
    calculate_step_cost,
    calculate_workflow_cost,
    compare_models_for_workflow,
)
from tokenomics_from_scratch.routing import simulate_routing


PRICING = {
    "cheap-model": {
        "input_price_per_million_tokens": 0.10,
        "output_price_per_million_tokens": 0.40,
    },
    "mid-model": {
        "input_price_per_million_tokens": 1.00,
        "output_price_per_million_tokens": 5.00,
    },
    "frontier-model": {
        "input_price_per_million_tokens": 5.00,
        "output_price_per_million_tokens": 15.00,
    },
}


WORKFLOW = {
    "workflow_id": "test-workflow",
    "monthly_volume": 1000,
    "steps": [
        {
            "name": "draft",
            "model_id": "mid-model",
            "input_tokens": 1000,
            "output_tokens": 200,
            "calls_per_task": 2,
        },
        {
            "name": "retrieve",
            "fixed_cost_per_task": 0.001,
        },
    ],
    "retry_rate": 0.10,
    "human_fallback_rate": 0.01,
    "human_fallback_cost": 2.00,
    "failure_rate": 0.02,
    "failure_cost": 1.50,
}


def test_model_call_cost_calculation():
    assert calculate_model_call_cost(1000, 200, 1.0, 5.0) == 0.002


def test_step_cost_calculation_for_model_step():
    step = WORKFLOW["steps"][0]
    assert calculate_step_cost(step, PRICING) == 0.004


def test_step_cost_calculation_for_fixed_step():
    step = WORKFLOW["steps"][1]
    assert calculate_step_cost(step, PRICING) == 0.001


def test_full_workflow_cost_calculation():
    result = calculate_workflow_cost(WORKFLOW, PRICING)
    assert result["base_cost_per_task"] == 0.005
    assert result["retry_cost_per_task"] == 0.0005
    assert result["human_fallback_cost_per_task"] == 0.02
    assert result["failure_cost_per_task"] == 0.03
    assert result["cost_per_completed_task"] == 0.0555


def test_monthly_cost_calculation():
    assert calculate_monthly_cost(0.0555, 1000) == 55.5


def test_model_comparison_sorts_by_cost():
    result = compare_models_for_workflow(
        WORKFLOW,
        PRICING,
        ["frontier-model", "mid-model", "cheap-model"],
    )
    assert [item["model_id"] for item in result] == [
        "cheap-model",
        "mid-model",
        "frontier-model",
    ]


def test_routing_simulation_selects_model_within_budget():
    result = simulate_routing(WORKFLOW, PRICING, budget_per_task=0.056)
    assert result["selected_model"] == "cheap-model"
    assert result["selected_cost_per_completed_task"] <= 0.056
