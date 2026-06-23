#!/usr/bin/env python3
"""Basic script scaffold for the project."""

from __future__ import annotations

import argparse
import sys


def parse_args() -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description="Run the DevAscDemo helper script."
    )
    parser.add_argument(
        "--name",
        default="World",
        help="Name to greet.",
    )
    return parser.parse_args()


def main() -> int:
    """Main entry point for the script."""
    args = parse_args()
    print(f"Hello, {args.name}!")
    print(f"Welcome to the DevAscDemo, {args.name}!")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
