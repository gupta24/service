import click
from .version import __version__

@click.command()
@click.argument('name')
@click.option('--version', '-V', help='version of the package')
def main(name, version):
    click.echo(f"{name}-{version}")


if __name__ == '__main__':
    main()