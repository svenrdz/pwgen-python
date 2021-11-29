#!/usr/bin/env python3
import click
from .core import Pwgen
from .utils import Sha1File

__all__ = ["Pwgen"]

CONTEXT_SETTINGS = dict(help_option_names=["-h", "--help"])
LINE_MAXLEN = 80
NUM_LINES = 20


def format_output(passwords):
    if passwords:
        pw_length = len(passwords[0])
    else:
        pw_length = 0
    if LINE_MAXLEN > pw_length * 2 + 1:
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
@click.argument("num_pw", default=1)
@click.option("-N", "--num-passwords", default=None)
@click.option("-H", "--sha1", type=Sha1File())
@click.option("-S", "--seed", type=str, default=None)
@click.option("-f", "--fillscreen", is_flag=True, default=True)
def cli(pw_length, num_pw, num_passwords, sha1, seed, fillscreen):
    if fillscreen:
        nb_per_line = LINE_MAXLEN // (pw_length + 1)
        num_pw = NUM_LINES * nb_per_line
    elif num_pw is None:
        num_pw = num_passwords
    if sha1:
        seed = sha1
    pwgen = Pwgen(pw_length=pw_length, num_pw=num_pw, seed=seed)
    passwords = pwgen.generate()
    formatted = format_output(passwords)
    click.echo(formatted)


if __name__ == "__main__":
    cli()
