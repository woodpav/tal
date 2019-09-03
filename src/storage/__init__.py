#!/usr/bin/env python3

import click

from . import buckets
from . import files


@click.group()
def storage():
    pass


@storage.command()
@click.argument("bucket_name")
def create_bucket(bucket_name):
    buckets.create_bucket(bucket_name)


@storage.command()
@click.argument("bucket_name")
def delete_bucket(bucket_name):
    message = f"Wait! To irreversibly delete bucket {bucket_name}, enter its bucket_name"
    value = click.prompt(message, type=str)
    if value == bucket_name:
        buckets.delete_bucket(bucket_name)
