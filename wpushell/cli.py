#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Wpushell is a tool used to upload a backdoor shell to a site that uses a WordPress Content Management System with a simple and fast process.
Copyright (C) 2022 RandsX

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>
"""

import os
import sys

from argparse import ArgumentParser
from argparse import RawDescriptionHelpFormatter
from argparse import SUPPRESS

""" setup the argument parser """
def setup_argument_parser() -> ArgumentParser:
    description = '\n' .join([
        'Wpushell is a tool used to upload a backdoor shell to a site that uses a WordPress Content Management System with a simple and fast process.',
        '',
        'In order to use it to upload your backdoor shell, you must first have managed to find the username and password (credentials) used to login to the target site. the input from your target list should be in this format:',
        'https://target.com/ -> [username::password]'
    ])
    parser = ArgumentParser(prog='wpushell', description=description, usage=f'{sys.argv[0]} <target_file> [options]', formatter_class=RawDescriptionHelpFormatter)

    parser.add_argument('target_file', nargs='?', help='list of target sites stored in a file along with the found or valid credentials')
    parser.add_argument('-fstdin', '--target-from-stdin', action='store_true', help=SUPPRESS)

    return parser


""" main entry point """
def main(args: list) -> None:
    arg_parser = setup_argument_parser()
    if len(args) == 0:
        arg_parser.print_usage()
        sys.exit(1)
    args = arg_parser.parse_args()


""" run main entry point """
def run() -> None:
    main(sys.argv[1:])


""" call """
if __name__ == '__main__':
    run()
