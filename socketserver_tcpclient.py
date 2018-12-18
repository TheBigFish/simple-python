#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : socketserver_tcpclient.py
# @Author: yubo
# @Date  : 2018/12/17
# @Desc  :

from socket import socket, AF_INET, SOCK_STREAM
s = socket(AF_INET, SOCK_STREAM)
s.connect(('localhost', 20000))
s.send(b'Hello')
msg = s.recv(8192)
print msg
