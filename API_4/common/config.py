# -*- coding: utf-8 -*-
# @Time : 2020/4/20 16:55
# @Author : Bella
# @Email : 1171208366@qq.com

import configparser
from API_4.common import constants
class ReadConfig:
    """
    完成配置文件的读取
    """
    def __init__(self):
        self.config = configparser.ConfigParser()   #实际上有get方法的是这个
        self.config.read(constants.global_file,encoding='utf-8')    #先加载global
        switch = self.config.getboolean('switch','on')
        if switch:   #开关打开的时候，使用online的配置
            self.config.read(constants.online_file,encoding='utf-8')
        else:   #开关关闭的时候，使用test的配置
            self.config.read(constants.test_file,encoding='utf-8')

    def get(self,section,option):
        return self.config.get(section,option)

config = ReadConfig()

if __name__ == '__main__':
    config = ReadConfig()
    print(config.get('api','pre_url'))

