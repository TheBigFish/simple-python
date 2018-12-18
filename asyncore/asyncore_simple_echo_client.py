#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : asyncore_simple_echo_client.py.py
# @Author: yubo
# @Date  : 2018/12/17
# @Desc  :

import asyncore, socket


class Client(asyncore.dispatcher_with_send):
    def __init__(self, host, port, message):
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connect((host, port))
        self.out_buffer = message

    def handle_close(self):
        self.close()

    def handle_read(self):
        s = self.recv(1024)
        print 'Received', s
        self.close()


c = Client('127.0.0.1', 8037, 'Hello, world')
asyncore.loop()