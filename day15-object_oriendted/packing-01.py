#!/usr/local/bin/python3
# -*- coding:utf-8 -*-

# 封装-构造方法

class Foo:

    def __init__(self,bk): # 构造方法；如果多个对象只需要一样的封装数据，则只需要self参数即可；如果有不同的数据，可以设定多个形参，在实例化对象的时候传入不同的实参即可。
        self.name = "staryjie" # 如果多个对象需要封装的参数一样，只需要在__init__方法中定义一个就可以
        self.favor = bk

obj1 = Foo("xx")
print(obj1.favor,obj1.name)
obj2 = Foo("oo")
print(obj2.favor,obj2.name)