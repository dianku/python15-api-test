# -*- coding: utf-8 -*-
# @Time : 2020/4/20 2:22
# @Author : Bella
# @Email : 1171208366@qq.com

import os

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) #动态获取当前文件的绝对路径
print(base_dir)

case_file = os.path.join(base_dir,'data','cases.xlsx')

global_file = os.path.join(base_dir,'config','global.conf')

online_file = os.path.join(base_dir,'config','online.conf')

test_file = os.path.join(base_dir,'config','test.conf')

log_dir = os.path.join(base_dir,'log')

case_dir = os.path.join(base_dir,'testcases')

report_dir = os.path.join(base_dir,'reports')
