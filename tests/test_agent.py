"""Tests for JupyterMLAgent."""

from jupyter_ml.agent import JupyterMLAgent


def test_agent_inspect_basic() -> None:
    """Test basic notebook inspection."""
    agent = JupyterMLAgent()

    nb_path = "examples/basic.ipynb"
    result = agent.inspect(nb_path)

    assert "notebook" in result
    assert "kernel" in result
    assert "status" in result
    assert result["cells"] == 1


def test_agent_trace() -> None:
    """Test cell-level trace capture."""
    agent = JupyterMLAgent()

    nb_path = "examples/basic.ipynb"
    result = agent.trace(nb_path)

    assert "notebook" in result
    assert "traces" in result
    assert len(result["traces"]) == 1
    assert result["traces"][0]["index"] == 0


def test_agent_init() -> None:
    """Test agent initialization."""
    agent = JupyterMLAgent()
    assert agent is not None
