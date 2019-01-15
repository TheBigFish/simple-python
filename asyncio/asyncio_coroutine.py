#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : asyncio_coroutine.py.py
# @Author: yubo
# @Date  : 2019/1/14
# @Desc  :

import asyncio


async def coroutine():
    print('in coroutine')


event_loop = asyncio.get_event_loop()
try:
    print('starting coroutine')
    coro = coroutine()
    print('entering event loop')
    event_loop.run_until_complete(coro)
finally:
    print('closing event loop')
    event_loop.close()