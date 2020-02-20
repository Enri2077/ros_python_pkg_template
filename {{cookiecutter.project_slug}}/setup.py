#!/usr/bin/env python

from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

# for your packages to be recognized by python
d = generate_distutils_setup(
 packages=['{{cookiecutter.project_slug}}_ros'],
 package_dir={'{{cookiecutter.project_slug}}_ros': 'src/{{cookiecutter.project_slug}}_ros'}
)

setup(**d)
