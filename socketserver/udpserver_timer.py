#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : udpserver_timer.py
# @Author: yubo
# @Date  : 2018/12/20
# @Desc  :

from SocketServer import BaseRequestHandler, UDPServer
import time

class TimeHandler(BaseRequestHandler):
    def handle(self):
        print('Got connection from', self.client_address)
        # Get message and client socket
        msg, sock = self.request
        resp = time.ctime()
        sock.sendto(resp.encode('ascii'), self.client_address)

if __name__ == '__main__':
    serv = UDPServer(('', 20000), TimeHandler)
    serv.serve_forever()