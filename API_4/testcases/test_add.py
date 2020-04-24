# -*- coding: utf-8 -*-
# @Time : 2020/4/9 15:12
# @Author : Bella
# @Email : 1171208366@qq.com
# @FileName : test_add.py


import unittest
from API_4.common.http_request import HttpRequest2
from API_4.common import do_excel
from API_4.common import constants
from ddt import ddt,data,unpack
from API_4.common.config import config
from API_4.common import context

@ddt
class AddTest(unittest.TestCase):
    excel = do_excel.DoExcel(constants.case_file,'add')
    cases = excel.get_cases()   #列表里面放case实例

    @classmethod   #类方法每个类只执行一次
    def setUpClass(cls):   #初始化    类方法
        cls.http_request = HttpRequest2()   #保持一个session

    @data(*cases)   #传进来的数据时case的实例  列表里多组数据传进来
    def test_add(self,case):
        # case.data = eval(case.data) #变成字典
        # print(type(case.data))
        # if case.data.__contains__('mobilephone') and case.data['mobilephone'] == 'normal_user':
        #     case.data['mobilephone'] = config.get('data', 'normal_user')  # 拿到配置文件里面的值赋值给mobilephone
        #
        # if case.data.__contains__('pwd') and case.data['pwd'] == 'normal_pwd':
        #     case.data['pwd'] = config.get('data', 'normal_pwd')
        #
        # if case.data.__contains__('memberId') and case.data['memberId'] == 'loan_member_id':
        #     case.data['memberId'] = config.get('data', 'loan_member_id')

        #请求之前替换参数化的值
        case.data= context.replace(case.data)
        print(case.title)
        resp = self.http_request.request(case.method,case.url,case.data)
        try:
            self.assertEqual(str(case.expected),resp.json()['code'])
            self.excel.write_result(case.case_id+1,resp.text,'PASS')
        except AssertionError as e:
            self.excel.write_result(case.case_id+1,resp.text,'FAILE')
            raise e
    @classmethod
    def tearDownClass(cls):
        cls.http_request.close()


