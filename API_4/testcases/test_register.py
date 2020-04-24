# -*- coding: utf-8 -*-
# @Time : 2020/4/8 14:56
# @Author : Bella
# @Email : 1171208366@qq.com
# @FileName : test_register.py

import unittest
from API_4.common.http_request import HttpRequest2
from API_4.common import do_excel
from API_4.common import constants
from ddt import ddt,data,unpack
from API_4.common import do_mysql

@ddt
class RegisterTest(unittest.TestCase):
    excel = do_excel.DoExcel(constants.case_file,'register')
    cases = excel.get_cases()   #列表里面放cases实例

    @classmethod   #类方法每个类只执行一次
    def setUpClass(cls):   #初始化    类方法
        cls.http_request = HttpRequest2()
        cls.mysql = do_mysql.DoMysql()

    @data(*cases)   #传进来的数据时case的实例  列表里多组数据传进来
    def test_register(self,case):
        if case.data.find('register_mobile')>-1: #判断参数化的标识
            sql = 'select max(mobilephone) from future.member'
            max_phone = self.mysql.fetch_one(sql)[0] #查询最大手机号码
            #最大手机号码+1
            print('最大手机号码',max_phone)
            #replace方法是替换之后返回一个新的字符串，所以需要case.data重新接收
            case.data = case.data.replace('register_mobile',str(max_phone))

        print(case.title)
        resp = self.http_request.request(case.method,case.url,case.data)
        try:
            self.assertEqual(case.expected,resp.text)
            self.excel.write_result(case.case_id+1,resp.text,'PASS')
        except AssertionError as e:
            self.excel.write_result(case.case_id+1,resp.text,'FAILE')
            raise e
    @classmethod
    def tearDownClass(cls):
        cls.http_request.close()
