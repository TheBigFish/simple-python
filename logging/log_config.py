#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : log_config.py.py
# @Author: yubo
# @Date  : 2019/2/20
# @Desc  :

#!/usr/bin/env python
import logging
import logging.config

args = "('info.log','a')"
args_ = eval(args)

logging.config.fileConfig('log.conf')

logs = logging.getLogger('error')
logs.error('errorsssss')
