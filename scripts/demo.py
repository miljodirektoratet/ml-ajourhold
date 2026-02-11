#!/usr/bin/env python3
"""
Example script demonstrating usage of the ml_ajourhold package.

This script shows how to import and use the ml_ajourhold module in a standalone script.
It can be run directly or used as a template for building more complex workflows.

Usage:
    python scripts/demo.py
    # or
    uv run python scripts/demo.py
"""

import ml_ajourhold


def main() -> None:
    """Run example usage of ml_ajourhold package."""
    print("=" * 60)
    print("ML-Ajourhold Example Script")
    print("=" * 60)
    print()

    # Call the main function from the package
    ml_ajourhold.main()
    print()

    # Access version information
    print(f"Package version: {ml_ajourhold.__version__}")
    print()


if __name__ == "__main__":
    main()
