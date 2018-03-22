#!/usr/bin/env python
# -*- coding:utf-8 -*-


#### 递归

# def f1():
#     return "f1"
#
# def f2():
#     r = f1()
#     return r
#
# def f3():
#     r = f2()
#     return r
#
# def f4():
#     r = f3()
#     return r
#
# ret = f4()
# print(ret)

# def function():
#     return function()
# function()

#斐波那契数列

# def f4(arg1,arg2):
#     if arg1 > 591286729879:
#         return
#     print(arg1)
#     tmp = arg1 + arg2
#     f4(arg2,tmp)
# f4(0,1)

# def function(arg):
#     if arg == 0:
#         return 0
#     elif arg == 1:
#         return 1
#     elif arg > 1:
#         return function(arg - 1) + function(arg - 2)
# ret = function(10)
# print(ret)

#计算器

# 1 - 2 * ( ( 60 - 30 + ( -40.0 / 5) * ( 9 - 2 * 5 / 3 + 7 / 3 * 99 / 4 * 2998 + 10 * 568 / 14 )) - (-4 * 3) / ( 16 - 3 * 2)

#找到第一个括号中只包含数字，算出结果赋值，依次递归算出括号中的值，知道没有括号，直接retuern值


def num(n,a,b):
    if n == 10:
        return a
    else:
        c = a + b
        r = num(n+1,b,c)
        return r
ret = num(1,0,1)
print(ret)