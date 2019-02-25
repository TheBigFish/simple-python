#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : remove_comment.py
# @Author: yubo
# @Date  : 2019/2/18
# @Desc  :

import os
import re
import sys
import shutil
import compileall


def delete_Notes(py_file):
    # 原始文件只读打开，处理文件追加打开
    _tmp_sr_file = open(py_file, "rb").readlines()
    _tmp_de_file = open("%s.swp" % py_file, "ab")
    _skip_status = 0
    _now_line = 0
    _multi_count = 0
    # 循环处理
    for line in _tmp_sr_file:
        # 跳过前10行，因为我的开头注释有10行
        if _now_line > 10:
            # 获取开头一位和三位
            try:
                _single_row_notes = line.strip()[0]
            except:
                _single_row_notes = ""
            try:
                _multi_row_notes = line.strip()[0:3]
            except:
                _multi_row_notes = ""
            # 获取行是否为注释
            if _single_row_notes == "#":
                _skip_status = 1
            elif _multi_row_notes == "'''":
                if _multi_count == 0:
                    _skip_status = 1
                    _multi_count = 1
                else:
                    _skip_status = 1
                    _multi_count = 0
            elif _multi_count == 1:
                _skip_status = 1
            else:
                _skip_status = 0
        else:
            _skip_status = 0
        # 判断是否跳过写入
        if _skip_status == 0:
            _tmp_de_file.write(line)
        _now_line += 1
    _tmp_de_file.close()
    # 处理完毕将临时文件处理为原始文件
    shutil.move("%s.swp" % py_file, py_file)


def main():
    _get_src_path = sys.argv[1]
    _get_dec_path = sys.argv[2]
    if os.path.exists(_get_src_path):
        # 拷贝原始文件夹
        shutil.copytree(_get_src_path, _get_dec_path)
        # 删除原始文件中的注释
        find_py_file = re.compile(r"^.*\.py$")
        find_walk = os.walk(_get_dec_path)
        for path, dirs, files in find_walk:
            for f in files:
                if find_py_file.search(f):
                    delete_Notes("%s/%s" % (path, f))
        # 编译成字节码
        compileall.compile_dir(_get_dec_path)
    else:
        print "Path Error!"


if __name__ == "__main__":
    main()
