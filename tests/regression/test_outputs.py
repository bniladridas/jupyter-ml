"""Test notebook outputs for regression detection."""

from jupyter_ml.runner import capture_outputs
from jupyter_ml.notebook import notebook_hash


def test_train_notebook_outputs():
    """Capture outputs from train.ipynb."""
    outputs = capture_outputs("examples/ml-pipeline/train.ipynb")
    assert len(outputs) == 3
    assert outputs[0]["index"] == 1
    assert outputs[1]["index"] == 2
    assert outputs[2]["index"] == 3


def test_evaluate_notebook_outputs():
    """Capture outputs from evaluate.ipynb."""
    outputs = capture_outputs("examples/ml-pipeline/evaluate.ipynb")
    assert len(outputs) == 2


def test_notebook_hash_stable():
    """Hash should be stable for same content."""
    hash1 = notebook_hash("examples/ml-pipeline/train.ipynb")
    hash2 = notebook_hash("examples/ml-pipeline/train.ipynb")
    assert hash1 == hash2


def test_notebook_hash_different():
    """Different notebooks should have different hashes."""
    hash1 = notebook_hash("examples/ml-pipeline/train.ipynb")
    hash2 = notebook_hash("examples/ml-pipeline/evaluate.ipynb")
    assert hash1 != hash2
