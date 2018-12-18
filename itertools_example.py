#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : itertools_example.py
# @Author: yubo
# @Date  : 2018/12/1
# @Desc  :


from itertools import islice

print list(islice('ABCDEFG', 2))
print list(next(islice('ABCDEFG', 2, None)))
from collections import deque

def consume(iterator, n=None):
    """Advance the iterator n-steps ahead. If n is none, consume entirely.

    http://docs.python.org/3.4/library/itertools.html#itertools-recipes
    """
    # Use functions that consume iterators at C speed.
    if n is None:
        # feed the entire iterator into a zero-length deque
        deque(iterator, maxlen=0)
    else:
        # advance to the empty slice starting at position n
        next(islice(iterator, n, n), None)

def take(limit, base):
    return islice(base, limit)

def drop(limit, base):
    return islice(base, limit, None)

a = list(range(10))
b = iter(a)
consume(b, 2)
print list(b)
print list(take(2, iter(range(10))))
print list(drop(2, iter(range(10))))

def izip1(*iterables):
    # izip('ABCD', 'xy') --> Ax By
    iterators = map(iter, iterables)
    while iterators:
        yield tuple(map(next, iterators))

print list(izip1('ABCD', 'xy'))

def takelast(n, iterable):
    "Return iterator to produce last n items from origin"
    return iter(deque(iterable, maxlen=n))
print list(takelast(2, "abcd"))

a = deque("abcd", 2)
print a


print filter(None, (1, 0, 23))


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


def nth(iterable, n, default=None):
    """Returns the nth item or a default value

    http://docs.python.org/3.4/library/itertools.html#itertools-recipes
    """
    return next(islice(iterable, n, None), default)


from functools import partial


head = first = partial(flip(nth), 0)

print head("abc")

print nth("abc", 0)

def drop(limit, base):
    return islice(base, limit, None)

print list(drop(0, "abc"))

tail = rest = partial(drop, 1)

print list(tail("abcd"))