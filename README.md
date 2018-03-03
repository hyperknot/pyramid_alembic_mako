# This project is archived now, use pyramid-cookiecutter-alchemy instead
https://github.com/Pylons/pyramid-cookiecutter-alchemy

pyramid_alembic_mako
====================

If installing from git, you must have `setuptools_git` installed, or setuptools won't realize the scaffold's template directory is part of the package.

Pyramid Alembic/SQLAlchemy project scaffold using url dispatch and Mako templates

Use alembic to generate revisions before you run initializedb. Example:

`alembic -c development.ini revision --autogenerate -m "starting"`

Then you can use alembic to upgrade to that revision:

`alembic -c development.ini upgrade head`

Or initializedb:

`initialize_myapp_db development.ini`
