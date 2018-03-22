#!/usr/bin/env python
# -*- coding:utf-8 -*-

import  configparser

# # 获取所有节点
# con = configparser.ConfigParser()
# con.read("ini",encoding="utf-8")
# # cond对象的read()功能，打开文件读取内容，放进内容
# result = con.sections()
# print(result)
#
# # con对象的options()功能，从内存中寻找所有的[xxx]
# ret = con.options("staryjie")
# print(ret)


# 获取指定节点下所有的键值对
# con = configparser.ConfigParser()
# con.read("ini",encoding="utf-8")
# ret = con.items("staryjie")
# print(ret)


# 获取指定节点下所有的建
# con = configparser.ConfigParser()
# con.read("ini",encoding="utf-8")
# ret = con.options("staryjie")
# print(ret)

# 获取指定节点下指定key的值
# con = configparser.ConfigParser()
# con.read("ini",encoding="utf-8")
# v = con.get("staryjie","age")
# print(v)


# # 检查、删除、添加节点
# con = configparser.ConfigParser()
# con.read("ini",encoding="utf-8")
#
# #检查
# hsa_sec = con.has_section("staryjie")
# print(hsa_sec)
#
# #添加节点
# con.add_section("tom")
# con.write(open("ini","w"))
#
# #删除节点
# con.remove_section("lucy")
# con.write(open("ini","w"))


# 检查、删除、设置指定组内的键值对

con = configparser.ConfigParser()
con.read("ini",encoding="utf-8")

#检查
has_opt = con.has_option("staryjie","age")
print(has_opt)

# 删除
con.remove_option("lucy","gender")
con.write(open("ini","w"))

# 设置
con.set("lucy","gender","women")
con.write(open("ini","w"))