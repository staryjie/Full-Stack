#!/usr/local/bin/python3
# -*- coding:utf-8 -*-

import datetime
import random
import pickle
import os
import sys

from config import settings

class Teacher:
    '''
    封装教师相关信息
    '''

    def __init__(self,name,age,admin):
        self.name = name
        self.age = age
        self.__assets = 0
        self.create_time = datetime.datetime.strptime("21/11/06 16:30","%d/%m/%y %H:%M")
        self.create_admin = admin

    def gain(self,cost):
        '''
        资产增加
        :param cost:
        :return:
        '''
        self.__assets += cost

    def decrease(self,cost):
        '''
        资产减少
        :param cost:
        :return:
        '''
        self.__assets -= cost

class Crouse:
    '''
    课程相关信息
    '''
    def __init__(self,crouse_name,cost,teacher_obj,admin):
        self.crouse_name = crouse_name
        self.cost = cost
        self.teacher = teacher_obj
        self.create_time = datetime.datetime.strptime("21/11/06 16:30", "%d/%m/%y %H:%M")
        self.create_admin = admin

    def have_lesson(self):
        '''
        上课
        :return:
        '''
        self.teacher.gain(self.cost)

class Admin:

    def __init__(self):
        self.username = None
        self.password = None

    def login(self,user,pwd):
        '''
        管理员登陆
        :param user:
        :param pwd:
        :return:
        '''
        if user == self.username and pwd == self.password:
            return True
        else:
            return False

    def register(self,user,pwd):
        '''
        管理员注册
        :param user:
        :param pwd:
        :return:
        '''
        self.username = user
        self.password = pwd

        # settings.BASE_ADMIN_DIR + self.username
        path = os.path.join(settings.BASE_ADMIN_DIR,self.username)

        pickle.dump(self,open(path,'xb'))

class Students:
    '''
    学生相关信息
    '''

    def __init__(self):
        self.username = None
        self.password = None

        self.crouse_list = []
        self.study_dict = {}

    def select_course(self,course_obj):
        '''
        选课
        :param course_obj:
        :return:
        '''

    def register(self,user,pwd):
        '''
        学生注册
        :param user:
        :param pwd:
        :return:
        '''
        self.username = user
        self.password = pwd

        path = os.path.join(settings.BASE_STUDENTS_DIR,self.username)

        pickle.dump(self,open(path,"xb"))

    def login(self,user,pwd):
        '''
        学生登录
        :param user:
        :param pwd:
        :return:
        '''
        if user == self.username and pwd == self.password:
            return True
        else:
            return False