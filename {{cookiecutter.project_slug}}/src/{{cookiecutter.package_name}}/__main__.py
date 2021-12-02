"""Command-line interface."""
import click


@click.command()
@click.version_option()
def main() -> None:
    """Run the main command of {{cookiecutter.project_slug}}."""


if __name__ == '__main__':
    main(prog_name='{{cookiecutter.package_name}}')
