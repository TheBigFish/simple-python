#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : with_metaclass.py
# @Author: yubo
# @Date  : 2019/11/18
# @Desc  :


def with_metaclass(meta, *bases):
    """Compatible metaclass

    :param meta: the metaclass
    :param *bases: base classes
    """
    print("with_metaclass")
    return meta('temp_class', bases, {})


# Testing:
class TestMeta(type):
    def __new__(cls, name, bases, d):
        d['a'] = 'xyz'
        print("TestMeta.__new__", cls, name, bases, d)

        return type.__new__(cls, name, bases, d)  # ➋


class Foo(object):
    pass


temp = with_metaclass(TestMeta, Foo)
print("type(temp)", type(temp))
print(temp)
print(temp.a)
"""
元类是 type 或者 type 的子类对象
"""


class Bar(temp):  # ➊
    pass


b = Bar()
print("---")

print("Bar ", Bar)
print(Bar.a)
print(Bar.__mro__)
print(b)
"""
➊. 创建Bar类时，调用 with_metaclass，调用了 meta（TestMeta），返回元类对象 
   类名：temp_class 基类： (<class '__main__.Foo'>,) 属性：{'a': 'xyz'}
➋. 该元类对象 temp_class 创建 Bar 类，调用 type.__new__
   类名：Bar 基类：(<class '__main__.temp_class'>,) 属性：{'__module__': '__main__', '__qualname__': 'Bar', 'a': 'xyz'}
   
输出：
with_metaclass
TestMeta.__new__ <class '__main__.TestMeta'> temp_class (<class '__main__.Foo'>,) {'a': 'xyz'}
TestMeta.__new__ <class '__main__.TestMeta'> Bar (<class '__main__.temp_class'>,) {'__module__': '__main__', '__qualname__': 'Bar', 'a': 'xyz'}
---
xyz
(<class '__main__.Bar'>, <class '__main__.temp_class'>, <class '__main__.Foo'>, <class 'object'>)
"""

print("=======")


def with_metaclass(meta, *bases):
    class metaclass(type):
        def __new__(cls, name, this_bases, d):  # ➋
            print(cls, "with_metaclass new is called")
            return meta(name, bases, d)

    return type.__new__(metaclass, 'temp_class', (), {})  # ➊


# Testing:
class TestMeta(type):
    def __new__(cls, name, bases, d):  # ➌
        d['a'] = 'xyz'
        print(cls, "TestMeta new is called")
        return type.__new__(cls, name, bases, d)


print("---")
temp = with_metaclass(TestMeta, Foo)


class Bar(temp): pass


print(Bar.a)
print(Bar.__mro__)

"""
➊. 返回一个中间 类实例 metaclass， 类名：temp_class
➋. 创建类 Bar 时调用 metaclass.new
"""
