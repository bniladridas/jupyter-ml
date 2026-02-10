# jupyter-ml Agent Design (Internal)

> This document describes the internal agent design for jupyter-ml.
> It is intended for internal contributors and will be open-sourced
> once APIs settle.

## Vision

Notebook-native ML agent infrastructure that:
- Works as a CLI, library, and agent
- Integrates with Jupyter ecosystem (nbformat, nbclient, jupyter_kernel_client)
- Supports LLM backends (OpenAI, Gemini, local)
- Provides kernel-level tracing and execution monitoring

## Architecture

```
┌─────────────────────────────────────────────────────────┐
│                    jupyter-ml                           │
├─────────────────────────────────────────────────────────┤
│  CLI          Agent Core        Runner        LLM       │
│  ───          ─────────        ──────        ───        │
│  main.py  →   agent.py     →   runner.py  →  llm.py     │
│               trace()          run()        complete(). │
├─────────────────────────────────────────────────────────┤
│  Jupyter Ecosystem (nbformat, nbclient, ipykernel)      │
├─────────────────────────────────────────────────────────┤
│  Notebooks (ipynb), Kernels (python3, julia, R), LLM    │
└─────────────────────────────────────────────────────────┘
```

## Agent Contract

### JupyterMLAgent

```python
class JupyterMLAgent:
    """Minimal ML agent bound to a Jupyter runtime."""

    def __init__(self, kernel: str = "python3"):
        """Initialize agent with kernel name."""
        self.kernel = kernel

    def inspect(self, notebook_path: str) -> dict[str, Any]:
        """Inspect notebook and return structured metadata."""
        ...

    def trace(self, notebook_path: str) -> dict[str, Any]:
        """Capture cell-level execution traces."""
        ...

    def execute(self, notebook_path: str) -> None:
        """Execute notebook via kernel."""
        ...
```

## Integration Points

### nbformat
- Read/write notebook `.ipynb` files
- Cell extraction and metadata

### nbclient
- Kernel communication
- Execution streaming
- Output collection

### jupyter_kernel_client
- Kernel lifecycle management
- Message channels (shell, iopub, stdin, control)

### ipykernel
- Python kernel for local execution
- Alternative: jupyter-xeus-[clang,julia,R]

## LLM Integration

### OpenAI
```python
from jupyter_ml.llm import openai_completion
openai_completion("Explain this notebook...")
```

### Gemini
```python
from jupyter_ml.llm import gemini_completion
gemini_completion("Summarize cell outputs...")
```

### Local (Ollama)
```python
from jupyter_ml.llm import local_completion
local_completion("Generate next cell...")
```

## Future: Jupyter Org Contribution

When APIs settle, this repo may be proposed to:
- https://github.com/jupyter/agent
- https://github.com/jupyter/nbclient
- https://github.com/jupyter/jupyter_kernel_client

See: https://jupyter.org/governance

## Versioning

- Major version: Jupyter ecosystem compatibility
- Minor version: Agent features
- Patch: Bug fixes

## Status

**Experimental** — APIs subject to change.

## Commit Author Configuration

When working with this repository, configure git and use co-authors.

### Git Config

```bash
# Set for this repository
git config user.name "jupyter[ml]"
git config user.email "jupyter-ml-bot@users.noreply.github.com"
git config commit.gpgsign false
```

### Creating Commits with Both Authors

All commits must include both authors as co-authors:

```bash
git commit -m "message

Co-authored-by: jupyter[ml] <jupyter-ml-bot@users.noreply.github.com>
Co-authored-by: Niladri Das <bniladridas@users.noreply.github.com>"
```

### Amending Commits

```bash
git commit --amend --no-edit -m "message

Co-authored-by: jupyter[ml] <jupyter-ml-bot@users.noreply.github.com>
Co-authored-by: Niladri Das <bniladridas@users.noreply.github.com>"

git push --force
```
