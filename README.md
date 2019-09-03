# tal

Deploys python GCP Functions with private git requirements.

### Install

    pip install tal

### Deploying Functions:


  1. Add the following to `main.py`

          import sys
          sys.path.append('lib')

  1. Put git dependencies in `private_requirements.txt`.
  2. Make sure there is no `lib/` directory.
  3. Run `tal func deploy my_func --stage dev`.


### Creating Repositories:

  1. Run `tal repo create my_repo`


### Creating Buckets:

  1. Run `tal storage create-bucket my_bucket`


### Deleting Buckets:

  1. Run `tal storage delete-bucket my_bucket`


### Uploading Files:

  1. Run `tal storage upload my_file.txt --bucket=my_bucket --path=my/nested/path`


### Inspiration

Build like Tal: https://www.youtube.com/watch?v=CF6w2-WNZLE
