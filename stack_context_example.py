#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : stack_context_example.py
# @Author: yubo
# @Date  : 2018/12/21
# @Desc  :

#
# class MyIOLoop:
#     def __init__(self):
#         self._callbacks = []
#
#     @classmethod
#     def instance(cls):
#         if not hasattr(cls, "_instance"):
#             cls._instance = cls()
#         return cls._instance
#
#     def add_callback(self, call_back):
#         self._callbacks.append(call_back)
#
#     def start(self):
#         callbacks = self._callbacks
#         self._callbacks = []
#         for call_back in callbacks:
#             call_back()
#
#
# my_io_loop = MyIOLoop.instance()
# times = 0
#
#
# def call_func():
#     print 'run call_func'
#     raise ValueError('except in call_func')
#
#
# def async_task():
#     global times
#     times += 1
#     print 'run async task {}'.format(times)
#     my_io_loop.add_callback(call_back=call_func)
#
#
# def main():
#     try:
#         async_task()
#     except Exception as e:
#         print 'main exception {}'.format(e)
#         print 'end'
#
#
# if __name__ == '__main__':
#     main()
#     my_io_loop.start()
#
import functools


class MyIOLoop:
    def __init__(self):
        self._callbacks = []

    @classmethod
    def instance(cls):
        if not hasattr(cls, "_instance"):
            cls._instance = cls()
        return cls._instance

    def add_callback(self, call_back):
        self._callbacks.append(call_back)

    def start(self):
        callbacks = self._callbacks
        self._callbacks = []
        for call_back in callbacks:
            call_back()


my_io_loop = MyIOLoop.instance()
times = 0


def call_func():
    print 'run call_func'
    raise ValueError('except in call_func')


def wrapper(func):
    try:
        func()
    except Exception as e:
        print 'wrapper exception {}'.format(e)


def async_task():
    global times
    times += 1
    print 'run async task {}'.format(times)
    my_io_loop.add_callback(call_back=functools.partial(wrapper, call_func))


def main():
    try:
        async_task()
    except Exception as e:
        print 'main exception {}'.format(e)
        print 'end'


if __name__ == '__main__':
    main()
    my_io_loop.start()
