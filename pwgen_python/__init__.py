#!/usr/bin/env python3
import click
from .core import Pwgen
from .utils import Sha1File, GeneratorFlags as gf

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
    "-1", "one", is_flag=True, default=False, help="Generate 1 password."
)
@click.option("-S", "--seed", type=str, help="Seed from string.")
@click.option(
    "-H",
    "--sha1",
    type=Sha1File(),
    help="Seed from file. Optional string seed after #",
)
@click.option(
    "-C/-L",
    "--columns / --line",
    is_flag=True,
    default=True,
    help="Output format. [default: columns]",
)
@click.option(
    "-s/-r",
    "--secure/--readable",
    is_flag=True,
    default=False,
    help="Enable/disable secure password generation. [default: readable]",
)
@click.option(
    "-V/-v",
    "--vowels/--no-vowels",
    is_flag=True,
    default=True,
    help="Enable/disable use of vowels. [default: vowels]",
)
@click.option(
    "-D/-d",
    "--digits/--no-digits",
    is_flag=True,
    default=True,
    help="Enable/disable use of digits. [default: digits]",
)
@click.option(
    "-u/-l",
    "--uppercase/--lowercase",
    is_flag=True,
    default=True,
    help="Enable/disable use of uppercase letters. [default: uppercase]",
)
@click.option(
    "-y",
    "--symbols",
    is_flag=True,
    default=False,
    help="Enable use of symbols. [default: False]",
)
@click.option(
    "-a",
    "--no-ambiguous",
    is_flag=True,
    default=False,
    help="Disable use of ambiguous characters. [default: False]",
)
def cli(
    pw_length,
    num_pw,
    num_passwords,
    one,
    seed,
    sha1,
    columns,
    secure,
    vowels,
    digits,
    uppercase,
    symbols,
    no_ambiguous,
):
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
    flags = gf(0)
    if secure:
        flags |= gf.Secure
    if vowels:
        flags |= gf.Vowels
    if digits:
        flags |= gf.Digits
    if uppercase:
        flags |= gf.Uppercase
    if symbols:
        flags |= gf.Symbols
    if no_ambiguous:
        flags |= gf.NoAmbiguous
    pwgen = Pwgen(pw_length=pw_length, num_pw=_num_pw, seed=seed, flags=flags)
    passwords = pwgen.generate()
    formatted = format_output(passwords, columns)
    click.echo(formatted)


if __name__ == "__main__":
    cli()
