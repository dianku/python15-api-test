# -*- coding: utf-8 -*-
# @Time : 2020/4/6 16:37
# @Author : Bella
# @Email : 1171208366@qq.com
# @FileName : session_request.py

import requests

session = requests.sessions.Session()  #session 是一个函数 会返回一个session request里面的一个session对象刚好名字叫session session对象里面有一个request方法
#登录
url = 'http://test.lemonban.com/futureloan/mvc/api/member/login'
params = {"mobilephone": "15810447878", "pwd": "123456"}
resp=session.request('post',url=url,data=params)
#充值
params = {"mobilephone": "15810447878", "amount": "1000"}
url = 'http://test.lemonban.com/futureloan/mvc/api/member/recharge'
resp=session.request('post',url,data=params)
print(resp.status_code)
print(resp.text)
print(resp.cookies)
#不同的session他们的cookie是不共享的
#Process finished with exit code 0 结束说明程序运行完了，同时所存在的实例化session对象也不存在了，他保存的所有信息也不存在了
#两种传递cookie方式 1、单独的session，把上一个请求的返回的cookies，指定传递到下一个请求的入参cookie当中
#2、使用同一个session，就会自动传递cookie
