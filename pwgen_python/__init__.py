#!/usr/bin/env python3
import click
from .core import Pwgen
from .utils import Sha1File

__all__ = ["Pwgen"]

CONTEXT_SETTINGS = dict(help_option_names=["-h", "--help"])
LINE_MAXLEN = 80
NUM_LINES = 20


def format_output(passwords, columns):
    if passwords:
        pw_length = len(passwords[0])
    else:
        pw_length = 0
    if LINE_MAXLEN > pw_length * 2 + 1 and columns:
        lines = [""]
        for pw in passwords:
            line = lines[-1]
            if len(line) > 0:
                line += " "
            line += pw
            if len(line) >= LINE_MAXLEN:
                lines.append(pw)
            else:
                lines[-1] = line
    else:
        lines = passwords
    return "\n".join(lines)


@click.command(context_settings=CONTEXT_SETTINGS)
@click.argument("pw_length", default=8)
@click.argument("num_pw", default=-1)  # -1 for `num_pw` to be optional
@click.option(
    "-N",
    "--num-passwords",
    type=int,
    help="Number of generated passwords. Lower precedence than `NUM_PW`",
)
@click.option(
    "-H",
    "--sha1",
    type=Sha1File(),
    help="Seed from file. Optional string seed after #",
)
@click.option("-S", "--seed", type=str, help="Seed from string.")
@click.option(
    "-1", "one", is_flag=True, default=False, help="Generate 1 password."
)
@click.option(
    "-C/-L",
    "--columns / --line",
    is_flag=True,
    default=True,
    help="Output format: `-C` columns, `-1` one per line. [default: columns]",
)
def cli(pw_length, num_pw, num_passwords, sha1, seed, one, columns):
    if one:
        _num_pw = 1
    elif columns and pw_length < LINE_MAXLEN:
        nb_per_line = LINE_MAXLEN // (pw_length + 1)
        _num_pw = NUM_LINES * nb_per_line
    else:
        _num_pw = NUM_LINES
    if num_pw >= 0:
        _num_pw = num_pw
    elif num_passwords is not None:
        _num_pw = num_passwords
    if sha1:
        seed = sha1
    pwgen = Pwgen(pw_length=pw_length, num_pw=_num_pw, seed=seed)
    passwords = pwgen.generate()
    formatted = format_output(passwords, columns)
    click.echo(formatted)


if __name__ == "__main__":
    cli()
