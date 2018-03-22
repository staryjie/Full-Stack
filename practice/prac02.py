#!/usr/bin/env python
# -*- coding:utf-8 -*-

#查找
# 查找列表中元素，移除每个元素的空格，并查找以 a或A开头 并且以 c 结尾的所有元素。
# li = ["alec", " aric", "Alex", "Tony", "rain"]
# tu = ("alec", " aric", "Alex", "Tony", "rain")
# dic = {'k1': "alex", 'k2': ' aric',  "k3": "Alex", "k4": "Tony"}

li = ["alec", " aric", "Alex", "Tony", "rain"]
tu = ("alec", " aric", "Alex", "Tony", "rain")
dic = {'k1': "alex", 'k2': ' aric',  "k3": "Alex", "k4": "Tony"}

new_li = []
new_tu = ()
new_dic = {}
for i in li:
    ret = i.strip()
    if (ret.startswith("a") or ret.startswith("A")) and ret.endswith("c"):
        print(ret)

for i in tu:
    ret = i.strip()
    if (ret.startswith("a") or ret.startswith("A")) and ret.endswith("c"):
        print(ret)

for k,v in dic.items():
    ret = v.strip()
    if (ret.startswith("a") or ret.startswith("A")) and ret.endswith("c"):
        print(ret)