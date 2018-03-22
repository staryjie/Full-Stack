#!/usr/bin/env python
# -*- coding:utf-8 -*-

#写函数，检查传入列表的长度，如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者。

def checklen(args):
    if isinstance(args,list):
        if len(args) > 2:
            del args[2:]
            return args
        else:
            return args
    else:
        return "传入参数不是列表"
li = ["11","abc","wq","sa"]
ret = checklen(li)
print(ret)