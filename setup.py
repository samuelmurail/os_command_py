#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Create the pipy:
# python setup.py sdist
# twine check dist/*
# twine upload dist/*

# Create conda env:
# conda update conda
# conda env create --name test -f=.conda.yml
# conda activate test
# conda deactivate

from setuptools import setup, find_packages


setup(
    name='os_command_py',
    version="1.0.2",
    packages=find_packages(),
    description='os_command_py is a python library allowing a simplified use of the OS commands.',
    long_description=open('README.rst', encoding='utf-8').read(),
    long_description_content_type='text/x-rst',
    author='Samuel Murail',
    author_email='samuel.murail@u-paris.fr',
    url='https://github.com/samuelmurail/os_command_py',
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.5",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
    ],
    install_requires=[
        "pytest",
        "sphinx_rtd_theme",
        "sphinx-argparse",
        "nbsphinx",
    ],
    include_package_data=True,
)
