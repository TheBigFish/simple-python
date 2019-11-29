#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : metaclass_2.py
# @Author: yubo
# @Date  : 2019/11/18
# @Desc  :


class SimpleMetaClass(type):
    def __new__(cls, *args, **kwargs):
        print("creating class Earth...")
        return super(SimpleMetaClass, cls).__new__(cls, *args, **kwargs)

    def __init__(self, *args, **kwargs):
        print("you have create a class instance by metaclass")
        super(SimpleMetaClass, self).__init__(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        print("__call__ in metaclass has been invoked...", "the args:", args, kwargs)
        return super(SimpleMetaClass, self).__call__(*args, **kwargs)


class Earth(metaclass=SimpleMetaClass):
    def __new__(cls, g, R=65535):
        print("creating instance using __new__")
        cls.g = g
        cls.R = R
        return super(Earth, cls).__new__(cls)

    def __init__(self, g, R=65535):
        print("initializing instance in __init__")
        print("gravity on Earth is:%f" % self.g)

    def __call__(self):
        print(self.g)

    def sayHello(self):
        print("hello earth,your gravity is:%f" % self.g)


if __name__ == "__main__":
    """earth = Earth(9.8, R=65535)
    1、调用 创建 Earth 的类的__call__ 方法，即 SimpleMetaClass.__call__
        1、调用 type.__call__
        2、调用 Earth.__new__
        3、type.__call__ 返回
        SimpleMetaClass.__call__ 返回 Earth 的一个实例
    2、调用 Earth.__init__ 
    """
    earth = Earth(9.8, R=65535)
    """
    earth() 调用创建 earth 的类的__call__方法，即 Earth.__call__
    """
    earth()
    earth.sayHello()

"""
creating class Earth...
you have create a class instance by metaclass
__call__ in metaclass has been invoked... the args: (9.8,) {'R': 65535}
creating instance using __new__
initializing instance in __init__
gravity on Earth is:9.800000
9.8
hello earth,your gravity is:9.800000
"""

"""
1. 首先python创建SimpleMetaClass类，这个SimpleMetaClass是元类，应该是由type创建的。
2. 当创建Earth这个类时，找到了它类中有__metaclass__属性，于是，采用SimpleClass来创建这个类
3. 创建Earth类时，解释器会把类名，父类元祖，类的属性三个参数传给SimpleMetaClass(传给 type 也是这几个参数)
4. SimpleMetaClass 根据 clazzName,(parent2,parent1,..),{‘attribute’:….,’method’:”}在自己__new__方法中创建出这个Earth实例【打印出①】，
   然后调用自己的__init__方法初始化类的参数【打印出②】。这时，这个Earth类作为metaclass的一个实例就被创建好了。
5. 接下来通过 earth = Earth(9.8,R=65535) 创建一个Earth对象实例earth。这一步实际上是调用 Earth这个类对象的__call__（SimpleMetaClass::__call__）
   方法来创建一个Earth的实例。【打印出③，我们还能看到调用__call__的参数】。
6. 而创建earth实例的方法__new__(Earth::__new__),和__init__(Earth:__init__),将会在Earth实例中的__call__（SimpleMetaClass::__call__）
   当中先后得以执行【先后打印出④⑤⑥】执行完成Earth实例earth对象被返回。
7.8. 容易理解

"""