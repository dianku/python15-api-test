# -*- coding: utf-8 -*-
# @Time : 2020/4/9 16:01
# @Author : Bella
# @Email : 1171208366@qq.com
# @FileName : study_re.py
from API_4.common.config import config
import re   #解析正则表达式用的   解析就相当于字符串普通的查找和替换  解析之后会获取到解析的结果
#根据编写的表达式，去指定的字符串里面去找他，找到返回找到的信息，否者返回None
data = '{"mobilephone":"#normal_user#","pwd":"#normal_pwd#"}'
#正则表达式：原本字符，元字符组成
p = "#(.*?)#" #正则表达式


# m = re.search(p,data)  #从任意位置开始找，找到第一个就返回，到第一个就返回Match object,如果没有找到返回None
# print(m.group(0)) #返回表达式和组里面匹配的内容
# print(m.group(1)) #只返回指定的内容
# g = m.group(1)  #拿到参数化的key
# v = config.get('data',g)  #根据key取值配置文件里面的值
# print(v)
# data_new = re.sub(p,v,data,count=1) #查找替换,count 查找替换的次数
# print(data_new)
#如果要匹配多次，替换多次，使用循环来解决
while re.search(p,data):
    print(data)
    m = re.search(p,data)  #从任意位置开始找，找到第一个就返回，到第一个就返回Match object,如果没有找到返回None
    g = m.group(1)  #拿到参数化的key
    v = config.get('data',g)  #根据key取值配置文件里面的值
    print(v)
    #记得替换后的内容，继续用data接收
    data = re.sub(p,v,data,count=1) #查找替换,count 查找替换的次数
print('最后替换后的data',data)

n = re.findall(p,data) #查找全部返回列表


