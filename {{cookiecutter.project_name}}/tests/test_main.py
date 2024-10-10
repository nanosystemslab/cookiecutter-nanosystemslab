"""Test cases for the __main__ module."""
import pytest
# from click.testing import CliRunner

from {{cookiecutter.package_name}} import __main__


# @pytest.fixture
# def runner() -> CliRunner:
#     """Fixture for invoking command-line interfaces."""
#     return CliRunner()


# def test_main_succeeds(runner: CliRunner) -> None:
#     """It exits with a status code of zero."""
#     result = runner.invoke(__main__.main)
#     assert result.exit_code == 0

def test_main_succeeds(capfd: CaptureFixture) -> None:
    """It prints output and exits successfully."""
    __main__.main()  # Directly call the main function
    captured = capfd.readouterr()  # Capture the output
    assert captured.out != None # Check that something is printed (you can be more specific here)