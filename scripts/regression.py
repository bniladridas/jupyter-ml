"""CLI for notebook regression tester."""

import argparse
import json
from pathlib import Path

from jupyter_ml.runner import capture_outputs
from jupyter_ml.notebook import notebook_hash, notebook_diff


def main() -> None:
    parser = argparse.ArgumentParser("nrt")
    parser.add_argument("notebook", help="Notebook to test")
    parser.add_argument("--baseline", help="Baseline JSON file", default=None)
    parser.add_argument("--hash", action="store_true", help="Show notebook hash")
    parser.add_argument("--diff", help="Compare against another notebook")

    args = parser.parse_args()

    if args.hash:
        h = notebook_hash(args.notebook)
        print(f"Hash: {h}")
        return

    if args.diff:
        result = notebook_diff(args.notebook, args.diff)
        print(f"Changed: {result['changed']}")
        print(f"Hash (before): {result['hash1']}")
        print(f"Hash (after): {result['hash2']}")
        print(f"Cells added: {result['cells_added']}")
        print(f"Cells removed: {result['cells_removed']}")
        return

    outputs = capture_outputs(args.notebook)
    print(json.dumps(outputs, indent=2))


if __name__ == "__main__":
    main()
