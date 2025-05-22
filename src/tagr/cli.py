import click


@click.group(help="A minimal, user-friendly CLI tool for editing audio file metadata.")
@click.version_option()
def cli() -> None: ...
