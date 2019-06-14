# https://docs.python.org/3.5/library/asyncio-task.html#future


import asyncio
import time


async def slow_operation(future):
    print("enter slow_operation")
    await asyncio.sleep(1)
    future.set_result('Future is done!')

loop = asyncio.get_event_loop()
future = asyncio.Future()
# 由输出可以看到，ensure_future 只是将协程包装成 task
# task 在 event loop 启动后才会执行
asyncio.ensure_future(slow_operation(future))
print("enter event loop")
time.sleep(2.0)
# d等待future 执行完成
loop.run_until_complete(future)
print(future.result())
loop.close()

# 也可以做如下修改
# task = asyncio.ensure_future(slow_operation(future))
# ...
# loop.run_until_complete(task)
# 输出是一样的
