#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : thread_local.py
# @Author: yubo
# @Date  : 2018/11/13
# @Desc  :

import threading

class MyData(threading.local):
    def __init__(self):
        self.x = {}

mydata = MyData()

class Worker(threading.Thread):
    def run(self):
        mydata.x['message'] = self.name
        print mydata.x['message']

w1, w2 = Worker(), Worker()
w1.start(); w2.start(); w1.join(); w2.join()
