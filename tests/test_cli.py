import json
import pytest
from pathlib import Path
from click.testing import CliRunner

from pwgen_python import cli


def enum_output(output: str) -> list[tuple[int, str]]:
    output_list = output.replace(" ", "\n").split()
    for i, pwd in enumerate(output_list):
        yield i, pwd


def split_output(output: str) -> list[str]:
    for i, pwd in enum_output(output):
        yield pwd


PW_FILE = Path(__file__).parent / "passwords.json"
with open(PW_FILE) as passwords:
    PW_DICT = json.load(passwords)


def pytest_generate_tests(metafunc):
    """Test scenarios to avoid copy-pasting the same seed
    parameters for each test.

    https://docs.pytest.org/en/6.2.x/example/parametrize.html#a-quick-port-of-testscenarios
    """
    idlist = []
    argvalues = []
    if metafunc.cls is not None:
        for scenario in metafunc.cls.scenarios:
            idlist.append(scenario[0])
            items = scenario[1].items()
            argnames = [x[0] for x in items]
            argvalues.append([x[1] for x in items])
        metafunc.parametrize(argnames, argvalues, ids=idlist, scope="class")


class TestCliStrSeed:
    scenarios = [
        (
            "seed1",
            {
                "opts": ["--seed", PW_DICT[0]["seed"]],
                "passwords": PW_DICT[0]["passwords"],
            },
        ),
        (
            "seed2",
            {
                "opts": ["--seed", PW_DICT[1]["seed"]],
                "passwords": PW_DICT[1]["passwords"],
            },
        ),
    ]

    def test_no_args_no_opts(self, opts, passwords):
        runner = CliRunner()
        result = runner.invoke(cli, opts)
        assert result.exit_code == 0
        output = list(split_output(result.output))
        assert len(output) == len(passwords)
        for pwd, expected in zip(output, passwords):
            assert pwd == expected

    def test_opt_1(self, opts, passwords):
        runner = CliRunner()
        opts += ["-1"]
        result = runner.invoke(cli, opts)
        assert result.exit_code == 0
        output = list(split_output(result.output))
        assert len(output) == 1
        for pwd, expected in zip(output, passwords):
            assert pwd == expected

    def test_opt_1_with_num_passwords_10(self, opts, passwords):
        runner = CliRunner()
        opts += ["-1", "--num-passwords", "10"]
        result = runner.invoke(cli, opts)
        assert result.exit_code == 0
        output = list(split_output(result.output))
        assert len(output) == 10
        for pwd, expected in zip(output, passwords):
            assert pwd == expected

    def test_arg_num_pw(self, opts, passwords):
        runner = CliRunner()
        opts += ["8", "10"]
        result = runner.invoke(cli, opts)
        assert result.exit_code == 0
        output = list(split_output(result.output))
        assert len(output) == 10
        for pwd, expected in zip(output, passwords):
            assert pwd == expected


class TestCliSha1Seed:
    scenarios = [
        (
            "pw_file",
            {
                "opts": ["8", "1", "--sha1", str(PW_FILE)],
                "password": "jElQ9bXA",
            },
        ),
        (
            "pw_file_with_hash",
            {
                "opts": ["8", "1", "--sha1", str(PW_FILE) + "#seed"],
                "password": "ilKYAUz0",
            },
        ),
    ]

    def test_sha1file(self, opts, password):
        runner = CliRunner()
        result = runner.invoke(cli, opts)
        assert result.exit_code == 0
        output = result.output.strip()
        assert output == password


def test_no_passwords():
    runner = CliRunner()
    opts = ["-N", "0"]
    result = runner.invoke(cli, opts)
    assert result.exit_code == 0
    assert result.output.strip() == ""


@pytest.mark.parametrize("num_pw", [40, 200])
def test_one_per_line(num_pw):
    runner = CliRunner()
    opts = ["--line", "-N", str(num_pw)]
    result = runner.invoke(cli, opts)
    assert result.exit_code == 0
    output = list(split_output(result.output))
    assert len(output) == num_pw


@pytest.mark.parametrize("length", [40, 200])
def test_long_passwords_one_per_line(length):
    runner = CliRunner()
    opts = [str(length)]
    result = runner.invoke(cli, opts)
    assert result.exit_code == 0
    output = list(split_output(result.output))
    assert len(output) == 20
