# -*- coding: utf-8 -*-
# @Time : 2020/4/8 14:55
# @Author : Bella
# @Email : 1171208366@qq.com
# @FileName : test_login.py

import unittest
from API_4.common import logger
from API_4.common.http_request import HttpRequest2
from API_4.common import do_excel
from API_4.common import constants
from ddt import ddt,data


logger = logger.get_logger(__name__)

@ddt
class LoginTest(unittest.TestCase):
    excel = do_excel.DoExcel(constants.case_file,'login')
    cases = excel.get_cases()   #列表里面放cases实例

    @classmethod   #类方法每个类只执行一次
    def setUpClass(cls):   #初始化    类方法
        logger.info('准备测试前置')
        cls.http_request = HttpRequest2()

    @data(*cases)   #传进来的数据时case的实例  列表里多组数据传进来
    def test_login(self,case):
        logger.info('开始测试:{0}'.format(case.title))
        resp = self.http_request.request(case.method,case.url,case.data)
        try:
            self.assertEqual(case.expected,resp.text)
            self.excel.write_result(case.case_id+1,resp.text,'PASS')
        except AssertionError as e:
            self.excel.write_result(case.case_id+1,resp.text,'FAILE')
            logger.error('报错了,{}'.format(e))
            raise e
        logger.info('结束测试:{0}'.format(case.title))
    @classmethod
    def tearDownClass(cls):
        cls.http_request.close()
        logger.info('测试后置处理')
