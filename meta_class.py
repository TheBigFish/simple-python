#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : meta_class.py
# @Author: yubo
# @Date  : 2018/11/28
# @Desc  :

#import operator
class itemgetter:
    """
    Return a callable object that fetches the given item(s) from its operand.
    After f = itemgetter(2), the call f(r) returns r[2].
    After g = itemgetter(2, 5, 3), the call g(r) returns (r[2], r[5], r[3])
    """
    __slots__ = ('_items', '_call')

    def __init__(self, item, *items):
        if not items:
            self._items = (item,)
            def func(obj):
                return obj[item]
            self._call = func
        else:
            self._items = items = (item,) + items
            def func(obj):
                return tuple(obj[i] for i in items)
            self._call = func

    def __call__(self, obj):
        return self._call(obj)

    def __repr__(self):
        return '%s.%s(%s)' % (self.__class__.__module__,
                              self.__class__.__name__,
                              ', '.join(map(repr, self._items)))

    def __reduce__(self):
        return self.__class__, self._items
cc_name = itemgetter(1, 0)

print repr(cc_name)

class Singleton(object):
    abc = 1
    def __new__(cls):
        # 关键在于这，每一次实例化的时候，我们都只会返回这同一个instance对象
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        self.index = 0

obj1 = Singleton()
obj2 = Singleton()

print Singleton.__dict__
obj1.attr1 = 'value1'
print id(Singleton.abc)
print id(obj1.abc)
print obj1.attr1, obj2.attr1
print obj1 is obj2


class Man(object):
    gender = 'male'
    item = ["1"]

    def __init__(self, name):
        self.name = name


a = Man('lily')
b = Man('tom')

a.gender = "female"
b.item.append("2")
print a.item
print b.item
print Man.item
print a.gender
print Man.gender
print b.gender
b.item = ["3"]
print a.item
print b.item
print Man.item
print a.__dict__
print b.__dict__
print Man.__dict__


def wrapper(func):
    def wrapper_in(*args, **kwargs):
        # args是一个数组，kwargs一个字典
        print("%s is running" % func.__name__)
        return func(*args, **kwargs)
    return wrapper_in

@wrapper
def func(parameter1, parameter2, key1=1):
    print("call func with {} {} {}".format(parameter1, parameter2, key1))


func("haha", None, key1=2)

def log(level):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if level == "warn":
                print("%s with warn is running" % func.__name__)
            elif level == "info":
                print("%s with info is running" % func.__name__)
            return func(*args, **kwargs)
        return wrapper

    return decorator


@log("warn")
def foo(*args, **kwargs):
    print("args {}, kwargs{}".format(args, kwargs))

foo(1, 2, a = 3)


def pecorate(func):
   def wrapper(*args, **kwargs):
       return "<p>{0}</p>".format(func(*args, **kwargs))
   return wrapper

class Person(object):
    def __init__(self):
        self.name = "John"
        self.family = "Doe"

    @pecorate
    def get_fullname(self):
        return self.name+" "+self.family

my_person = Person()

print my_person.get_fullname()

class EntryExit(object):

    def __init__(self, f):
        self.f = f

    def __call__(self):
        print "Entering", self.f.__name__
        self.f()
        print "Exited", self.f.__name__

@EntryExit
def func1():
    print "inside func1()"

@EntryExit
def func2():
    print "inside func2()"

def func3():
    pass

print type(EntryExit(None))
print type(func1)
print type(EntryExit)
print type(func3)
func1()
func2()
# myfunc1 = logit()(myfunc1)
# myfunc1()


register_handles = []


def route(url):
    global register_handles

    def register(handler):
        register_handles.append((".*$", [(url, handler)]))
        return handler

    return register

@route("/index")
class Index():
    def get(self, *args, **kwargs):
        print("hi")

@route("/main")
class Main():
    def get(self, *args, **kwargs):
        print("hi")

print (register_handles)
print(type(Index))


from functools import wraps

def logged(func):
    @wraps(func)
    def with_logging(*args, **kwargs):
        '''wrap function'''
        return func(*args, **kwargs)
    return with_logging

# 函数
@logged
def f(x):
   """return x*x"""
   return x * x
#f = logged(f)

print f.__name__
print f.__doc__
print f(2)
