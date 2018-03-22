#!/usr/bin/env python
# -*- coding:utf-8 -*-

####map()的实现原理
def MyMap(fun,arg):
    result = []
    for i in li:
        ret = fun(i)
        result.append(ret)
    return result

def x(arg):
    return arg + 100

li = [11,22,33,44,55,66]

ret = MyMap(x,li)
print(ret)