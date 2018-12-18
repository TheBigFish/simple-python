#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : random_shits.py
# @Author: yubo
# @Date  : 2018/12/13
# @Desc  :
import random
from itertools import cycle
import time
import SocketServer

print time.time()

rand_number = 81098
seed = ["幸运数字：{}".format(rand_number)]
time = ["时间：2018/12/14 周五19:30"]
local = ["地点：谷山体育公园"]

random.seed(rand_number)
captains = ['心力(队长)', '博(队长)', '李建强(队长)']
others = ["长腿", "老王", "操", "巨", "顿哥", "艾", "易兵", "大空", "徐", "李江", "周任强",
          "响哥",
          "武松", "肖宇", "唐医生", "俊", "容虹斌", "冯志军", "吴波",
          "严敏",
          "刘博"
          ]
random.shuffle(captains)
random.shuffle(others)
main = captains + others
captains = None
others = None
group_a = ["曼联红"]
group_b = ["巴西黄"]
group_c = ["阿根廷蓝白"]

for group in cycle((group_a, group_b, group_c)):
    if not len(main):
        break
    group.append(main.pop(0))

for group in (group_a, group_b, group_c):
    for i in group:
        print i.decode("utf8"),
    print ""
