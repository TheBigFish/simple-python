#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : echo_stream_request_server.py
# @Author: yubo
# @Date  : 2018/12/19
# @Desc  :

import SocketServer


class MyTCPServer(SocketServer.StreamRequestHandler):
    def handle (self):
        while 1:
            peer = self.connection.getpeername()[0]
            line = self.rfile.readline()
            print "%s wrote: %s" % (peer, line)
            sck = self.connection.getsockname()[0]
            self.wfile.write("%s: %d bytes successfully received." % (sck, len(line)))


# Create SocketServer object
serv = SocketServer.TCPServer(("", 50008), MyTCPServer)

# Activate the server to handle clients
serv.serve_forever()