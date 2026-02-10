"""CLI entry point for jupyter-ml."""

import argparse
from jupyter_ml.agent import JupyterMLAgent


def main() -> None:
    parser = argparse.ArgumentParser("jupyter-ml")
    parser.add_argument("notebook")
    args = parser.parse_args()

    agent = JupyterMLAgent()
    result = agent.inspect(args.notebook)
    print(result)
