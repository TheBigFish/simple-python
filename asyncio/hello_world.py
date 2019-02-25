#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : hello_world.py
# @Author: yubo
# @Date  : 2019/1/18
# @Desc  :

import asyncio
import time


async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)


async def main():
    print(f"started at {time.strftime('%X')}")

    await say_after(1, 'hello')
    await say_after(2, 'world')

    print(f"finished at {time.strftime('%X')}")


async def main_task():
    task1 = asyncio.create_task(
        say_after(1, 'hello'))

    task2 = asyncio.create_task(
        say_after(2, 'world'))

    print(f"started at {time.strftime('%X')}")

    # Wait until both tasks are completed (should take
    # around 2 seconds.)
    await task1
    await task2

    print(f"finished at {time.strftime('%X')}")


async def nested():
    return 42


async def main_await():
    # Nothing happens if we just call "nested()".
    # A coroutine object is created but not awaited,
    # so it *won't run at all*.
    #nested()

    # Let's do it differently now and await it:
    print(await nested())  # will print "42".


asyncio.run(main())
asyncio.run(main_task())
asyncio.run(main_await())