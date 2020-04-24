# -*- coding: utf-8 -*-
# @Time : 2020/4/16 0:40
# @Author : Bella
# @Email : 1171208366@qq.com
# @FileName : d2_email.py


#添加附件
#解析邮件格式的方式，发送一个标准的email
#发送一个html格式的邮件
import smtplib
from email.mime.text import MIMEText #解析邮件格式
from email.mime.application import MIMEApplication #用来传各种各样不同的附件
from email.mime.multipart import MIMEMultipart

#总的邮件内容，分为不同的模块
msg_total = MIMEMultipart()
msg_total['subject'] = 'nihao'

#正文模块
msg_raw = """<p style="color:red">你好</p>"""
msg = MIMEText(msg_raw,'html')
msg_total.attach(msg)

#附件模块
file = MIMEApplication(open('demo.txt','rb').read()) #读取文件信息
#添加附件的头信息
file.add_header('content-Dispostion','attachment',filename='demo.txt')
#把附件模块添加到总的里面去
msg_total.attach(file)


with smtplib.SMTP_SSL("smtp.qq.com".encode(), 465) as server:
    #登录
    server.login('1171208366@qq.com','ttddaxjizuuhfeig')
    #发送邮件
    server.sendmail('1171208366@qq.com','198954680@qq.com',msg_total.as_string())