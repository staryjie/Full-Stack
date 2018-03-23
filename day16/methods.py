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

    # 特性，将方法伪造成字段
    def start(self):
        temp = "%s sb"% self.name
        return temp

    @property #把原来的方法设置成直接通过字段的方式访问，不能加参数
    def end(self):
        temp = "%s sb" % self.name
        return temp

Provice.xxoo()

obj = Provice("alex")
ret1 = obj.start()
ret2 = obj.end # 没有加括号()
print(ret1,ret2)