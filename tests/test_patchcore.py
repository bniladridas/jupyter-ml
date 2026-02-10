"""Test jupyter-ml integration with patchcore notebook."""

import os

from jupyter_ml.runner import capture_outputs
from jupyter_ml.notebook import notebook_hash


PATCHCORE_NOTEBOOK = "/Users/niladri/Desktop/patchcore/mlx_anomalib_notebook.ipynb"


def require_notebook(path):
    if not os.path.exists(path):
        import pytest

        pytest.skip(f"Patchcore notebook not found: {path}")


def test_patchcore_notebook_executes():
    """Test that patchcore notebook executes via jupyter-ml."""
    require_notebook(PATCHCORE_NOTEBOOK)
    outputs = capture_outputs(PATCHCORE_NOTEBOOK)
    assert len(outputs) > 0


def test_patchcore_notebook_no_errors():
    """Test that patchcore notebook has no errors."""
    require_notebook(PATCHCORE_NOTEBOOK)
    outputs = capture_outputs(PATCHCORE_NOTEBOOK)
    for cell in outputs:
        for out in cell.get("outputs", []):
            assert out.get("output_type") != "error"


def test_patchcore_notebook_hash():
    """Test stable hash for patchcore notebook."""
    require_notebook(PATCHCORE_NOTEBOOK)
    h = notebook_hash(PATCHCORE_NOTEBOOK)
    assert len(h) == 16
