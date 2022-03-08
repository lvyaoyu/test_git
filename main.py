# -*- coding: utf-8 -*-
# @Time : 2022-03-08 12:07 
# @Author : YD

from loguru import logger

from conifg import *


for k,v in dict(setting).items():
    logger.info(f"{k},{v}")
