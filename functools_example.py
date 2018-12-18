#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : functools_example.py.py
# @Author: yubo
# @Date  : 2018/11/29
# @Desc  :

from functools import partial
import operator


def add3(a, b, c):
    print("{}{}{}".format(a, b, c))
    return a + b + c


p1 = partial(add3, 1)


print p1(2, 3)

p2 =partial(p1, 2)

print p2(3)

def a(*args):
    print args
    pass


def foldl(f, init=None):
    """Return function to fold iterator to scala value
    using passed function as reducer.
    Usage:
    >>> print foldl(_ + _)([0,1,2,3,4])
    10
    >>> print foldl(_ * _, 1)([1,2,3])
    6
    """
    def fold(it):
        args = [f, it]
        if init is not None: args.append(init)
        a(*args)
        return reduce(*args)

    return fold

print foldl(operator.add, 5)([0,1,2,3,4])

def call(f, *args, **kwargs):
    return f(*args, **kwargs)

def flip(f):
    """Return function that will apply arguments in reverse order"""

    # Original function is saved in special attribute
    # in order to optimize operation of "duble flipping",
    # so flip(flip(A)) is A
    # Do not use this approach for underscore callable,
    # see https://github.com/kachayev/fn.py/issues/23
    flipper = getattr(f, "__flipback__", None)
    if flipper is not None:
        return flipper

    def _flipper(a, b):
        return f(b, a)

    setattr(_flipper, "__flipback__", f)
    return _flipper

def foldr(f, init=None):
    """Return function to fold iterator to scala value using
    passed function as reducer in reverse order (consume values
    from iterator from right-to-left).
    Usage:
    >>> print foldr(call, 10)([lambda s: s**2, lambda k: k+10])
    400
    """
    def fold(it):
        args = [flip(f), reversed(it)]
        if init is not None: args.append(init)
        return reduce(*args)

    return fold

print foldr(call, 10)([lambda s: s**2, ])

