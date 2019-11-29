#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : metaclass_0.py
# @Author: yubo
# @Date  : 2019/11/18
# @Desc  :


class Meta(type):
    """
    自定义元类
    """
    def __new__(cls, name, bases, d):
        """
        使用自定义元类，最终都是要调用 type 生成类实例
        return super(Meta, cls).__new__(cls, name, bases, d)
        等同于
        type.__new__(cls, name, bases, d)
        """
        print("call Meta __new__")
        d["a"] = "a"
        return super(Meta, cls).__new__(cls, name, bases, d)

    def __init__(self, *args, **kwargs):
        print("call Meta __init__")
        super(Meta, self).__init__(*args, **kwargs)


class MetaNormal0(object):
    """
    我们写下如下代码时：

    class Foo(object):
        pass
    实际上，解释器将其解释为：

    Foo = type('Foo', (object,), {})
    """
    pass


class MetaNormal1(metaclass=Meta):
    """
    如果定义了元类
    class MyMetaType(type):
          pass
    class Foo(metaclass=MyMetaType):
        pass

    解释器解释到class Foo(...)的时候，就会转换为：
    Foo = MyMetaType('Foo', (object,), {})

    此时调用 MyMetaType.__new__, MyMetaType.__init__, 生成类MyMetaType 的实例化对象：Foo
    """
    pass


"""
MetaNormal1 的元类是 Meta, 父类是 object
"""
print(type(MetaNormal1))
print(MetaNormal1.__mro__)
"""
call Meta __new__
call Meta __init__
<class '__main__.Meta'>
(<class '__main__.MetaNormal1'>, <class 'object'>)
"""