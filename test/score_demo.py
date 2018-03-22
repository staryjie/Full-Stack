#!/usr/bin/env python
# -*- coding:utf-8 -*-

score = int(input("Pls enter yur score: "))

if score > 100:
    print("分数不能超过100！")
elif score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 60:
    print("C")
elif score >= 40:
    print("D")
elif score >=0:
    print("E")
elif score < 0:
    print("分数不能为负数！")