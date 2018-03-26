#!/usr/local/bin/python3
# -*- coding:utf-8 -*-

# 通过反射导入模块、查找类、创建对象、查找对象中的字段

m = __import__("s2",fromlist=True) # 导入模块
class_name = getattr(m,"Foo") # 模块中找到类
obj = class_name("staryjie") # 根据类创建对象

name = getattr(obj,"name") # 获取对象中的值
print(name)