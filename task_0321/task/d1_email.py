# -*- coding: utf-8 -*-
# @Time : 2020/4/15 21:48
# @Author : Bella
# @Email : 1171208366@qq.com

import smtplib
#
# #选择邮件服务商
# server = smtplib.SMTP_SSL("smtp.qq.com".encode(), 465)
#
# #登录
# server.login('1171208366@qq.com','ttddaxjizuuhfeig')
#
# #发送邮件
# msg = '''\\
# From:liuchuang
# Subject:woaini
#
# This is a test '''
# server.sendmail('1171208366@qq.com','198954680@qq.com',msg)
#
# #关闭
# server.quit()

with smtplib.SMTP_SSL("smtp.qq.com".encode(), 465) as server:
    #登录
    server.login('1171208366@qq.com','ttddaxjizuuhfeig')
    #发送邮件
    msg = '''\\
    From:liuchuang
    Subject:woaini
    This is a test '''
    server.sendmail('1171208366@qq.com','198954680@qq.com',msg)

