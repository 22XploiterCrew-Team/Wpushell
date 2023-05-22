#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Wpushell is a tool used to upload a backdoor shell to a site that uses a WordPress Content Management System with a simple and fast process.
Copyright (C) 2022 RandsX

This program is free software: you can redistribute it and/or modify  it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>

Install packages as defined in this file into the Python environment.
"""
from setuptools import setup, find_packages

# The version of this tool is based on the following steps:
# https://packaging.python.org/guides/single-sourcing-package-version/
VERSION = {}
with open("./wpushell/__version__.py") as file:
    exec(file.read(), VERSION)

setup(
    name="wpushell",
    author="RandsX",
    author_email="andrevirdiaz@gmail.com",
    url="https://github.com/22XploiterCrew-Team/Wpushell",
    description="Wpushell is a tool used to upload a backdoor shell to a site that uses a WordPress Content Management System with a simple and fast process.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    version=VERSION.get("__version__", "0.0.0"),
    packages=find_packages(where="."),
    install_requires=open("requirements.txt").read().splitlines(),
    entry_points={
        "console_scripts": [
            "wpushell=wpushell.__init__:run",
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3.0",
        "Topic :: Security",
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
    ],
)