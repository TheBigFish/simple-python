#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : switch_return.py
# @Author: yubo
# @Date  : 2019/1/18
# @Desc  :

import greenlet

def test1(x, y):
    z = gr2.switch(x+y)
    print('test1 ', z)

def test2(u):
    print('test2 ', u)
    gr1.switch(10)

gr1 = greenlet.greenlet(test1)
gr2 = greenlet.greenlet(test2)
print gr1.switch("hello", " world")