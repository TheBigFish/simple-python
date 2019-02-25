#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : timed_rotating_file.py
# @Author: yubo
# @Date  : 2019/2/18
# @Desc  :


# !/usr/bin/env python3

import time
import logging.handlers


logging.basicConfig()

myapp = logging.getLogger('myapp')
myapp.setLevel(logging.INFO)


filehandler = logging.handlers.TimedRotatingFileHandler("time_rotate.log", when='S', interval=1, backupCount=3)

filehandler.suffix = "%Y-%m-%d_%H-%M-%S.log"
myapp.addHandler(filehandler)

while True:
    myapp.info("just")
    time.sleep(0.1)

