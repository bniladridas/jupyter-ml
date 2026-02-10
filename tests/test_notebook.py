"""Tests for notebook utilities."""

from pathlib import Path
from jupyter_ml import notebook


def test_notebook_hash() -> None:
    """Test stable hash computation."""
    nb = notebook.load("examples/basic.ipynb")
    hash1 = notebook.notebook_hash(nb)
    hash2 = notebook.notebook_hash(nb)
    assert hash1 == hash2
    assert len(hash1) == 16


def test_notebook_diff() -> None:
    """Test notebook comparison."""
    result = notebook.notebook_diff("examples/basic.ipynb", "examples/basic.ipynb")
    assert result["changed"] is False
    assert result["cells_added"] == 0
    assert result["cells_removed"] == 0


def test_load_save_roundtrip(tmp_path: Path) -> None:
    """Test load/save roundtrip."""
    nb = notebook.load("examples/basic.ipynb")
    path = tmp_path / "output.ipynb"
    notebook.save(nb, str(path))
    nb2 = notebook.load(str(path))
    assert len(nb2.cells) == len(nb.cells)
