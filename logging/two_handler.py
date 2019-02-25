#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : two_handler.py
# @Author: yubo
# @Date  : 2019/1/22
# @Desc  :

import logging
import logging.handlers
import logging.config
import datetime

logger = logging.getLogger('mylogger.test1.test2')
logger.setLevel(logging.DEBUG)

logger_mylogger_test1 = logging.getLogger('mylogger.test1')


rf_handler = logging.handlers.TimedRotatingFileHandler('all.log', when='midnight', interval=1, backupCount=7)
rf_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))

f_handler = logging.FileHandler('error.log')
f_handler.setLevel(logging.DEBUG)
f_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(filename)s[:%(lineno)d] - %(message)s"))

#logger_mylogger_test1.addHandler(rf_handler)
#logger.addHandler(rf_handler)
logger.addHandler(f_handler)

logger.debug('debug message %d', 0)
logger.info('info message')
logger.warning('warning message')
logger.error('error message')
logger.critical('critical message')