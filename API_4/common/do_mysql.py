# -*- coding: utf-8 -*-
# @Time : 2020/4/21 17:30
# @Author : Bella
# @Email : 1171208366@qq.com

import pymysql

class DoMysql:
    """
    完成与MYSQL数据库的一个交互
    """
    def __init__(self):
        #把这些参数放到配置文件里面去做，然后在这里读取配置文件
        host = "test.lemonban.com"
        user = "test"
        password = "test"
        port =3306
        #创建连接
        self.mysql = pymysql.connect(host=host,user=user,password=password,port=port,charset="utf8")
        #设置返回字典
        self.cursor = self.mysql.cursor(pymysql.cursors.DictCursor) #创建游标

    def fetch_one(self,sql):
        self.cursor.execute(sql)
        self.mysql.commit()
        return self.cursor.fetchone()   #返回一条数据 元组

    def fetch_all(self,sql):
        self.cursor.execute(sql)
        return self.cursor.fetchone()   #返回多条数据的时候元组里面套元组

    def close(self):
        self.cursor.close()   #关闭游标
        self.mysql.close()   #关闭连接

if __name__ == '__main__':
    mysql = DoMysql()
    result1 = mysql.fetch_one('select max(mobilephone) from future.member')  # 返回一条数据，元组
    print(type(result1), result1)
    result2 = mysql.fetch_all('select * from future.member limit 10')  # 返回多条数据的时候，元组里面套元组
    print(type(result2), result2)
    mysql.close()
