#!/usr/bin/env python
# -*- coding:utf-8 -*-


#####装饰器

def outer(func):
    def inner():
        print("hello")
        print("hello")
        print("hello")
        r = func()
        print("end")
        print("end")
        print("end")
        return r
    return inner

@outer
def f1():
    print("F1")
    return "ooo"
'''解释器执行到@outer,会做如下操作
1.执行outer()函数，并且将其下面的函数名，当做参数传入outer(f1)
2.将outer()的返回值，重新赋值给f1
3.outer()中的inner()下的function()函数就是外面的f1()函数
4.执行下面的f1()函数时，其实是执行了inner()函数
'''
f1()
'''
@outer相当于如下内容
f1 = outer(f1)
result = f1()
print(result)
'''