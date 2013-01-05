pyramid_alembic_mako
====================

Pyramid Alembic/SQLAlchemy project scaffold using url dispatch and Mako templates

Use alembic to generate revisions before you run initializedb. Example:

`alembic -c development.ini revision --autogenerate -m "starting"`

Then you can use alembic to upgrade to that revision:

`alembic -c development.ini upgrade head`

Or initializedb:

`initialize_myapp_db development.ini`
