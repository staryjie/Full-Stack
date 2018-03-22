#!/usr/bin/env python
# -*- coding:utf-8 -*-
import getpass

username = input("Pls enter your username: ").strip()
passwd = getpass.getpass("Pls enter your password: ")

print(username,passwd)