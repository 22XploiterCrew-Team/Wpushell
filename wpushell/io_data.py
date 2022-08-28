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
