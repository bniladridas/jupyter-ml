"""Regression tests for notebooks."""

import os
import json
from pathlib import Path

from jupyter_ml.runner import capture_outputs
from jupyter_ml.notebook import notebook_hash


def get_baseline_path(notebook: str) -> Path:
    """Path to baseline outputs for a notebook."""
    name = Path(notebook).stem
    return Path("tests/baselines") / f"{name}.json"


def test_no_regression_train():
    """Train notebook should produce consistent outputs."""
    outputs = capture_outputs("examples/ml-pipeline/train.ipynb")

    baseline_path = get_baseline_path("examples/ml-pipeline/train.ipynb")

    if not baseline_path.exists():
        baseline_path.parent.mkdir(parents=True, exist_ok=True)
        baseline_path.write_text(json.dumps(outputs, indent=2))
        print(f"Created baseline: {baseline_path}")

    baseline = json.loads(baseline_path.read_text())
    assert outputs == baseline


def test_no_regression_evaluate():
    """Evaluate notebook should produce consistent outputs."""
    outputs = capture_outputs("examples/ml-pipeline/evaluate.ipynb")

    baseline_path = get_baseline_path("examples/ml-pipeline/evaluate.ipynb")

    if not baseline_path.exists():
        baseline_path.parent.mkdir(parents=True, exist_ok=True)
        baseline_path.write_text(json.dumps(outputs, indent=2))
        print(f"Created baseline: {baseline_path}")

    baseline = json.loads(baseline_path.read_text())
    assert outputs == baseline


def test_notebook_structure_unchanged():
    """Notebook structure should not change unexpectedly."""
    baseline_dir = Path("tests/baselines")
    if not baseline_dir.exists():
        baseline_dir.mkdir(parents=True, exist_ok=True)

    notebooks = [
        "examples/ml-pipeline/train.ipynb",
        "examples/ml-pipeline/evaluate.ipynb",
    ]
    for nb in notebooks:
        hash_file = baseline_dir / f"{Path(nb).stem}.hash"
        current_hash = notebook_hash(nb)

        if not hash_file.exists():
            hash_file.write_text(current_hash)
            print(f"Created hash baseline: {hash_file}")

        baseline = hash_file.read_text()
        assert current_hash == baseline, f"Notebook {nb} has changed"
