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
        self._eof = False  # 有没有收到 EOF
        self._waiter = None  # 用来等待接收数据的 future

    def connection_made(self, transport):
        self.transport = transport

    def data_received(self, data):
        print(data.decode())

    def eof_received(self):
        self._eof = True
        self._wakeup_waiter()

    def connection_lost(self, exc):
        pass  # 不再调用 self.loop.stop()

    async def wait_for_data(self):
        assert not self._eof
        assert not self._waiter

        self._waiter = self.loop.create_future()
        await self._waiter
        self._waiter = None

    def _wakeup_waiter(self):
        # waiter = self._waiter
        # if waiter:
        #     self._waiter = None
        #     waiter.set_result(None)

        if self._waiter:
            self._waiter.set_result(None)
            self._waiter = None

class ClientSession:
    def __init__(self, loop):
        self._loop = loop

    async def get(self, url, host, port):
        transport, protocol = await self._loop.create_connection(
            lambda: ClientProtocol(self._loop), host, port)

        request = 'GET {} HTTP/1.1\r\nHost: {}\r\n\r\n'.format(url, host)
        transport.write(request.encode())

        # 等待接收数据。
        await protocol.wait_for_data()


async def main(loop):
    cs = ClientSession(loop)
    await cs.get('/', 'localhost', 8000)

loop = asyncio.get_event_loop()
loop.run_until_complete(main(loop))
