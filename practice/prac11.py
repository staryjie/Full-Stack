#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 写函数，检查获取传入列表或元组对象的所有奇数位索引对应的元素，并将其作为新列表返回给调用者。


def funct(arg):
    new_list = []
    for k, v in enumerate(arg):
        if k % 2 != 0:
            new_list.append(arg[k])
    return new_list
tu = ("a","b","c","d","e")
print(funct(tu))

def f4(arg):
    ret = []
    for i in range(len(arg)):
        if i % 2 == 1:
            ret.append(arg[i])
        else:
            pass
    return ret

li = ["11","22","33","44","55"]
ret = f4(li)
print(ret)
