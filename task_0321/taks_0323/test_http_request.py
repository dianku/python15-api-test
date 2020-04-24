# -*- coding: utf-8 -*-
# @Time : 2020/4/15 1:21
# @Author : Bella
# @Email : 1171208366@qq.com
# @FileName : test_http_request.py

import unittest

from task_0321.taks_0323.http_request import HttpRequest

from ddt import ddt,data,unpack
test_data=[['get',{'mobilephone':'18688773467','pwd':'123456'},'10001'],
           ['post',{'mobilephone':'18688773467','pwd':'123456'},'10001'],
           ['get',{'mobilephone':'18688773467','pwd':'12345678'},'20111'],
           ['get',{'mobilephone':'1868877346789','pwd':'123456'},'20111']]
@ddt
class TestHttpRequest(unittest.TestCase):
    def setUp(self):
        self.url = 'http://test.lemonban.com/futureloan/mvc/api/member/login'

    @data(*test_data)
    def test_login_api(self,item):
        resp = HttpRequest().http_request(item[0],self.url,item[1])
        #断言code
        self.assertEqual(resp.json()['code'],item[2])









    # @data()
    # def test_normal_login_1(self):#正常登录
    #     param = {'mobilephone':'18688773333', 'pwd':'123456'}
    #     resp = HttpRequest().http_request('get',self.url,param)
    #     #断言code
    #     self.assertEqual('10001',resp.json()['code'])
    #
    # @data()
    # def test_normal_login_2(self):#正常登录
    #     param = {'mobilephone':'18688773444', 'pwd':'123456'}
    #     resp = HttpRequest().http_request('post',self.url,param)
    #     #断言code
    #     self.assertEqual('10001',resp.json()['code'])
    # @data()
    # def test_err_pwd_login(self):#输入错误的密码登录
    #     param = {'mobilephone':'186887734', 'pwd':'123456789'}
    #     resp = HttpRequest().http_request('get',self.url,param)
    #     #断言code
    #     self.assertEqual('20111',resp.json()['code'])
    # @data()
    # def test_err_tel_login(self):#输入错误的手机号码
    #     param = {'mobilephone':'19088773333', 'pwd':'123456'}
    #     resp = HttpRequest().http_request('get',self.url,param)
    #     #断言code
    #     self.assertEqual('20111',resp.json()['code'])

