#!/usr/local/bin/python3
# -*- coding:utf-8 -*-

# 成员修饰符-Python特殊之处

class Foo:

    def __init__(self):
        self.__name = "staryjie"


obj = Foo()
# print(obj.__name) # 私有的普通字段无法通过类实例化的对象直接访问
# Python特殊之处：
print(obj._Foo__name) # 在Python中，私有的类成员可以通过"_类名__成员名"来访问，但是一般不使用这种方法。