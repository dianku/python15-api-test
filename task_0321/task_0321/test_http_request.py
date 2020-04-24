# -*- coding: utf-8 -*-
# @Time : 2020/4/15 1:21
# @Author : Bella
# @Email : 1171208366@qq.com
# @FileName : test_http_request.py

import unittest

from task_0321.task_0321.http_request import HttpRequest


class TestHttpRequest(unittest.TestCase):
    def setUp(self):
        self.url = 'http://test.lemonban.com/futureloan/mvc/api/member/login'
    def test_normal_login_1(self):#正常登录
        param = {'mobilephone':'18688773333', 'pwd':'123456'}
        resp = HttpRequest().http_request('get',self.url,param)
        #断言code
        self.assertEqual('10001',resp.json()['code'])


    def test_normal_login_2(self):#正常登录
        param = {'mobilephone':'18688773444', 'pwd':'123456'}
        resp = HttpRequest().http_request('post',self.url,param)
        #断言code
        self.assertEqual('10001',resp.json()['code'])

    def test_err_pwd_login(self):#输入错误的密码登录
        param = {'mobilephone':'186887734', 'pwd':'123456789'}
        resp = HttpRequest().http_request('get',self.url,param)
        #断言code
        self.assertEqual('20111',resp.json()['code'])

    def test_err_tel_login(self):#输入错误的手机号码
        param = {'mobilephone':'19088773333', 'pwd':'123456'}
        resp = HttpRequest().http_request('get',self.url,param)
        #断言code
        self.assertEqual('20111',resp.json()['code'])

