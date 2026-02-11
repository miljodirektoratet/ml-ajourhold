"""Common test fixtures for the ml-ajourhold project."""

from pathlib import Path
from typing import Dict, Generator, List
import pytest
import tempfile
import json


@pytest.fixture
def sample_data() -> List[str]:
    """
    Provide sample data for testing.

    :return: List of sample strings.
    """
    return ["  hello world  ", "python testing", "", "  ml_ajourhold  ", "unit tests"]


@pytest.fixture
def sample_config() -> Dict[str, str]:
    """
    Provide sample configuration for testing.

    :return: Dictionary with sample configuration.
    """
    return {"name": "ml-ajourhold", "version": "1.0.0", "environment": "test"}


@pytest.fixture
def temp_config_file(sample_config: Dict[str, str]) -> Generator[Path, None, None]:
    """
    Create a temporary configuration file for testing.

    :param sample_config: Configuration data to write.
    :return: Path to temporary configuration file.
    """
    with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
        json.dump(sample_config, f)
        temp_path = Path(f.name)

    yield temp_path

    # Cleanup
    if temp_path.exists():
        temp_path.unlink()


@pytest.fixture
def temp_keyvalue_file() -> Generator[Path, None, None]:
    """
    Create a temporary key=value configuration file for testing.

    :return: Path to temporary key=value file.
    """
    content = """
# ml-ajourhold test configuration
name=ml-ajourhold
version=1.0.0
environment=test
debug=true
"""

    with tempfile.NamedTemporaryFile(mode="w", suffix=".conf", delete=False) as f:
        f.write(content)
        temp_path = Path(f.name)

    yield temp_path

    # Cleanup
    if temp_path.exists():
        temp_path.unlink()


class MockLogger:
    """Mock logger for testing logging functionality."""

    def __init__(self):
        """Initialize mock logger."""
        self.messages = []

    def info(self, msg: str, *args) -> None:
        """Mock info logging."""
        self.messages.append(("INFO", msg % args if args else msg))

    def warning(self, msg: str, *args) -> None:
        """Mock warning logging."""
        self.messages.append(("WARNING", msg % args if args else msg))

    def debug(self, msg: str, *args) -> None:
        """Mock debug logging."""
        self.messages.append(("DEBUG", msg % args if args else msg))

    def error(self, msg: str, *args) -> None:
        """Mock error logging."""
        self.messages.append(("ERROR", msg % args if args else msg))


@pytest.fixture
def mock_logger() -> MockLogger:
    """
    Provide a mock logger for testing.

    :return: Mock logger instance.
    """
    return MockLogger()
