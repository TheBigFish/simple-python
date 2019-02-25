#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : dd.py
# @Author: yubo
# @Date  : 2019/1/21
# @Desc  :

import time
import logging
from tornado.gen import coroutine
from tornado.httpclient import AsyncHTTPClient
from tornado.ioloop import IOLoop
from tornado.web import Application, RequestHandler


class MainHandler(RequestHandler):

    @coroutine
    def get(self):
        client = AsyncHTTPClient()
        urls = ['http://www.jd.com'] * 5
        start = time.time()
        yield [client.fetch(url) for url in urls]
        print(time.time() - start)


def make_app():
    return Application([(r"/", MainHandler), ])


if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    IOLoop.current().start()