#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : reveal_access.py
# @Author: yubo
# @Date  : 2019/12/17
# @Desc  :

class RevealAccess(object):
    """A data descriptor that sets and returns values
       normally and prints a message logging their access.
    """

    def __init__(self, initval=None, name='var'):
        self.val = initval
        self.name = name

    def __get__(self, obj, objtype):
        print('Retrieving', self.name)
        return self.val

    def __set__(self, obj, val):
        print('Updating' , self.name)
        self.val = val

class MyClass(object):
    x = RevealAccess(10, 'var "x"')
    y = 5

m = MyClass()
m.x
m.x = 20
m.x
m.y
