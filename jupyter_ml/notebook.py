"""Notebook utilities."""

import json
import hashlib
import nbformat
from typing import Any


def load(path: str) -> nbformat.NotebookNode:
    """Load a notebook from path."""
    return nbformat.read(path, as_version=nbformat.NO_CONVERT)


def save(nb: nbformat.NotebookNode, path: str) -> None:
    """Save a notebook to path."""
    nbformat.write(nb, path)


def notebook_hash(nb: nbformat.NotebookNode | str) -> str:
    """Compute a stable hash of a notebook's structure.

    Ignores execution counts and timing metadata.
    """
    if isinstance(nb, str):
        nb = load(nb)

    canonical = {
        "cells": [
            {
                "cell_type": cell.cell_type,
                "source": cell.source,
            }
            for cell in nb.cells
        ],
        "metadata": {
            k: v
            for k, v in nb.metadata.items()
            if k not in ("metadata", "outputs", "execution_count")
        },
    }
    content = json.dumps(canonical, sort_keys=True)
    return hashlib.sha256(content.encode()).hexdigest()[:16]


def notebook_diff(
    nb1: nbformat.NotebookNode | str,
    nb2: nbformat.NotebookNode | str,
) -> dict[str, Any]:
    """Compare two notebooks and return a diff.

    Args:
        nb1: First notebook or path.
        nb2: Second notebook or path.

    Returns:
        Dict with 'changed', 'hash1', 'hash2', 'cells_added', 'cells_removed'.
    """
    if isinstance(nb1, str):
        nb1 = load(nb1)
    if isinstance(nb2, str):
        nb2 = load(nb2)

    hash1 = notebook_hash(nb1)
    hash2 = notebook_hash(nb2)

    return {
        "changed": hash1 != hash2,
        "hash1": hash1,
        "hash2": hash2,
        "cells_added": max(0, len(nb2.cells) - len(nb1.cells)),
        "cells_removed": max(0, len(nb1.cells) - len(nb2.cells)),
    }
