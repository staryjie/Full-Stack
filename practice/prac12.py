#!/usr/bin/env python
# -*- coding:utf-8 -*-
#写函数，检查传入字典的每一个value的长度,如果大于2，那么仅保留前两个长度的内容，
# 并将新内容返回给调用者。

# def function(args):
#     for k,v in args.items():
#         if len(v) > 2:
#             print(v[0:2])
# dic = {
#     "k1":"v1v2",
#     "k2":[11,22,33,44]
# }
# ret = function(dic)
# print(ret)

def f5(arg):
    ret = {}
    for key,value in arg.items():
        if len(value) > 2 :
            ret[key] = value[0:2]
        else:
            ret[key] = value
    return ret

dic = {
    "k1":"v1v2",
    "k2":[11,22,33,44],
    "k3":"12"
}

ret = f5(dic)
print(ret)


def method2(arg):
    for key,value in arg.items():
        if len(value) > 2:
            arg[key] = value[0:2]
        else:
            arg[key] = value
    return arg

print(method2(dic))