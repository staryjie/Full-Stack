#!/usr/local/bin/python3
# -*- coding:utf-8 -*-

import comments

# target_func = getattr(comments,'NAME')
# print(target_func)
# ret = target_func()
# print(ret)

r = hasattr(comments,"AGE")
print(r)

setattr(comments,"AGE",26)

setattr(comments,"f4",lambda a:a+1)

r = hasattr(comments,"AGE")
print(r)

delattr(comments,"AGE")