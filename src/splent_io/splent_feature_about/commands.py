"""
CLI commands contributed by splent_feature_about.

These commands are auto-discovered by the framework and exposed in the
SPLENT CLI under the ``feature:about`` group.

Usage::

    splent feature:about hello
"""

import click


@click.command("hello")
def hello():
    """Example command — replace with your own."""
    click.echo("  Hello from splent_feature_about!")


cli_commands = [hello]
