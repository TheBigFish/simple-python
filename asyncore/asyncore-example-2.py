#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : asyncore-example-2.py
# @Author: yubo
# @Date  : 2018/12/18
# @Desc  :


import asyncore
import socket
import datetime


class TimeChannel(asyncore.dispatcher):

    def handle_write(self):
        self.send(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    def handle_close(self):
        self.close()


class TimeServer(asyncore.dispatcher):

    def __init__(self, port=37):
        asyncore.dispatcher.__init__(self)
        self.port = port
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.bind(("", port))
        self.listen(5)
        print "listening on port", self.port

    def handle_accept(self):
        channel, _ = self.accept()
        TimeChannel(channel)


server = TimeServer(8037)
print server
asyncore.loop()
