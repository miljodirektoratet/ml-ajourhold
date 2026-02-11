"""
ml-ajourhold.

A Python project for detecting landcover changes using machine learning. It identifies landscape modifications that are not yet reflected in national geospatial datasets, such as newly built infrastructure.
"""

from importlib.metadata import version

__version__ = version("ml-ajourhold")


def main() -> None:
    """Display a welcome message and version information."""
    print("Hello from ml-ajourhold!")
    print(f"Version: {__version__}")


if __name__ == "__main__":
    main()
