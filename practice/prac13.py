#!/usr/bin/env python
# -*- coding:utf-8 -*-
#写函数，利用递归获取斐波那契数列中的第 10 个数，并将该值返回给调用者。

# 0 1 1 2 3 5 8 13 21 34
def fbnq(depth,arg1,arg2):
    if depth == 10:
        return arg1
    print(arg1)
    arg3 = arg1 + arg2
    ret = fbnq(depth+1 ,arg2,arg3)
    return ret
ret = fbnq(1,0,1)
print(ret)

# def function(arg):
#     if arg == 0:
#         return 0
#     elif arg == 1:
#         return 1
#     elif arg > 1:
#         return function(arg - 1) + function(arg - 2)
# ret = function(9)
# print(ret)