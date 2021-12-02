"""Test cases for the __main__ module."""
import pytest
from click.testing import CliRunner

from {{cookiecutter.package_name}} import __main__


@pytest.fixture()
def runner() -> CliRunner:
    """Create a CLI runner for the tests."""
    return CliRunner()


def test_main_succeeds(runner: CliRunner) -> None:
    """Ensure that the main program exits with a status code of zero."""
    result = runner.invoke(__main__.main)
    assert result.exit_code == 0
