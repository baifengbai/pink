#!/usr/bin/env python
# coding=utf-8

from setuptools import setup

# RELEASE STEPS
# $ python setup.py bdist_wheel
# $ python twine upload dist/VX.Y.Z.whl
# $ git tag -a VX.Y.Z -m "release version VX.Y.Z"
# $ git push origin VX.Y.Z

NAME = "pink"
VERSION = "0.2.0"
URL = "https://github.com/chenjiandongx/pink"
AUTHOR = "chenjiandongx"
AUTHOR_EMAIL = "chenjiandongx@qq.com"
LICENSE = "MIT"
REQUIRES = ["black", "glob2"]
MODULES = ["pink"]
DESC = "reformatted code via the command line."


setup(
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    name=NAME,
    version=VERSION,
    license=LICENSE,
    install_requires=REQUIRES,
    url=URL,
    py_modules=MODULES,
    description=DESC,
    entry_points={"console_scripts": ["pink=pink:command_line_runner"]},
)
