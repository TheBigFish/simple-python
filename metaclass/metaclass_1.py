#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : metaclass_1.py
# @Author: yubo
# @Date  : 2019/11/18
# @Desc  :

class_definition = type('class_name', (), {})   # ➊

print(type(class_definition))


class Meta(type):   # ➋
    def __new__(cls, name, bases, d):
        print("call Meta __new__")
        d["a"] = "a"
        return super(Meta, cls).__new__(cls, name, bases, d)

    def __init__(self, *args, **kwargs):
        print("call Meta __init__")
        super(Meta, self).__init__(*args, **kwargs)


print(type(class_definition))   # ➌
print(class_definition)     # ➍
print(Meta)
print(type(Meta))

meta_definition = Meta('meta', (), {})  # ➎
print(meta_definition)
print(type(meta_definition))        # ➏


class MetaNormal0(Meta):
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
    """
    pass


class MetaNormal2(meta_definition):
    '''
    为什么这里可以用 meta_definition 定义元类？而不需要 metaclass 关键字？
    '''
    pass


print(type(MetaNormal2))
print(MetaNormal2.a)

# print(MetaNormal0.__mro__)
# print(MetaNormal1.__mro__)
"""
➊ ➋ type 类或者继承自 type 的类称为元类
➌ class_definition 是type创建，所以 type(class_definition) 为 <class 'type'>
➍ class_definition 是一个类
➎ meta_definition 由元类 Meta 创建，创建 meta_definition 时，
    1. 先调用 Meta 的 __new__, 
    2. 再调用 Meta 的 __init__，
  这样，meta_definition（类） 作为 元类 Meta 的一个实例就被创建好
➏ meta_definition 的元类为 Meta
"""

""" 输出：
<class 'type'>
<class '__main__.class_name'>
<class 'type'>
call Meta __new__
call Meta __init__
<class '__main__.meta'>
<class '__main__.Meta'>
"""