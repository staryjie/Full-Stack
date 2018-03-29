#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
import datetime
import random
import pickle
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from lib import modles
from config import settings
from lib.modles import *


def create_crouse(admin_obj):
    teacher_list = pickle.load(open(settings.TEACHER_DB_DIR, "rb"))
    for num,item in enumerate(teacher_list,1):
        print(num,item.name,item.age,item.create_time,item.create_admin.username)

    crouse_list = []

    while True:
        name = input("请输入课程名称(q/Q退出): ")
        if name.lower() == "q":
            break
        cost = input("请输入课时费...: ")
        num = input("请选择任课老师(输入对应序号)...: ")

        obj = modles.Crouse(name,cost,teacher_list[int(num) - 1],admin_obj)
        crouse_list.append(obj)
        print("课程%s创建成功！"%name)

    if os.path.exists(settings.COURSE_DB_DIR):
        exists_list = pickle.load(open(settings.COURSE_DB_DIR,"rb"))
        crouse_list.extend(exists_list)
    pickle.dump(crouse_list,open(settings.COURSE_DB_DIR,"wb"))

def create_teacher(admin_obj):
    teacher_list = []
    while True:
        teacher_name = input("请输入教师姓名(q/Q退出)： ")
        if teacher_name.lower() == 'q':
            break
        teacher_age = input("请输入教师年龄： ")

        obj = modles.Teacher(teacher_name,teacher_age,admin_obj)
        print("教师%s创建成功！"%teacher_name)
        teacher_list.append(obj)

    if os.path.exists(settings.TEACHER_DB_DIR):
        exists_list = pickle.load(open(settings.TEACHER_DB_DIR,"rb"))
        teacher_list.extend(exists_list)
    pickle.dump(teacher_list,open(settings.TEACHER_DB_DIR,"wb"))

def login(user,pwd):
    if os.path.exists(os.path.join(settings.BASE_ADMIN_DIR,user)):
        admin_obj = pickle.load(open(os.path.join(settings.BASE_ADMIN_DIR,user), 'rb'))
        if admin_obj.login(user, pwd):
            print("登陆成功！")
            # print(admin_obj.username, admin_obj.password)
            while True:
                sel = input("1.创建教师；2.创建课程；3.退出；\n >>>")
                if sel == '1':
                    create_teacher(admin_obj)
                elif sel == '2':
                    create_crouse(admin_obj)
                elif sel == '3':
                    break

        else:
            # print("登陆失败！")
            return 1
    else:
        # print("用户不存在！")
        return 0

def register(user,pwd):
    admin_obj = modles.Admin()
    admin_obj.register(user, pwd)
    print("管理员%s注册成功！" % user)


def main():

    inp = input("1.管理员登陆；2.管理员注册；3.退出系统; \n >>>")
    if inp == '3':
        sys.exit()
    user = input("请输入用户名： ")
    pwd = input("请输入密码： ")

    if inp == '1':
        ret = login(user,pwd)
        if ret == 1:
            print("密码错误！")
        elif ret == 0:
            yep = input("用户不存在！是否前往注册管理员(y/n)? ")
            if yep.lower() == "y":
                register(user,pwd)
            elif yep.lower() == "n":
                return
    elif inp == '2':
        register(user,pwd)

if __name__ == '__main__':
    main()