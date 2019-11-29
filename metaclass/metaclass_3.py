#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : metaclass_3.py
# @Author: yubo
# @Date  : 2019/11/20
# @Desc  :


class M(type):
    def __new__(cls, name, bases, d):
        print(cls, name, bases)
        return super(M, cls).__new__(cls, name, bases, d)


class A(metaclass=M):
    pass


class B(A):
    def __new__(cls, *args, **kwargs):
        print("B.new")
        return super(B, cls).__new__(cls, *args, **kwargs)

    pass


class C(B):
    def __new__(cls, *args, **kwargs):
        print("C.new")
        return super(C, cls).__new__(cls, *args, **kwargs)

    pass


print(type(A))
print(type(B))
print(type(C))
print(isinstance(C, B))  # False
print(isinstance(C, M))  # True
c = C()
"""
创建类的类为元类

类 C 继承 B, 类 B 继承 A, 类 A 的元类为 M, C B A 的元类都是 M
"""
"""
<class '__main__.M'> A ()
<class '__main__.M'> B (<class '__main__.A'>,)
<class '__main__.M'> C (<class '__main__.B'>,)
<class '__main__.M'>
<class '__main__.M'>
<class '__main__.M'>
False
True
C.new
B.new
"""


class M(type):
    def __new__(cls, name, bases, d):
        print(cls, name, bases)
        return super(M, cls).__new__(cls, name, bases, d)


meta = type.__new__(M, "temple", (), {})


class A(meta):
    pass


print(type(meta))
print(type(A))

"""
<class '__main__.M'> A (<class '__main__.temple'>,)
<class '__main__.M'>
<class '__main__.M'>
"""


def with_metaclass(meta, *bases):
    class metaclass(type):
        def __new__(cls, name, this_bases, d):
            print(cls, "new is called")
            # Metaclass.__new__ returns the Class object
            return meta(name, bases, d)
            # 等同于
            #return type.__new__(meta, name, bases, d)

    return type.__new__(metaclass, 'temp_class', (), {})
    # 此处 metaclass 指定该临时类由 metaclass 生成)，即元类为 metaclass


# Testing:
class TestMeta(type):
    def __new__(cls, name, bases, d):
        d['a'] = 'xyz'
        print(cls, "new is called")
        return type.__new__(cls, name, bases, d)


class Foo(object): pass


temp = with_metaclass(TestMeta, Foo)


class Bar(temp): pass
print(type(Bar))

#print(Bar.a)
print(Bar.__mro__)

"""
<class '__main__.with_metaclass.<locals>.metaclass'> new is called
<class '__main__.TestMeta'> new is called
xyz
(<class '__main__.Bar'>, <class '__main__.Foo'>, <class 'object'>)
"""


class Meta(type):
    def __new__(mcs, name, bases, dct):
        print(mcs)
        x = super().__new__(mcs, name, bases, dct)
        x.attr = 100
        print(mcs, name, bases, dct)
        return x

    def __init__(cls, name, bases, dct):
        print(cls, name, bases, dct)
        super(Meta, cls).__init__(name, bases, dct)


class Foo(metaclass=Meta):
    pass


print(Foo.attr)
