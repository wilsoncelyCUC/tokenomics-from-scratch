# Model Routing Simulator

This demo tries simple budget-aware routing for the internal copilot example.

Run:

```bash
python projects/model-routing-simulator/simulator.py
```

Or use the package CLI:

```bash
python -m tokenomics_from_scratch.cli route --workflow examples/internal-copilot-cost.json --budget-per-task 0.05
```

This is intentionally simple. It teaches the idea of routing under a budget, not production-grade routing.
