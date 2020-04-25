# -*- coding: utf-8 -*-
# @Time : 2020/4/24 2:35
# @Author : Bella
# @Email : 1171208366@qq.com
# @function:

import sys
sys.path.append('./') #加到project根目录地址

import unittest
from API_4.testcases import test_login
import HTMLTestRunnerNew
from API_4.common import constants

suite = unittest.TestSuite()
loader = unittest.TestLoader() #找case
suite.addTest(loader.loadTestsFromModule(test_login))

discover = unittest.defaultTestLoader.discover(constants.case_dir,'test_*.py')

with open(constants.report_dir+'/report.html','wb+') as file:
    runner = HTMLTestRunnerNew.HTMLTestRunner(
        stream=file,
        title='python15 api test report',
        description='前程贷API',
        verbosity=3,
        tester='刘闯'
    )
    runner.run(discover)
