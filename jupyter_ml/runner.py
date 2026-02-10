"""Notebook execution runner."""

import nbclient
import nbformat


def execute(
    notebook: str,
    kernel_name: str | None = None,
    timeout: int | None = None,
    allow_errors: bool = True,
) -> nbformat.NotebookNode:
    """Execute a notebook via nbclient and return the executed notebook.

    Args:
        notebook: Path to the notebook file.
        kernel_name: Kernel name to use (defaults to notebook's kernel).
        timeout: Execution timeout in seconds.
        allow_errors: Continue execution even if cells fail (default: True).

    Returns:
        The executed notebook with outputs.
    """
    nb = nbformat.read(notebook, as_version=nbformat.NO_CONVERT)

    kwargs = {}
    if kernel_name is not None:
        kwargs["kernel_name"] = kernel_name

    client = nbclient.NotebookClient(nb, allow_errors=allow_errors, **kwargs)
    client.execute()

    return nb


def capture_outputs(notebook: str) -> list[dict]:
    """Execute a notebook and capture cell outputs.

    Args:
        notebook: Path to the notebook file.

    Returns:
        List of output dicts for each code cell.
    """
    nb = execute(notebook)
    outputs = []

    for cell in nb.cells:
        if cell.cell_type == "code" and cell.outputs:
            cell_outputs = []
            for out in cell.outputs:
                output_dict = {
                    "output_type": out.output_type,
                }
                # Capture text output
                if hasattr(out, "text"):
                    output_dict["text"] = out.get("text", "")
                # Capture data (rich output)
                if hasattr(out, "data"):
                    output_dict["data"] = out.get("data", {})
                # Capture error details
                if out.output_type == "error":
                    output_dict["ename"] = out.get("ename", "")
                    output_dict["evalue"] = out.get("evalue", "")
                    output_dict["traceback"] = out.get("traceback", [])
                cell_outputs.append(output_dict)

            outputs.append(
                {
                    "index": cell.execution_count,
                    "outputs": cell_outputs,
                }
            )

    return outputs
