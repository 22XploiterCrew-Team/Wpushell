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

import colorama
import termcolor

from .io_data import OutputData
from .io_data import OutputDataList

colorama.init()


class Output:
    """ Output class """
    def __init__(self, data: OutputDataList, *args, **kwargs) -> None:
        """ Initialize the class """
        self.data = data

    def put(self) -> str:
        """ put the data """
        pass


class PlainOutput(Output):
    """ PlainOutput class, Used to display the output on the terminal screen """
    def __init__(self, *args, **kwargs) -> None:
        self.is_colored = kwargs.get('colored', True)
        super().__init__(*args, **kwargs)

    def colored(self, value, color):
        """ Output colored """
        if not self.is_colored:
            return value
        return termcolor.colored(value, color)

    def put(self) -> str:
        """ put the data """
        text, total = '', 0
        output_data_list = self.data

        for output in output_data_list:
            text += f'Target: {self.colored(str(output.input_data), "green")}\n'

            for n, result in enumerate(output.results):
                total += 1

                for key in result.fields:
                    name = key.title().replace('_', ' ')
                    if name == 'Data':
                        name = 'Result'
                    value = result.__dict__.get(key)
                    if value is None:
                        value = ''
                    else:
                        text += f'{self.colored(name, "yellow")}: {value}\n'
                text += '\n'
            text += '-' * 22 + '\n'
        text += f'Total data: {total}'

        return text
