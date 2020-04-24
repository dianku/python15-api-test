# -*- coding: utf-8 -*-
# @Time : 2020/4/6 15:52
# @Author : Bella
# @Email : 1171208366@qq.com
# @FileName : http_request.py

import requests
from API_4.common import logger
from API_4.common.config import config #这个config是对象的引用
logger = logger.get_logger(__name__)

class  HttpRequest:  #对类进行封装
    """
    使用这个类的request方法去完成不同的http请求，并且返回响应结果
    """
    def request(self,method,url,data=None,json=None,cookies=None):
        if type(data) == str:
            data = eval(data) #将str转换成字典

        if method.lower() == 'get': #强制将method转换成小写
            resp=requests.get(url,params=data,cookies=cookies)

        elif method.lower() == 'post':
            if json is not None:   #或者if none也可以
                resp=requests.post(url,json=json,cookies=cookies)
            else:
                resp=requests.post(url,data=data,cookies=cookies)
        else:
            print('UN-support method')
        return resp

class HttpRequest2:

    def __init__(self):
        #打开一个session   一个实例变量 对象属性  实例化Http_Request2的时候就自带这个变量，就是一个session会话的对象
        self.session=requests.sessions.Session()

    def request(self,method,url,data=None,json=None):   #data为None是要支持get可能不需要传参
        if type(data) == str:
            data = eval(data) #将str转换成字典

        #拼接rul
        url = config.get('api','pre_url')+url
        logger.debug("请求的url:{0}".format(url))
        logger.debug('请求data:{0}'.format(data))

        if method.lower() == 'get': #强制将method转换成小写
            resp = self.session.request(method=method,url=url,params=data)

        elif method.lower() == 'post': #强制将method转换成小写
            if json:
                resp = self.session.request(method=method,url=url,json=json)
            else:
                resp = self.session.request(method=method,url=url,data=data)
        else:
            logger.error('UN-support method')
        logger.debug("请求的response:{0}".format(resp.text))

        return resp
    #session打开还需要关闭 用完就需要关闭

    def close(self):
        self.session.close()


if __name__ == '__main__':
    # params = {"mobilephone": "15810447878", "pwd": "123456"}
    # url = 'http://test.lemonban.com/futureloan/mvc/api/member/login'
    # http_request=Http_Request()
    # #调用登录接口
    # resp=http_request.request('POST',url,data=params)
    # print(resp.text)
    # print(resp.cookies)
    #
    # #调用充值接口
    # params = {"mobilephone": "15810447878", "amount": "1000"}
    # url = 'http://test.lemonban.com/futureloan/mvc/api/member/recharge'
    # resp2=http_request.request('post',url,data=params,cookies=resp.cookies)
    # print(resp2.text)
    # print(resp2.status_code)
    # print(resp2.cookies)
    url = 'http://test.lemonban.com/futureloan/mvc/api/member/login'
    params = {"mobilephone": "15810447878", "pwd": "123456"}
    http_request2 = HttpRequest2()
    resp = http_request2.request('post',url,data=params)
    print(resp.text)

    params = {"mobilephone": "15810447878", "amount": "1000"}
    url = 'http://test.lemonban.com/futureloan/mvc/api/member/recharge'
    resp = http_request2.request('post',url=url,data=params)
    print(resp.text)
    print(resp.cookies)
    print(resp.status_code)





