#!/usr/bin/env python
# -*- coding:utf-8 -*-
import hashlib

def md5(passwd):
    '''
    实现用户密码的MD5加密
    :param passwd: 传入参数，用户输入的密码
    :return: 返回值，返回加密后的密文
    '''
    hash = hashlib.md5(bytes("staryjie",encoding="utf-8"))
    hash.update(bytes(passwd,encoding="utf-8"))
    return hash.hexdigest()

def register(username,passwd):
    '''
    实现用户注册功能，有待完善检查用户名是否已经存在的功能
    :param username:用户名
    :param passwd:用户输入的密码
    :return:返回知否注册成功
    '''
    with open("user.db","a",encoding="utf-8") as f:
        temp = "\n" + username + "|" + md5(passwd)
        f.write(temp)
        f.flush()
        f.close()

def login(username,passwd):
    '''
    实现用户登录
    :param username: 用户名
    :param passwd: 用户输入的密码
    :return: 返回是否登陆成功
    '''
    f = open("user.db", "r", encoding="utf-8")
    for line in f:
        line = line.strip()  # 默认strip()无参数，移除空格或换行，有参数时移除两端指定的元素
        line_list = line.split("|")
        if username == line_list[0] and md5(passwd) == line_list[1]:#用户输入的密码通过与注册时相同的加密算法生成密文与数据库或者文件中的密文对比
            print("登陆成功！")
            print("欢迎您,%s!" % username)
            return True
            break
        else:
            print("用户名或密码不正确，登陆失败！")
            return False
    f.close()

def main():
    '''
    主函数，实现用户登录和注册的选择
    :return:
    '''
    print("1.登陆；2.注册")
    num = input("请输入对应的序号： ")
    if num == "2":
        username = input("用户名：")
        passwd = input("密码：")
        register(username,passwd)
    elif num == "1":
        username = input("用户名：")
        passwd = input("密码：")
        login(username,passwd)
    else:
        print("没有该选项！")

main()