"""Tests for the main ml_ajourhold module."""

import pytest

# Add the src directory to the Python path if not already added
# sys.path.insert(0, str(Path(__file__).parent.parent.parent / "src"))

from ml_ajourhold import main


def test_main_function_output(capsys) -> None:
    """Test that the main function prints the expected output."""
    main()
    captured = capsys.readouterr()
    assert "Hello from ml-ajourhold!" in captured.out
    assert "Version:" in captured.out
