"""Agent core for notebook-centric ML automation."""

import nbformat
from pathlib import Path
from typing import Any


class JupyterMLAgent:
    """Minimal ML agent bound to a Jupyter runtime."""

    def __init__(self, kernel: str = "python3"):
        self.kernel = kernel

    def inspect(self, notebook_path: str) -> dict[str, Any]:
        """Inspect a notebook and return structured metadata."""
        nb = nbformat.read(notebook_path, as_version=nbformat.NO_CONVERT)
        return {
            "notebook": str(Path(notebook_path).resolve()),
            "kernel": self.kernel,
            "status": "ready",
            "cells": len(nb.cells),
        }

    def trace(self, notebook_path: str) -> dict[str, Any]:
        """Capture cell-level execution traces."""
        nb = nbformat.read(notebook_path, as_version=nbformat.NO_CONVERT)
        traces = []
        for i, cell in enumerate(nb.cells):
            if cell.cell_type == "code":
                traces.append(
                    {
                        "index": i,
                        "source": cell.source,
                        "execution_count": cell.get("execution_count"),
                    }
                )
        return {
            "notebook": notebook_path,
            "traces": traces,
        }

    def execute(self, path: str | Path) -> None:
        """Execute a notebook (placeholder for kernel integration)."""
        nb = nbformat.read(path, as_version=nbformat.NO_CONVERT)
        for cell in nb.cells:
            if cell.cell_type == "code":
                print(f"[exec] {cell.source[:50]}...")
