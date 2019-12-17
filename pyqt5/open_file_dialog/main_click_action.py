#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : main_click_action.py.py
# @Author: yubo
# @Date  : 2019/12/13
# @Desc  :

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from main_click import Ui_MainWindow
import os


class MyMainWindow(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super(MyMainWindow, self).setupUi(MainWindow)
        self.pushButton.clicked.connect(lambda : self.show_dialog(MainWindow))
    #
    # def show_dialog(self):
    #     self.text_msg.setPlainText("Hello world!")
    #     #QtWidgets.QMessageBox.information(self.pushButton, "标题", "这是第一个PyQt5 GUI程序")
    #     fileName_choose, filetype = QFileDialog.getOpenFileName(self,
    #                                                             "选取文件",
    #                                                             "E:/",  # 起始路径
    #                                                             "All Files (*);;Text Files (*.txt)")  # 设置文件扩展名过滤,用双分号间隔
    #    print(fileName_choose)

    def show_dialog(self, frame):
        fileName_choose, filetype = QFileDialog.getOpenFileName(frame,'Open file', os.getcwd(), "All Files (*);;Binary Files (*.bin *.hex)")
        self.text_msg.setPlainText(fileName_choose)