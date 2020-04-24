# -*- coding: utf-8 -*-
# @Time : 2020/4/15 1:40
# @Author : Bella
# @Email : 1171208366@qq.com
# @FileName : run.py

import unittest

from task_0321.task_0321 import test_http_request

suite = unittest.TestSuite()

#第一种方法：创建实例的方法
# from task_0321.test_http_request import TestHttpRequest
# suite.addTest(TestHttpRequest('test_normal_login_1'))
# suite.addTest(TestHttpRequest('test_normal_login_2'))
# suite.addTest(TestHttpRequest('test_err_pwd_login'))
# suite.addTest(TestHttpRequest('test_err_tel_login'))

#第二种方法:loader的方法:从测试类名去加载
# from task_0321.test_http_request import TestHttpRequest
# loader = unittest.TestLoader()
# suite.addTest(loader.loadTestsFromTestCase(TestHttpRequest))


#第三种方法:loader的方法:通过模块加载测试用例
loader = unittest.TestLoader()
suite.addTest(loader.loadTestsFromModule(test_http_request))


#执行测试用例
runner = unittest.TextTestRunner()
runner.run(suite)


