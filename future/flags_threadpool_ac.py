#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : flags_threadpool_ac.py.py
# @Author: yubo
# @Date  : 2019/1/8
# @Desc  :

from concurrent import futures
from flags import save_flag, get_flag, show, main

def download_one(cc):
    image = get_flag(cc)
    show(cc)
    save_flag(image, cc.lower() + '.gif')
    return cc

def download_many(cc_list):
    cc_list = cc_list[:5]
    with futures.ThreadPoolExecutor(max_workers=3) as executor:
        to_do = []
        for cc in sorted(cc_list):
            future = executor.submit(download_one, cc)
            to_do.append(future)
            msg = 'Scheduled for {}: {}'
            print(msg.format(cc, future))
        results = []
        for future in futures.as_completed(to_do):
            res = future.result()
            msg = '{} result: {!r}'
            print(msg.format(future, res))
            results.append(res)
    return len(results)

if __name__ == '__main__':
    main(download_many)