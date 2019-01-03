#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : vector2d.py
# @Author: yubo
# @Date  : 2018/12/26
# @Desc  :

from array import array
import math

class Vector2d:
    typecode = 'd'

    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def __iter__(self):
        return (i for i in (self.x, self.y))

v = Vector2d(1, 2)
x, y = v
print x, y

def func(*p):
    print p

a = (i for i in (1, 2, 3))
func(*a)

def gen_fn():
    result = yield 1
    print('result of yield: {}'.format(result))
    result2 = yield 2
    print('result of 2nd yield: {}'.format(result2))
    return