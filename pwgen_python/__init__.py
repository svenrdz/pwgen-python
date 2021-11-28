import click
from .core import Pwgen


@click.command()
def cli():
    pwgen = Pwgen()
    click.echo(pwgen.run())


if __name__ == "__main__":
    cli()
