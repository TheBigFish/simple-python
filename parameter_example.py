#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : parameter_example.py
# @Author: yubo
# @Date  : 2018/12/8
# @Desc  :

import html


dict_a = {"a": 1, "b": "b1"}
for item in dict_a.items():
    print "%s=%s" % item

a = 1
print "%d"%a

def make_element(name, value, **attrs):
    keyvals = [' %s="%s"' % item for item in attrs.items()]
    attr_str = ''.join(keyvals)
    element = '<{name}{attrs}>{value}</{name}>'.format(
    name=name,
    attrs=attr_str,
    value=value) #html.escape(value))
    return element
# Example
# Creates '<item size="large" quantity="6">Albatross</item>'
print make_element('item', 'Albatross', size='large', quantity=6)
# Creates '<p>&lt;spam&gt;</p>'
make_element('p', '<spam>')


from itertools import chain
numbers = list(range(5))
abc = ["a", "b", "c"]
print list(chain.from_iterable([abc, numbers]))

def imap1(function, *iterables):
    iterables = map(iter, iterables)
    while True:
        args = [next(it) for it in iterables]
        if function is None:
            yield tuple(args)
        else:
            yield function(*args)

print list(imap1(pow, (2,3,10), (5,2,3)))


a = [2, 3]
print(pow(*a))