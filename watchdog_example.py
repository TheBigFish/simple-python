#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : watchdog_example.py
# @Author: yubo
# @Date  : 2018/12/3
# @Desc  :
#
import sys
import time
import json
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler



class MyHandler(PatternMatchingEventHandler):
    patterns = ["abc.json"]

    def process(self, event):
        """
        event.event_type
            'modified' | 'created' | 'moved' | 'deleted'
        event.is_directory
            True | False
        event.src_path
            path/to/observed/file
        """

        with open(event.src_path, 'r') as load_f:
            load_dict = json.load(load_f)
            print(load_dict)

    def on_modified(self, event):
        self.process(event)

    def on_created(self, event):
        self.process(event)


if __name__ == '__main__':
    observer = Observer()
    observer.schedule(MyHandler(), ".")


    try:
        observer.start()
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()

#
# import time
# from watchdog.observers import Observer
# from watchdog.events import FileSystemEventHandler
#
#
# class Watcher:
#     DIRECTORY_TO_WATCH = "."
#
#     def __init__(self):
#         self.observer = Observer()
#
#     def run(self):
#         event_handler = Handler()
#         self.observer.schedule(event_handler, self.DIRECTORY_TO_WATCH, recursive=True)
#         self.observer.start()
#         try:
#             while True:
#                 time.sleep(5)
#         except:
#             self.observer.stop()
#             print "Error"
#
#         self.observer.join()
#
#
# class Handler(FileSystemEventHandler):
#
#     @staticmethod
#     def on_any_event(event):
#         if event.is_directory:
#             return None
#
#         elif event.event_type == 'created':
#             # Take any action here when a file is first created.
#             print "Received created event - %s." % event.src_path
#
#         elif event.event_type == 'modified':
#             # Taken any action here when a file is modified.
#             print "Received modified event - %s." % event.src_path
#
#
# if __name__ == '__main__':
#     w = Watcher()
#     w.run()