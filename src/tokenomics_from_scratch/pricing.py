from __future__ import annotations

import json
from pathlib import Path
from typing import Any


DEFAULT_PRICING_PATH = Path("data/sample_pricing.json")


def load_json(path: str | Path) -> dict[str, Any]:
    with Path(path).open("r", encoding="utf-8") as file:
        return json.load(file)


def load_pricing_catalog(path: str | Path = DEFAULT_PRICING_PATH) -> dict[str, dict[str, Any]]:
    data = load_json(path)
    return {model["id"]: model for model in data["models"]}


def load_workflow(path: str | Path) -> dict[str, Any]:
    return load_json(path)
