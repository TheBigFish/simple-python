#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : exception_example.py
# @Author: yubo
# @Date  : 2018/12/3
# @Desc  :
print "abc", "123", "456"

print 'get_%s' % "abc", "123", "456"

class ROSException(Exception):
    """
    Base exception class for ROS clients
    """
    pass

try:
    raise ROSException("error")
except ROSException as ex:
    print ex


class RobotConfigInner(object):
    def __init__(self):
        #self._model = None
        self.run_model = "idol"

    @property
    def run_model(self):
        return self._model

    @run_model.setter
    def run_model(self, value):
        self._model = value + "123"

a = RobotConfigInner()
print a.run_model

# class Text(object):
#     def __init__(self, font, size=12):
#         self.size = size
#         self.font = font
#         self.dirty = False
#
#     def draw(self):
#         print "Draw: ", self.size, self.font, self.dirty
#
#     @property
#     def size(self):
#         return self._size
#
#     @size.setter
#     def size(self, px):
#         if self._size != px:
#             self._size = px
#             self.dirty=True

if __name__  == "__main__":
    # t = Text("arial", 6)
    # t.draw()
    # t.size = 8
    # t.draw()

    a = {"a": 1, "c": 3}
    print a.items()
    c = dict(list(a.items()) + [("b", 2)])
    print c