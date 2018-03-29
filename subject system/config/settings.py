#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
BASE_ADMIN_DIR = os.path.join(BASE_DIR,"db","admin")
BASE_STUDENTS_DIR = os.path.join(BASE_DIR,"db","students")

TEACHER_DB_DIR =os.path.join(BASE_DIR,"db","teacher_list")
COURSE_DB_DIR =os.path.join(BASE_DIR, "db", "course_list")


log_path = "xxx" # 指定日志目录