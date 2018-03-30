#!/usr/local/bin/python3
# -*- coding:utf-8 -*-

sec = input("请输入秒数： ")
if sec.isdigit():
    sec = int(sec)
    hour = sec / 3600
    min = hour % 60
    sec = sec % 60
    msg = "%d时%d分%d秒"%(hour,min,sec)
    print(msg)
else:
    print("输入有误！")