#!/usr/local/bin/python3
# -*- coding:utf-8 -*-

# 多态
class Foo:

    def f1(self):
        print("Foo")

class Bar:

    def f1(self):
        print("Bar")

'''
def func(Foo arg): # Foo arg 表示arg必须是Foo类对象
    arg.f1()
'''
def func(arg):
    arg.f1()

func(Foo())
func(Bar())