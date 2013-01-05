from setuptools import setup, find_packages
import sys, os

version = '0.1'

requires = [
    'pyramid >= 1.4',
    'alembic >= 0.4.1',
    ]

setup(name='pyramid_alembic',
      version=version,
      description="Alembic scaffold for Pyramid 1.4",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='Jon Rosebaugh',
      author_email='jon@inklesspen.com',
      url='',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=True,
      install_requires=requires,
      entry_points="""
      # -*- Entry points: -*-
      [pyramid.scaffold]
      alembic_mako=pyramid_alembic:AlembicProjectTemplate
      """,
      )
