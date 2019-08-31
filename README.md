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


### Inspiration

Build like Tal: https://www.youtube.com/watch?v=CF6w2-WNZLE
