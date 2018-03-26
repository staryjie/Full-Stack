#!/usr/local/bin/python3
# -*- coding:utf-8 -*-

# 静态字段

class Foo:

    country = "China" # 静态字段，在类中保存，在Python解释器运行到这的时候还没有创建对象，只是创建了一个类，所以静态字段保存在类中

    def __init__(self,name):
        temp = "xxx"
        self.name = name # 普通字段，在对象中保存

    def show(self): # 普通方法，在类中保存
        print("show")


class Provice:

    country = "中国"

    def __init__(self,name):
        self.name = name
        # self.country = "China"

    def show(self):
        print(self.country,self.name)

hebei = Provice("河北")
henan = Provice("河南")
hebei.show()
henan.show()