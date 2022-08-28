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

from tqdm import tqdm
from typing import Any
from typing import List
from typing import Tuple
from typing import Callable
from typing import Iterable

QueryDraft = Tuple[Callable, List, List]

class AsyncExecutor:
    """ AsyncExecutor class, BASE CLASS """
    def __init__(self, *args, **kwargs) -> None:
        """ Initialize the class """
        pass

    async def run(self, tasks: Iterable[QueryDraft]):
        """ run tasks """
        return await self._run(tasks)

    async def _run(self, tasks: Iterable[QueryDraft]):
        """ run tasks """
        await asyncio.sleep(0)


class AsyncioExecutorNoProgress(AsyncExecutor):
    """ AsyncioExecutorNoProgress class """
    def __init__(self, *args, **kwargs) -> None:
        """ Initialize the class """
        super().__init__(*args, **kwargs)

    async def _run(self, tasks: Iterable[QueryDraft]):
        """ run tasks """
        futures: list = []
        for func, args, kwargs in tasks:
            futures.append(func(*args, **kwargs))

        return await asyncio.gather(*futures)


class AsyncioExecutorWithProgress(AsyncExecutor):
    """ AsyncioExecutorWithProgress class """
    def __init__(self, *args, **kwargs) -> None:
        """ Initialize the class """
        super().__init__(*args, **kwargs)

    async def _run(self, tasks: Iterable[QueryDraft]):
        """ run tasks """
        futures: list = []
        for func, args, kwargs in tasks:
            futures.append(func(*args, **kwargs))

        result: list = []
        for task in tqdm(
            asyncio.as_completed(futures),
            total=len(futures),
            desc='Processing'
        ):
            result.append(await task)

        return result
