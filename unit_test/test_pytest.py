#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : test_pytest.py
# @Author: yubo
# @Date  : 2019/12/6
# @Desc  :


import pytest

variable_module = 0


@pytest.fixture(scope='module')
def variable_to_module():
    global variable_module
    variable_module += 1
    return variable_module


def test_variable_module1(variable_to_module):
    assert variable_module == 1


def test_variable_module2(variable_to_module):
    assert variable_module == 1
