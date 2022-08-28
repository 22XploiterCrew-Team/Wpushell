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

import asyncio
from typing import List

from wpushell.io_data import InputData
from wpushell.executor import AsyncioExecutorNoProgress
from wpushell.executor import AsyncioExecutorWithProgress
from wpushell.request import ClientRequest


class Processor:
    """ Processor class, used to process all data and tasks """
    def __init__(self, *args, **kwargs):
        """ Initialize the class """
        self.executor = AsyncioExecutorWithProgress()
        if kwargs.get('no_progressbar'):
            self.executor = AsyncioExecutorNoProgress()

        self.request = ClientRequest(kwargs.get('proxy'), kwargs.get('ssl'))

    async def worker(self, data: InputData):
        """ worker func """
        pass

    async def run(self, data: List[InputData]):
        """ run the processor """
        tasks: list = []
        for item in data:
            tasks.append((self.worker, [item], {}))

        return await self.executor.run(tasks)

    async def close(self) -> None:
        """ close the session """
        await self.request.session.close()
