#!/usr/bin/env python
# -*- coding:utf-8 -*-
#写函数，检查用户传入的对象（字符串、列表、元组）的每一个元素是否含有空内容。
def checkkg(args):
    ret = True
    for i in args:
        if i.isspace():
            ret = False
            break
    else:
        return ret

s ="he he he"
s1 = "jhfghjk"
li = [" ",1,22,4]
tu = (" ",12,45)
ret = checkkg(s1)
print(ret)