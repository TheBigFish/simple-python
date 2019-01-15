#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : asyncio_create_task.py.py
# @Author: yubo
# @Date  : 2019/1/14
# @Desc  :

import asyncio

@asyncio.coroutine
def task_func():
    print('in task_func')
    return 'the result'

@asyncio.coroutine
def main(loop):
    print('creating task')
    task = loop.create_task(task_func())
    print('waiting for {!r}'.format(task))
    return_value = yield from task
    print('task completed {!r}'.format(task))
    print('return value: {!r}'.format(return_value))


event_loop = asyncio.get_event_loop()
try:
    event_loop.run_until_complete(main(event_loop))
finally:
    event_loop.close()