#!/usr/local/bin/python3
# -*- coding:utf-8 -*-

# 利用反射查看面向对象成员归属

class Foo:

    def __init__(self,name):
        self.name = name

    def show(self):
        print("show")

obj = Foo("staryjie")

ret1 = hasattr(Foo,"show")
ret2 = hasattr(obj,"name")
ret3 = hasattr(obj,"show")
print(ret1,ret2,ret3)

r1 = Foo.__dict__
r2 = obj.__dict__
print(r1)
print(r2)

# 反射：类，只能找类中的成员
# 反射：对象，既可以找对象的成员，也可以找到类成员