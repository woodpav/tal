#!/usr/bin/env python3

import subprocess


def with_bucket_name(func):
    def deco(name, *original_args, **original_kwargs):
        name = f"gs://{name}/"
        return func(name, *original_args, **original_kwargs)

    return deco


@with_bucket_name
def create_bucket(bucket_name):
    try:
        subprocess.check_call(["gsutil", "mb", bucket_name])
    except subprocess.CalledProcessError:
        pass
    else:
        subprocess.call(["gsutil", "ls", "-L", "-b", bucket_name])
        print("Success!")


@with_bucket_name
def delete_bucket(bucket_name):
    try:
        subprocess.check_call(["gsutil", "rm", "-r", bucket_name])
    except subprocess.CalledProcessError:
        pass
    else:
        print("Success!")
