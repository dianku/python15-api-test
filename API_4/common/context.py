# -*- coding: utf-8 -*-
# @Time : 2020/4/22 16:07
# @Author : Bella
# @Email : 1171208366@qq.com

import re
from API_4.common.config import config
import configparser

class Context:
    loan_id = None

def replace(data):
    p = "#(.*?)#" #正则表达式
    while re.search(p,data):
        m = re.search(p,data)  #从任意位置开始找，找到第一个就返回，到第一个就返回Match object,如果没有找到返回None
        g = m.group(1)  #拿到参数化的key
        try:
            v = config.get('data',g)  #根据key取值配置文件里面的值
        except configparser.NoOptionError as e: #如果配置文件里面没有的话去Context里面去取
            if hasattr(Context,g):
                v = getattr(Context,g)
            else:
                print('找不到参数化的值')
                raise e
        print(v)
        #记得替换后的内容，继续用data接收
        data = re.sub(p,v,data,count=1) #查找替换,count 查找替换的次数
    return data
#步骤传进来一个data，并用data近search
#然后去查找
#找到了到配置文件里找对应的值
#拿到值之后就去替换
#替换之后返回data


