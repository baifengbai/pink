#!/usr/bin/env python
# coding=utf-8

from setuptools import setup

NAME = "pink"
VERSION = "0.1.0"
URL = "https://github.com/chenjiandongx/pink"
AUTHOR = "chenjiandongx"
AUTHOR_EMAIL = "chenjiandongx@qq.com"
LICENSE = "MIT"
REQUIRES = ["black", "glob2", "delegator.py"]
MODULES = ["pink"]
DESC = "reformatted code via the command line."


setup(
    author=AUTHOR,
    author_email=AUTHOR,
    name=NAME,
    version=VERSION,
    license=LICENSE,
    install_requires=REQUIRES,
    url=URL,
    py_modules=MODULES,
    description=DESC,
    entry_points={"console_scripts": ["pink=pink:command_line_runner"]},
)
