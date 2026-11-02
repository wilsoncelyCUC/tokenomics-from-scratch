from tokenomics_from_scratch.calculator import (
    assign_model,
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


def test_assign_model_applies_how_the_model_behaves():
    workflow = {**WORKFLOW, "model_behavior": {"cheap-model": {"output_token_multiplier": 1.5, "retry_rate": 0.3}}}
    candidate = assign_model(workflow, "cheap-model")
    assert candidate["steps"][0]["model_id"] == "cheap-model"
    assert candidate["steps"][0]["output_tokens"] == 300
    assert candidate["steps"][0]["input_tokens"] == 1000
    assert candidate["retry_rate"] == 0.3
    assert candidate["failure_rate"] == WORKFLOW["failure_rate"]


def test_cheaper_per_token_model_can_cost_more_per_completed_task():
    # The shape of the Gemini 3.5 Flash vs 3.1 Pro case: 25% cheaper per token,
    # but more output tokens and more turns, so a bigger bill.
    pricing = {
        "pro": {"input_price_per_million_tokens": 2.00, "output_price_per_million_tokens": 12.00},
        "flash": {"input_price_per_million_tokens": 1.50, "output_price_per_million_tokens": 9.00},
    }
    workflow = {
        "workflow_id": "flash-vs-pro",
        "monthly_volume": 1000,
        "steps": [{"name": "answer", "model_id": "pro", "input_tokens": 10000, "output_tokens": 2000}],
        "retry_rate": 0.1,
        "model_behavior": {"flash": {"output_token_multiplier": 1.28, "retry_rate": 0.5}},
    }
    result = compare_models_for_workflow(workflow, pricing, ["flash", "pro"])
    assert [item["model_id"] for item in result] == ["pro", "flash"]


def test_comparison_flags_models_with_assumed_behavior():
    workflow = {**WORKFLOW, "model_behavior": {"cheap-model": {"failure_rate": 0.2}}}
    result = {item["model_id"]: item for item in compare_models_for_workflow(workflow, PRICING, ["cheap-model", "mid-model"])}
    assert result["cheap-model"]["behavior_assumed"] is False
    assert result["mid-model"]["behavior_assumed"] is True


def test_routing_picks_cheapest_completed_task_not_cheapest_price():
    # The cheap model fits the budget, but it fails so often that mid-model completes tasks for less.
    workflow = {**WORKFLOW, "model_behavior": {"cheap-model": {"failure_rate": 0.2}}}
    result = simulate_routing(workflow, PRICING, budget_per_task=0.5)
    assert result["attempts"][0]["default_model"] == "cheap-model"
    assert result["attempts"][0]["within_budget"] is True
    assert result["selected_model"] == "mid-model"


def test_routing_reports_none_when_nothing_fits():
    result = simulate_routing(WORKFLOW, PRICING, budget_per_task=0.01)
    assert result["selected_model"] is None
    assert result["selected_cost_per_completed_task"] == min(a["cost_per_completed_task"] for a in result["attempts"])
