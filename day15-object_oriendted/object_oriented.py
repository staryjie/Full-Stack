#!/usr/local/bin/python3
# -*- coding:utf-8 -*-

# 面向对象

'''

1、面向过程编程
2、函数式编程     def 函数
3、面向对象编程    类，def 函数
'''



class Test():

    def f1(self): # self是一个形参，Python内部传递，谁调用该方法，self就是谁
        print("this is the function of f1.")

    def f2(self):
        print("this is the function of f2.")

obj = Test()
obj.f1()
obj.f2()
