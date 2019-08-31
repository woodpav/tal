#!/usr/bin/env python3

import click

from .func import func


@click.group()
def cli():
    pass


cli.add_command(func)
