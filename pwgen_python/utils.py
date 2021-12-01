import click
import typing as t
from pathlib import Path
from hashlib import sha1


class Sha1File(click.ParamType):
    """
    Custom click.ParamType that opens a file and hashes its bytes content.
    Add extra seed after the path separated with `#`.
    """

    name = "/path/to/file[#seed]"

    def convert(
        self,
        value: str,
        param: t.Optional["Parameter"],
        ctx: t.Optional["Context"],
    ):
        if "#" in value:
            path, opt_seed = value.split("#")
        else:
            path, opt_seed = value, ""
        path = Path(path)
        if not path.is_file():
            raise ValueError(self.fail(f'"{path}" is not a file.', param, ctx))
        with path.open("rb") as f:
            content = b"".join(f.readlines())
        return sha1(content + opt_seed.encode()).digest()


def assert_natural(name: str, value: int):
    assert (
        isinstance(value, int) and value >= 0
    ), f"{name} ({value}) should be >= 0"
