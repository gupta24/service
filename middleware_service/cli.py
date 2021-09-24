import os
import sys
from .version import __version__


try:
    import click
except ImportError:
    sys.stderr.write('It seems middleware_service is not installed with cli option. \n'
                     'Run pip install "middleware_service[cli]" to fix this.')
    sys.exit(1)



@click.group()
@click.version_option(version=__version__)
@click.pass_context
def cli(ctx):
    pass


if __name__ == "__main__":
    cli()