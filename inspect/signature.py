#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : signature.py
# @Author: yubo
# @Date  : 2019/12/11
# @Desc  :
from inspect import signature


# * means all arguments afterwards are keyword-only
def test_fun(x, y=42, *, z=None):
    pass


sig = signature(test_fun)
value = sig.bind_partial(1, 2, z=3)
print(value.arguments)
# OrderedDict([('x', 1), ('y', 2), ('z', 3)])

value = sig.bind_partial(z=2)
print(value.arguments)
# OrderedDict([('z', 2)])


value = sig.bind(z=2)
# TypeError: missing a required argument: 'x'
print(value.arguments)

# bind_partial 是对参数的部分绑定
# bind 必须全部符合参数要求

