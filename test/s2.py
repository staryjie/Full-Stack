#!/usr/bin/env python
# -*- coding:utf-8 -*-

name = "staryjie"
passwd = "staryjie123"

username = input("Pls enter your username: ")
password = input("Pls enter your password: ")

if name == username and passwd == password:
    print("Welcome %s !"%name)
else:
    print("username or password error!")