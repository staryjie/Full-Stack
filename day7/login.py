#!/usr/bin/env python
# -*- coding:utf-8 -*-

def login(username,passwd):
    f = open("db", "r", encoding="utf-8")
    for line in f:
        line = line.strip()  # 默认strip()无参数，移除空格或换行，有参数时移除两端指定的元素
        line_list = line.split("$")
        # print(line_list)
        if username == line_list[0] and passwd == line_list[1]:
            print("登陆成功！")
            print("欢迎您,%s!" % username)
            return True
            break
        else:
            print("用户名或密码不正确，登陆失败！")
            return False
def main():
    print("Welcome to XXXX login.")
    username = input("Pls enter your username: ")
    passwd = input("Pls enter your password: ")
    login(username,passwd)

main()