#!/usr/bin/env python
# -*- coding:utf-8 -*-

def function1(args):
    num = 0
    zimu = 0
    kg = 0
    oth = 0
    for i in args:
        if i.isdigit():
            num += 1
        elif i.isalpha():
            zimu += 1
        elif i == " ":
            kg += 1
        else:
            oth += 1
    return {"数字":num,"字母":zimu,"空格":kg,"其他":oth}

dic = function1("asd234 -45sasa呵呵sa1 21*()")
print(dic)