#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = "staryjie"
import time

i = 1
while i <101:
    if i % 2 == 0:
        if i == 50:
            i += 1
            continue
        if i>=60 and i <= 80:
            print("loop", i*i)
            i += 1
            continue
        print("loop",i)
    i +=1