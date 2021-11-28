import pytest
from click.testing import CliRunner

from pwgen_python import cli


def enum_output(output: str) -> list[tuple[int, str]]:
    output_list = output.replace(" ", "\n").split()
    for i, pwd in enumerate(output_list):
        yield i, pwd


def split_output(output: str) -> list[str]:
    for i, pwd in enum_output(output):
        yield pwd


def test_output():
    runner = CliRunner()
    result = runner.invoke(cli)
    assert result.exit_code == 0
    for pwd in split_output(result.output):
        assert pwd == "aaaaaaaa"
