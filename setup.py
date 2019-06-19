"""This file installs the dependencies
   needed for the Birdman CLI.
"""

from setuptools import setup

setup(
    name="main",
    version="0.1",
    py_modules=["main"],
    install_requires=[
        "Click>=7.0",
        "colorama"
    ],
    entry_points='''
        [console_scripts]
        birdman=main:details
    '''
)
