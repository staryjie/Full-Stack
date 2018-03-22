#!/usr/bin/env python
# -*- coding:utf-8 -*-

# def f1():
#     print("F1")
#
# def f1():
#     print("FF1")
#
# f1()

################################################ 装饰器 ######################################################
# def outer(func):
#     def inner():
#         print("hello")
#         print("hello")
#         print("hello")
#         r = func()
#         print("end")
#         print("end")
#         print("end")
#         return r
#     return inner
# @outer
# def f1():
#     print("F1")
#     return "xxx"
# f1()

# def outer(func):
#     return "s"
#
# @outer
# def index():
#     #功能
#     return True
#
# print(index)
'''
上面部分可以看出，当解释器执行到'@outer'的时候，会把outer()函数的返回值赋值给index.
'''

# def outer(func):
#     def inner():
#         print("我就是index()函数")
#     return inner()
#
# @outer
# def index():
#     print("原函数功能")
#     return True
'''
从这里可以看出，如果outer()里面定义一个函数，可以将这个函数作为返回值赋值给index，后面的index()函数其实就是装饰器中的inner()函数。
'''

# def outer(func):
#     def inner():
#         print("原函数执行之前增加的其他功能")
#         func()
#         print("原函数实现之后增加的额外功能")
#     return inner()
#
# @outer
# def index():
#     print("原函数功能")

#装饰器装饰含两个参数的函数

# def outer(func):
#     def inner(arg1,arg2):
#         print("第一个数为：",arg1)
#         ret = func(arg1,arg2)
#         print("第二个数为：",arg2)
#         return ret
#     return inner
# @outer
# def sum(a1,a2):
#     result = a1 + a2
#     info = "两个数的和为：" + str(result)
#     return info
# ret = sum(12,22)
# print(ret)

#装饰器装饰含N个参数的函数

# def outer(func):
#     def inner(*args,**kwargs):
#         print("123")
#         ret = func(*args,**kwargs)
#         print("456")
#         return ret
#     return inner
#
# @outer
# def f():
#     print("f()")
# @outer
# def f1(arg):
#     print(arg)
# @outer
# def f2(arg1,arg2):
#     print(arg1,arg2)
# @outer
# def f3(arg1,arg2,arg3):
#     print(arg1,arg2,arg3)
# @outer
# def f4(*args,**kwargs):
#     print(*args,**kwargs)
#
# dic = {
#     "k1":2,
#     "k2":3
# }
# # f2(1,dic)
# f4(1,2,3,dic)

def outer2(func):
    def inner(*args,**kwargs):
        print("new 123")
        ret = func(*args,**kwargs)
        return ret
    return inner

def outer1(func):
    def inner(*args,**kwargs):
        print("123")
        ret = func(*args,**kwargs)
        print("456")
        return ret
    return inner
@outer2
@outer1
def index(a1,a2):
    print("原函数功能")
    return a1+a2

ret = index(1,2)
print(ret)