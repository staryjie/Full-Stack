#!/usr/bin/env python
# -*- coding:utf-8 -*-

#随机验证码
####思路：
##########1.生成随机十进制数  65-90
##########2.将数字转换成字母 chr()

import random
# i = random.randrange(65,91)
# c = chr(i)
# print(c)
yzm = ""
for i in range(4):
    num = random.randrange(0,5)
    if num == 2 or num == 4:
        rand2 = random.randrange(0,10)
        yzm = yzm + str(rand2)
    else:
        rand1 = random.randrange(65,91)
        c = chr(rand1)
        yzm += c
print(yzm)