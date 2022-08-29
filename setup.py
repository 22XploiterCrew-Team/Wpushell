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
"""

from wpushell.__version__ import __version__
from setuptools import setup
from setuptools import find_packages

with open('requirements.txt') as file:
    requirements = file.read().splitlines()

setup(
    name='wpushell',
    version=__version__,
    description='Wpushell is a tool used to upload a backdoor shell to a site that uses a WordPress Content Management System with a simple and fast process.',
    author='RandsX',
    author_email='andrewvirdiaz@gmail.com',
    keywords='wordpress, upload, backdoor, shell',
    entry_points={
        'console_scripts': [
            'wpushell = wpushell.__init__:run'
        ]
    },
    packages=find_packages(),
    install_requires=requirements,
    include_package_data=True
)
