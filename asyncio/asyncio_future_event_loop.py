# asyncio_future_event_loop.py
import asyncio


def mark_done(future, result):
    print('setting future result to {!r}'.format(result))
    future.set_result(result)


event_loop = asyncio.get_event_loop()
try:
    all_done = asyncio.Future()

    print('scheduling mark_done')
    # call_soon 注册的是普通回调函数，将在事件循环启动时调用
    event_loop.call_soon(mark_done, all_done, 'the result')

    print('entering event loop')
    # 等待 future 结束
    result = event_loop.run_until_complete(all_done)
    print('returned result: {!r}'.format(result))
finally:
    print('closing event loop')
    event_loop.close()

print('future result: {!r}'.format(all_done.result()))