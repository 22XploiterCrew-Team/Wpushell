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

from typing import List


class InputData:
    """ InputData class, which is used to receive or store the given data """
    def __init__(self, data) -> None:
        """ Initialize the class """
        self.data = data

    def __str__(self) -> str:
        """ Return string representation of InpuData class """
        return str(self.data)

    def __repr__(self) -> str:
        """ Return string representation of InputData class """
        return str(self.data)


class OutputData:
    """ OutputData class, used to display all executed output """
    def __init__(self, data: str, status: int, error: str) -> None:
        """ Initialize the class """
        self.data = data
        self.code = status
        self.error = error

    @property
    def fields(self):
        """ Property fields to set the field of output """
        fields = list(self.__dict__.keys())
        return fields

    def __str__(self) -> str:
        """ Return string representation of OutputData class """
        error, result = '', ''
        if self.error:
            error = f' (error: {str(self.error)}'

        for field in self.fields:
            field_name = field.title().replace('_',' ')
            field_value = self.__dict__.get(field)
            if field_value:
                result += f'{field_name}: {str(field_value)}\n'
        result += f'{error}'

        return result


class OutputDataList:
    """ OutputDataList class, used to display a list of output data """
    def __init__(self, data: InputData, results: List[OutputData]) -> None:
        """ Initialize the class """
        self.input_data = data
        self.results = results

    def __repr__(self) -> str:
        """ Return string representation of OutputDataList class """
        return f'Target {self.input_data}:\n' + '----\n' . join(map(str, self.results))
