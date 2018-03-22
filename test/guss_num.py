#!/usr/bin/env python
# -*- coding:utf-8 -*-
import random

num = random.randrange(1,11)
count = 0
while True:
    guss_num = int(input("Pls enter a num(1-10): "))
    if guss_num == 15:
        print(num)
    if count == 3:
        print("three time over!")
        break
    if guss_num == num:
        print("bingo!")
        break
    elif guss_num > num:
        print("try smaller!")
    else:
        print("try bigger!")
    count += 1