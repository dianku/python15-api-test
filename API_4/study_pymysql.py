# -*- coding: utf-8 -*-
# @Time : 2020/4/8 15:33
# @Author : Bella
# @Email : 1171208366@qq.com
# @FileName : study_pymysql.py

import pymysql

#1,建立连接：数据库连接信息：
host = "test.lemonban.com"
user = "test"
password = "test"
port = 3306
mysql = pymysql.connect(host=host,user=user,password=password,port=port) #建立连接保存连接
#2,新建一个查询页面
cursor = mysql.cursor()  #记录的作用  建立游标
#3，编写SQL
sql = 'select max(mobilephone) from future.member'   #只有一条时
# sql = 'select * from future.loan limit 10' #查询有多条时
#4,执行SQL
cursor.execute(sql)   #用游标对象的execute()方法执行sql把sql语句放进去
# 5,查看结果
result = cursor.fetchone() #获取查询结果集里面最近的一条数据返回
# result = cursor.fetchall() #获取全部结果集
print(type(result),result[0])
#6，关闭查询
cursor.close()
#7，关闭数据库连接
mysql.close()
#获取的结果是元组类型数据