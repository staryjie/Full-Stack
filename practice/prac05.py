#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 用户交互，显示省市县三级联动的选择
import sys
dic = {
    "河北": {
        "石家庄": ["鹿泉", "藁城", "元氏"],
        "邯郸": ["永年", "涉县", "磁县"],
    },
    "河南": {
        "郑州":["中原区","二七区","金水区"],
        "开封":["龙亭区","鼓楼区","禹王台区"]
    },
    "山西": {
        "太原市":["小店区","迎泽区","万柏林区"],
        "大同市":["城区","矿区","南郊区"]
    },
}
#循环输出所有的省
for shen in dic.keys():
    print(shen)
inpshen = input("请输入身份：")
if inpshen in dic.keys():
    for qu in dic[inpshen].keys():
        print(qu)
else:
    print("输入有误！")
    sys.exit(1)
inpqu = input("请输入区：")
if inpqu in dic[inpshen].keys():
    for xian in dic[inpshen][inpqu]:
        print(xian)
else:
    print("输入有误！")
    sys.exit(1)