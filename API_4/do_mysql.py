# -*- coding: utf-8 -*-
# @Time : 2020/4/8 16:22
# @Author : Bella
# @Email : 1171208366@qq.com
# @FileName : do_mysql.py

import pymysql
class DoMysql:
    """
    完成与MySql数据库的一个交互
    """
    def __init__(self):
        host = "test.lemonban.com"
        user = "test"
        password = "test"
        port = 3306
        #创建连接
        self.mysql = pymysql.connect(host=host,user=user,password=password,port=port) #建立连接保存连接
        self.cursor = self.mysql.cursor()
    def fetch_one(self,sql):
        self.cursor.execute(sql)
        return self.cursor.fetchone()

    def fetch_all(self,sql):
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def close(self):
        self.cursor.close()   #关闭游标
        self.mysql.close()   #关闭连接

if __name__ == '__main__':
    mysql = DoMysql()  #用初始化后实例化的过程就是建立连接的郭过程
    result = mysql.fetch_one('select max(mobilephone) from future.member')
    print(result)
    mysql.close()

