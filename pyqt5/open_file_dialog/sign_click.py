#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : sign_click.py
# @Author: yubo
# @Date  : 2019/12/13
# @Desc  :
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication , QMainWindow
from main_click import *
from main_click_action import MyMainWindow


if __name__ == '__main__':
    '''
    主函数
    '''
    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    ui = MyMainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
