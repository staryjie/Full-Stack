#!/usr/bin/env python
# -*- coding:utf-8 -*-
import json

f = open("user.json","rb+")
users = json.load(f)

# for user in users.keys():
#     print(user)
count = 0
while True:
    if count == 3:
        users[username]["isLocked"] = True
        print("Error up to 3 times, the account is locked!")
        break
    username = input("Pls enter your username: ")
    password = input("Pls enter your password: ")
    if username in users.keys():
        if users[username]["isLocked"] != True:
            passwd = users[username]["password"]
        else:
            print("Account has been locked!")
            break
        if password == passwd:
            print("Welcome %s !"%username)
            break
        else:
            print("The password is error!")
            count += 1
            print(count)
    else:
        print("No such username!")
f.close()