#!/usr/local/bin/python3
# -*- coding:utf-8 -*-

# 特殊类成员 - iter

class Foo:

    def __init__(self):
        pass

    def __iter__(self):
        yield 1
        yield 2
        yield 3
        yield 4

obj = Foo()

for i in obj: # 循环对象的时候，默认就去循环类中__iter__生成的数据，就是去循环生成器
    print(i)