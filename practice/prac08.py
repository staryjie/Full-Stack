#!/usr/bin/env python
# -*- coding:utf-8 -*-


def lens(args):
    if isinstance(args,str) or isinstance(args,list) or isinstance(args,tuple):
        if len(args) > 5:
            return  True
        else:
            return False
    else:
        return False
ret = lens("hjhgthz")
print(ret)