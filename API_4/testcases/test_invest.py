# -*- coding: utf-8 -*-
# @Time : 2020/4/23 0:05
# @Author : Bella
# @Email : 1171208366@qq.com

import unittest
from API_4.common.http_request import HttpRequest2
from API_4.common import do_excel
from API_4.common import constants
from ddt import ddt,data
from API_4.common import context
from API_4.common import do_mysql
from API_4.common.context import Context

@ddt
class AddTest(unittest.TestCase):
    excel = do_excel.DoExcel(constants.case_file,'invest')
    cases = excel.get_cases()   #列表里面放case实例

    @classmethod   #类方法每个类只执行一次
    def setUpClass(cls):   #初始化    类方法
        cls.http_request = HttpRequest2()   #保持一个session
        cls.mysql=do_mysql.DoMysql()

    @data(*cases)   #传进来的数据时case的实例  列表里多组数据传进来
    def test_invests(self,case):
        print(case.title)

        #请求之前替换参数化的值
        case.data= context.replace(case.data)
        resp = self.http_request.request(case.method,case.url,case.data)
        try:
            self.assertEqual(str(case.expected),resp.json()['code'])
            self.excel.write_result(case.case_id+1,resp.text,'PASS')

            #判断加标成功之后 查询数据库 取到loan_id
            if resp.json()['msg'] == '加标成功':
                sql = 'select id from future.loan where memberid = 1290 order by id desc limit 1'
                loan_id = self.mysql.fetch_one(sql)[0] #返回元组数据类型
                print('加标之后的ID',loan_id)
                #保存到类属性里面
                setattr(Context,'loan_id',str(loan_id))

        except AssertionError as e:
            self.excel.write_result(case.case_id+1,resp.text,'FAILE')
            raise e
    @classmethod
    def tearDownClass(cls):
        cls.http_request.close()