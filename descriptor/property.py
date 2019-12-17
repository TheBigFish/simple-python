#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : property.py
# @Author: yubo
# @Date  : 2019/12/17
# @Desc  :
class Property(object):
    "Emulate PyProperty_Type() in Objects/descrobject.c"

    def __init__(self, fget=None, fset=None, fdel=None, doc=None):
        self.fget = fget
        self.fset = fset
        self.fdel = fdel
        self.__doc__ = doc

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        if self.fget is None:
            raise AttributeError("unreadable attribute")
        return self.fget(obj)

    def __set__(self, obj, value):
        if self.fset is None:
            raise AttributeError("can't set attribute")
        self.fset(obj, value)

    def __delete__(self, obj):
        if self.fdel is None:
            raise AttributeError("can't delete attribute")
        self.fdel(obj)

    def getter(self, fget):
        return type(self)(fget, self.fset, self.fdel, self.__doc__)

    def setter(self, fset):
        return type(self)(self.fget, fset, self.fdel, self.__doc__)

    def deleter(self, fdel):
        return type(self)(self.fget, self.fset, fdel, self.__doc__)

class C(object):
    def __init__(self):
        self.__x = None
    def getx(self): return self.__x
    def setx(self, value): self.__x = value
    def delx(self): del self.__x
    x = Property(getx, setx, delx, "I'm the 'x' property.")

# c 是类C的实例

c = C()
"""
描述器可以直接这么调用： d.__get__(obj)
然而更常见的情况是描述器在属性访问时被自动调用。举例来说， obj.d 会在 obj 的字典中找 d ,
如果 d 定义了 __get__ 方法，那么 d.__get__(obj) 会依据下面的优先规则被调用。
调用的细节取决于 obj 是一个类还是一个实例。另外，描述器只对于新式对象和新式类才起作用。继承于 object 的类叫做新式类。
对于对象来讲，方法 object.__getattribute__() 把 b.x 变成 type(b).__dict__['x'].__get__(b, type(b)) 。
具体实现是依据这样的优先顺序：资料描述器优先于实例变量，实例变量优先于非资料描述器，__getattr__()方法(如果对象中包含的话)具有最低的优先级。
完整的C语言实现可以在 Objects/object.c 中 PyObject_GenericGetAttr() 查看。
"""

"""
对于类来讲，方法 type.__getattribute__() 把 B.x 变成 B.__dict__['x'].__get__(None, B) 。用Python来描述就是:


def __getattribute__(self, key):
"Emulate type_getattro() in Objects/typeobject.c"
v = object.__getattribute__(self, key)
if hasattr(v, '__get__'):
return v.__get__(None, self)
return v
"""

# x 有 __get__ 属性，c.x ==> x.__get__(c, type(c))
# 变成 fget(c)
# 变成 C.fget(c)， 返回 c.__x
print(c.x)

c.x = 1
print(c.x)