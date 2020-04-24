# -*- coding: utf-8 -*-
# @Time : 2020/4/23 23:50
# @Author : Bella
# @Email : 1171208366@qq.com
# @function:

import logging
from API_4.common import constants

def get_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel('DEBUG')

    fmt = "%(asctime)s - %(name)s - %(levelname)s - %(message)s - [%(filename)s:%(lineno)d] "
    formatter = logging.Formatter(fmt=fmt)

    console_handler = logging.StreamHandler() #控制台
    #不是日志级别放到配置文件里面去做到可变的--优化
    console_handler.setLevel('DEBUG') #指定输出级别
    console_handler.setFormatter(formatter)

    file_handler = logging.FileHandler(constants.log_dir+'/case.log',encoding='utf-8')
    #把日志级别放到配置文件里面配置
    file_handler.setLevel('INFO')
    file_handler.setFormatter(formatter)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
    return logger

# logger = get_logger('case')
# logger.info('测试开始啦')
# logger.debug('测试数据')
# logger.error('测试报错')
# logger.info('测试结束啦')
