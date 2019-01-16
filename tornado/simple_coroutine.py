#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : asyncore-example-2.py
# @Author: yubo
# @Date  : 2018/12/18
# @Desc  :

import time
import bisect
import functools
from backports_abc import Generator as GeneratorType


class Future(object):
    def __init__(self):
        self._done = False
        self._callbacks = []
        self._result = None

    def _set_done(self):
        self._done = True
        for cb in self._callbacks:
            cb(self)
        self._callbacks = None

    def done(self):
        return self._done

    def add_done_callback(self, fn):
        if self._done:
            fn(self)
        else:
            self._callbacks.append(fn)

    def set_result(self, result):
        self._result = result
        self._set_done()

    def result(self):
        return self._result


class IOLoop(object):
    def __init__(self):
        self._callbacks = []
        self._timers = []
        self._running = False

    @classmethod
    def instance(cls):
        if not hasattr(cls, "_instance"):
            cls._instance = cls()
        return cls._instance

    def add_future(self, future, callback):
        future.add_done_callback(
            lambda future: self.add_callback(functools.partial(callback, future)))

    def add_timeout(self, when, callback):
        bisect.insort(self._timers, (when, callback))

    def call_later(self, delay, callback):
        return self.add_timeout(time.time() + delay, callback)

    def add_callback(self, call_back):
        self._callbacks.append(call_back)

    def start(self):
        self._running = True
        while self._running:

            # 回调任务
            callbacks = self._callbacks
            self._callbacks = []
            for call_back in callbacks:
                call_back()

            # 定时器任务
            while self._timers and self._timers[0][0] < time.time():
                task = self._timers[0][1]
                del self._timers[0]
                task()

    def stop(self):
        self._running = False

    def run_sync(self, func):
        future_cell = [None]

        def run():
            try:
                future_cell[0] = func()
            except Exception:
                pass

            self.add_future(future_cell[0], lambda future: self.stop())

        self.add_callback(run)

        self.start()
        return future_cell[0].result()


class Runner(object):
    def __init__(self, gen, result_future, first_yielded):
        self.gen = gen
        self.result_future = result_future
        self.io_loop = IOLoop.instance()
        self.running = False
        self.future = None

        if self.handle_yield(first_yielded):
            self.run()

    def run(self):
        try:
            self.running = True
            while True:

                try:
                    # 每一个 yield 处看做一个协程，对应一个 Future
                    # 将该协程的结果 send 出去
                    # 这样外层形如  ret = yiled coroutine_func() 能够获取到协程的返回数据
                    value = self.future.result()
                    yielded = self.gen.send(value)
                except (StopIteration, Return) as e:
                    self.result_future.set_result(_value_from_stopiteration(e))
                    self.result_future = None
                    return
                except Exception:
                    return
                if not self.handle_yield(yielded):
                    return
        finally:
            self.running = False

    def handle_yield(self, yielded):
        self.future = yielded
        if not self.future.done():
            self.io_loop.add_future(
                self.future, lambda f: self.run())
            return False
        return True


def sleep(duration):
    f = Future()
    IOLoop.instance().call_later(duration, lambda: f.set_result(None))
    return f


class Return(Exception):
    def __init__(self, value=None):
        super(Return, self).__init__()
        self.value = value
        self.args = (value,)


def _value_from_stopiteration(e):
    try:
        return e.value
    except AttributeError:
        pass
    try:
        return e.args[0]
    except (AttributeError, IndexError):
        return None


def coroutine(func):
    return _make_coroutine_wrapper(func)

# 每个协程都有一个 future， 代表当前协程的运行状态
def _make_coroutine_wrapper(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        future = Future()

        try:
            result = func(*args, **kwargs)
        except (Return, StopIteration) as e:
            result = _value_from_stopiteration(e)
        except Exception:
            return future
        else:
            if isinstance(result, GeneratorType):
                try:
                    yielded = next(result)
                except (StopIteration, Return) as e:
                    future.set_result(_value_from_stopiteration(e))
                except Exception:
                    pass
                else:
                    Runner(result, future, yielded)
                try:
                    return future
                finally:
                    future = None
        future.set_result(result)
        return future
    return wrapper


@coroutine
def routine_ur(url, wait):
    yield sleep(wait)
    print('routine_ur {} took {}s to get!'.format(url, wait))


@coroutine
def routine_url_with_return(url, wait):
    yield sleep(wait)
    print('routine_url_with_return {} took {}s to get!'.format(url, wait))
    raise Return((url, wait))

# 非生成器协程，不会为之生成单独的 Runner()
# coroutine 运行结束后，直接返回一个已经执行结束的 future
@coroutine
def routine_simple():
    print("it is simple routine")

@coroutine
def routine_simple_return():
    print("it is simple routine with return")
    raise Return("value from routine_simple_return")

@coroutine
def routine_main():
    yield routine_simple()

    yield routine_ur("url0", 1)

    ret = yield routine_simple_return()
    print(ret)

    ret = yield routine_url_with_return("url1", 1)
    print(ret)

    ret = yield routine_url_with_return("url2", 2)
    print(ret)


if __name__ == '__main__':
    IOLoop.instance().run_sync(routine_main)
