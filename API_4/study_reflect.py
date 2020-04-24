# -*- coding: utf-8 -*-
# @Time : 2020/4/22 23:25
# @Author : Bella
# @Email : 1171208366@qq.com

class People():

    number_leg = 2

    def __init__(self,name,age):
        self.name = name
        self.age =age

if __name__ == '__main__':
    p = People('liuchuang',18)

    print(hasattr(People,'number_eyes'))
    print(getattr(People,'number_leg'))
    setattr(People,'number_eyes',2)
    print(getattr(People,'number_eyes'))
