# -*- coding: utf-8 -*-
# @Time : 2020/4/15 1:19
# @Author : Bella
# @Email : 1171208366@qq.com
# @FileName : http_request.py


# 1：作业安排：
# 写一个类：里面有一个方法 http_request 能够完成get请求或post请求，要求有返回值
# 每个请求要求有请求参数
# 登录请求地址：http://47.107.168.87:8080/futureloan/mvc/api/member/login
# 请求参数：mobilephone:18688773467 pwd：123456 登录的时候需要提供手机号码和密码
import requests

class HttpRequest:

    def http_request(self,method,url,param):
        '''完成http的get请求或post请求
        :method 请求方法 可以是get or post
        :url 请求地址
        :param 请求参数，字典的格式'''
        if method.lower()=='get': # 发送一个get请求:如果请求有参数的话 就要以字典的形式传递过去
            try:
                resp=requests.get(url,params=param)#响应结果消息实体  包含：响应头 响应报文 状态码
                print('get响应报文:',resp.text)#响应报文
            except Exception as e:
                print('get请求出错：{}'.format(e))
        else:#除了get就是post 所以这里设定else情况是发送一个post请求
            try:
                resp=requests.post(url,data=param)#响应结果消息实体  包含：响应头 响应报文 状态码
                print('post响应报文:',resp.text)#响应报文
            except Exception as e:
                print('post请求出错：{}'.format(e))
        return resp


if __name__ == '__main__':
    login_url='http://test.lemonban.com/futureloan/mvc/api/member/register'
    param={'mobilephone':'15541466666', 'pwd':'lc123456'}
    resp=HttpRequest().http_request('post',login_url,param)
    print('结果是：{}'.format(resp.json()))

