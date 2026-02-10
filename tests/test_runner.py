"""Tests for notebook runner."""

from pathlib import Path
from jupyter_ml import runner


def test_execute_notebook() -> None:
    """Test notebook execution returns executed notebook."""
    nb = runner.execute("examples/basic.ipynb")
    assert nb is not None
    assert hasattr(nb, "cells")


def test_capture_outputs() -> None:
    """Test output capture from executed notebook."""
    outputs = runner.capture_outputs("examples/basic.ipynb")
    assert isinstance(outputs, list)
