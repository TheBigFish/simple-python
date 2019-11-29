#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : abc_ABCMeta.py
# @Author: yubo
# @Date  : 2019/11/29
# @Desc  :

import abc

"""
解释器创建类时，会检测 cls.__abstractmethods__ 是否为空，若不为空，则拒绝创建对象

ABCMeta 利用了一点，在类 TestA 创建时，检测是否含有 @abc.abstractmethod 修饰的成员，即设置了 .__isabstractmethod__ 
根据各成员生成一个 __abstractmethods__ 集合，若集合不为空，则无法创建示例，即为抽象类

class ABC(metaclass=ABCMeta):
    pass

ABC 指定元类为 ABCMeta, 故继承 ABC 的类的元类也为 ABCMeta

class TestA(abc.ABC) 等同于
class TestA(metaclass=ABCMeta)
"""
class TestA(abc.ABC):

    a = 1
    b = "a"

    @abc.abstractmethod
    def func1(self):
        pass


class TestB(TestA):
    @abc.abstractmethod
    def func2(self):
        pass


class TestC(TestB):
    @abc.abstractmethod
    def func3(self):
        pass

'''
The notion is correct; the ABCMeta code does not distinguish between a abstractproperty and a abstractmethod.

Both of these decorators add an attribute to the decorated item, .__isabstractmethod__, 
which ABCMeta uses to add an .__abstractmethods__ attribute (a frozenset) to the ABC you defined. 
The object type then guards against creating an instance of any class where any of the names listed 
in .__abstractmethods__ does not have a concrete implementation. No checks are made for functions versus properties there.

To illustrate:

>>> from abc import *
>>> class C:
...     __metaclass__ = ABCMeta
...     @abstractmethod
...     def abstract_method(self): pass
...     @abstractproperty
...     def abstract_property(self): return 'foo'
... 
>>> C.__abstractmethods__
frozenset(['abstract_method', 'abstract_property'])
By creating new overrides for these in a subclass, the ABCMeta class will find fewer methods or properties with 
the . __isabstractmethod__ attribute, thus making the resulting __abstractmethods__ set smaller; once the set is empty 
you can create instances of such a subclass.

These checks are made in the ABCMeta.__new__ constructor and no checks are made to match descriptor types:

cls = super(ABCMeta, mcls).__new__(mcls, name, bases, namespace)
# Compute set of abstract method names
abstracts = set(name
             for name, value in namespace.items()
             if getattr(value, "__isabstractmethod__", False))
for base in bases:
    for name in getattr(base, "__abstractmethods__", set()):
        value = getattr(cls, name, None)
        if getattr(value, "__isabstractmethod__", False):
            abstracts.add(name)
cls.__abstractmethods__ = frozenset(abstracts)
You'd have to create a subclass of ABCMeta that overrides the __new__ method, and check that any abstract method or 
property named on a base class is indeed matched with a non-abstract method or property on cls instead.
'''