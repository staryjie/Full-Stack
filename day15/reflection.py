#!/usr/local/bin/python3
# -*- coding:utf-8 -*-

# 反射
# 通过字符串的形式，导入模块
# 通过字符串的形式，去模块中寻址指定函数、全局变量，并执行

'''
import comments

ret = comments.f1()
print(ret)
'''

# 根据用户输入的内容，导入对应的模块
inp = input("请输入模块名： ")
print(inp,type(inp))
dd = __import__(inp,fromlist=True) # 递归查找，模块嵌套在目录中的时候可以使用

ret = dd.f1()
print(ret)


# 小结： 反射就是根据字符串的形式去某个模块中寻找东西,设置东西，删除东西，见getattr_s1.py
# 以字符串的形式去指定的对象中操作其成员
# __import__
# getattr : 反射