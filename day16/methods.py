#!/usr/local/bin/python3
# -*- coding:utf-8 -*-

class Provice:

    country = "中国"

    def __init__(self,name):
        temp = "xxx"

        self.name = name

    # 静态方法,不需要创建对象即可执行
    @staticmethod
    def xo(arg1,arg2):
        print("xo")

    # 普通方法，必须创建对象才能执行
    def show(self):
        print("show")

    # 类方法,只能通过类访问
    @classmethod
    def xxoo(cls):
        print("xxoo",cls)

Provice.xxoo()