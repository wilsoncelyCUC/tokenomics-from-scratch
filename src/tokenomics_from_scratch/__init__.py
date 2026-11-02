"""Small educational helpers for AI task economics."""

from .calculator import (
    assign_model,
    calculate_model_call_cost,
    calculate_monthly_cost,
    calculate_step_cost,
    calculate_workflow_cost,
    compare_models_for_workflow,
)
from .routing import simulate_routing

__all__ = [
    "assign_model",
    "calculate_model_call_cost",
    "calculate_monthly_cost",
    "calculate_step_cost",
    "calculate_workflow_cost",
    "compare_models_for_workflow",
    "simulate_routing",
]
