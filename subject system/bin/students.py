#!/usr/local/bin/python3
# -*- coding:utf-8 -*-

import os,sys

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from lib import modles
from lib.modles import *
from config import settings

def course_info(students_obj):
    for item in students_obj.crouse_list:
        print(item.crouse_name, item.cost, item.teacher.name)

def select_course(students_obj):
    course_list = pickle.load(open(settings.COURSE_DB_DIR,"rb"))
    for num,item in enumerate(course_list,1):
        print(num,item.crouse_name,item.cost,item.teacher.name)

    while True:
        num = input("选课(输入序号q/Q退出): ")
        if num.lower() == "q":
            break
        select_course_obj = course_list[int(num) - 1]
        if select_course_obj not in students_obj.crouse_list:
            students_obj.crouse_list.append(select_course_obj)

    pickle.dump(students_obj,open(os.path.join(settings.BASE_STUDENTS_DIR,students_obj.username),"wb"))


def login(user,pwd):
    if os.path.exists(os.path.join(settings.BASE_STUDENTS_DIR,user)):
        students_obj = pickle.load(open(os.path.join(settings.BASE_STUDENTS_DIR,user), 'rb'))
        if students_obj.login(user, pwd):
            print("登陆成功！")
            # print(admin_obj.username, admin_obj.password)
            while True:
                sel = input("1.选课；2.上课；3.查看课程信息；4.退出；\n >>>")
                if sel == '1':
                    select_course(students_obj)
                elif sel == '2':
                    pass
                elif sel == '3':
                    course_info(students_obj)
                elif sel == '4':
                    break

        else:
            # print("登陆失败！")
            return 1
    else:
        # print("用户不存在！")
        return 0


def register(user,pwd):
    students_obj = modles.Students()
    students_obj.register(user,pwd)
    print("学生%s注册成功！"%user)


def main():
    inp = input("1.登录；2.注册；3.退出；\n >>> ")
    if inp == '3':
        sys.exit()
    user = input("请输入用户名： ")
    pwd = input("请输入密码： ")
    if inp == '1':
        login(user,pwd)
    elif inp == '2':
        register(user, pwd)

if __name__ == '__main__':
    main()