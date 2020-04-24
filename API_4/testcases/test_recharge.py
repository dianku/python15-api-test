# -*- coding: utf-8 -*-
# @Time : 2020/4/8 14:56
# @Author : Bella
# @Email : 1171208366@qq.com
# @FileName : test_recharge.py

import unittest

# setup() #每一个testmethod执行之前，它会执行一遍
# teardown() #每一个testmethod执行之后，它会执行一次

from API_4.common import  constants
from API_4.common import do_excel
from ddt import ddt,data,unpack
from API_4.common.http_request import HttpRequest2

@ddt
class RechargeTest(unittest.TestCase):
    excel =  do_excel.DoExcel(constants.case_file,'recharge')   #读取充值表单
    cases = excel.get_cases()   #拿到case

    @classmethod
    def setUpClass(cls):
        cls.http_request = HttpRequest2()

    @data(*cases)
    def test_recharge(self,case):
        print(case.title)
        resp =  self.http_request.request(case.method,case.url,case.data)
        actual_code = resp.json()['code']
        try:
            self.assertEqual(str(case.expected),actual_code)
            self.excel.write_result(case.case_id+1,resp.text,"PASS")  #断言成功写入PASS
        except AssertionError as e:
            self.excel.write_result(case.case_id+1,resp.text,"FAIL")  #断言成功写入FAILE
        raise e