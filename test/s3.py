#!/usr/bin/env python
# -*- coding:utf-8 -*-

name = input("Pls enter your username: ")
sex = input("Pls enter your sex(f|m):")
age = int(input("Pls enter your age: "))

if sex == "f":
    if age > 28:
        print("I LOVE YOU,%s!"%name)
    else:
        print("I LOVE YOU,%s!"%name)
else:
    print("YOU OUT!")