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

    def connection_made(self, transport):
        request = 'GET / HTTP/1.1\r\nHost: localhost\r\n\r\n'
        transport.write(request.encode())

    def data_received(self, data):
        print(data.decode())

    def connection_lost(self, exc):
        self.loop.stop()


async def main(loop):
    await loop.create_connection(
        lambda: ClientProtocol(loop), 'localhost', 8000)

loop = asyncio.get_event_loop()
loop.run_until_complete(main(loop))
loop.run_forever()