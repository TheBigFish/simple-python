#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : aysnc_hello_client.py
# @Author: yubo
# @Date  : 2019/2/25
# @Desc  :
import asyncio
class ClientProtocol(asyncio.Protocol):
    def __init__(self, loop):
        self.loop = loop
        self.transport = None

    def connection_made(self, transport):
        self.transport = transport

    def data_received(self, data):
        print(data.decode())

    def connection_lost(self, exc):
        self.loop.stop()

class ClientSession:
    def __init__(self, loop):
        self._loop = loop

    async def get(self, url, host, port):
        transport, protocol = await self._loop.create_connection(
            lambda: ClientProtocol(loop), host, port)

        request = 'GET {} HTTP/1.1\r\nHost: {}\r\n\r\n'.format(url, host)
        transport.write(request.encode())


async def main(loop):
    cs = ClientSession(loop)
    await cs.get('/', 'localhost', 8000)

loop = asyncio.get_event_loop()
loop.run_until_complete(main(loop))
loop.run_forever()