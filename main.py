#!/usr/bin/env python3
"""Ship It Friday — one-line git commit message from an AI coding agent
right before it breaks production on a Friday."""

import os

ENTRY = "fix: ship untested code to prod on Friday, my confidence is the whole test suite"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.path.dirname(
        os.path.abspath(__file__)
    )
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
