#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
import logging

#logging模块写多文件日志
# http://www.cnblogs.com/wupeiqi/articles/5501365.html

# 创建文件
file1 = logging.FileHandler("11.log","a")
# 创建格式
fmt = logging.Formatter(fmt="%(asctime)s - %(name)s - %(levelname)s - %(module)s: %(message)s")
# 文件应用格式
file1.setFormatter(fmt)


# 创建文件
file2 = logging.FileHandler("12.log","a")
# 创建格式
fmt = logging.Formatter(fmt="%(asctime)s - %(name)s - %(levelname)s - %(module)s: %(message)s")
# 文件应用格式
file2.setFormatter(fmt)


logger1 = logging.Logger("s1",level=logging.ERROR)
logger1.addHandler(file1)
logger1.addHandler(file2)


# 写日志
logger1.critical("1111")