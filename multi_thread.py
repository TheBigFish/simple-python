#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : multi_thread.py
# @Author: yubo
# @Date  : 2018/11/14
# @Desc  :


import threading
import datetime
from threading import Timer

# class ThreadClass(threading.Thread):
#     def run(self):
#         now = datetime.datetime.now()
#         print "%s says Hello World at time: %s" % \
#             (self.getName(), now)
#
#
# for i in range(2):
#     t = ThreadClass()
#     t.start()
#
# import urllib2
# import time
#
# hosts = ["http://baidu.com", "http://baidu.com", "http://baidu.com",
# "http://baidu.com", "http://baidu.com"]
#
# start = time.time()
# #grabs urls of hosts and prints first 1024 bytes of page
# for host in hosts:
#     url = urllib2.urlopen(host)
#     print url.read(1024)
#
# print "Elapsed Time: %s" % (time.time() - start)
#
# !/usr/bin/env python
import Queue
import threading
import time


# i = 0
# while True:
#     print("1")
#     try:
#         raise BaseException()
#     except BaseException as ex:
#         continue
#     print("2")

class Test:
    def __init__(self, name):
        self.name = name


task_queue = Queue.Queue()


class ThreadTest(threading.Thread):
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue

    def run(self):
        while not self.queue.empty():
            msg = self.queue.get()
            print(msg.name)
            time.sleep(0.1)
            self.queue.task_done()
        print("thread out")


def main():
    start = time.time()
    # populate queue with data
    for i in range(100):
        task_queue.put(Test("message1"))

    # spawn a pool of threads, and pass them queue instance
    for i in range(5):
        t = ThreadTest(task_queue)
        t.setDaemon(True)
        t.start()

    # wait on the queue until everything has been processed
    task_queue.join()
    print "Elapsed Time: {}".format(time.time() - start)


if __name__ == "__main__":
    main()
