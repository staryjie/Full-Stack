#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 1.函数参数、引用
# 2.lambda表达式
# 3.Python内置函数
# 4.递归

# if 1 == 1:
#     name = "staryjie"
# else:
#     name = "jie"
#
# name = "staryjie" if 1 == 1 else "jie"

# def func1(arg):
#     return arg + 1
#
# func2 = lambda arg:arg + 1


# ret = abs(-2)
# print(ret)

# r = all([True,True,False])
# print(r)

# print(bool(0))
# print(bool(None))
# print(bool(""))

# li = [None,"",[],{},(),1]
# ret = any(li)
# print(ret)

# class Foo:
#     def __repr__(self):
#         return "hello"
#
# obj = Foo()
# ret = ascii(obj)
# print(ret)

# ret = hex(29)
# print(ret)

# ret = chr(66)
# print(ret)

# ret = ord('E')
# print(ret)

# def f1():
#     return 123
# r = callable(f1)
# print(r)

# namespace = {"name":"staryjie","data":[25,26,27,28]}
# code = '''def hello():return "name %s,age %d"%(name,data[0])'''
# func = compile(code,"<string>","exec")
# exec(func in namespace)
# result = namespace["hello"]()
# print(result)

# ret = divmod(10,3)
# print(ret)

# a = 1 + 3
# print(a)
# a = "1 + 3"
# print(a)
# a = "1 + 3"
# print(eval(a))

# code = "for i in range(0,3):print(i)"
# exec(code)

#循环可迭代的对象，获取每一个参数，执行函数(参数)
# def f1(arg):
#     if arg > 30:
#         return arg
# li = [11,22,33,44,55]
# ret = filter(f1,li)
# for i in ret:
#     print(i)
# li = [11,22,33,44,55]
# ret = filter(lambda arg:arg>30,li)
# for i in ret:
#     print(i)

# li = [1,2,3,4,5]
# ret = map(lambda arg:arg + 100,li)
# for i in ret:
#     print(i)


# name = input("Pls enter your name: ")
# print("Welcome %s."%(name))


# def func():
#     name = "staryjie"
#     print(locals())
# func()

# print(globals())

# s = "sdfghjkldfdsgbnfghjkadscfghjkdasdfsfdbnm,sacdkn"
# ret = hash(s)
# print(ret)


# li = [11,22,33]
# ret = isinstance(li,list)
# print(ret)


# i = range(3)

# obj = iter([11,22,33,44])
# print(obj)
# print(next(obj))

# li = [11,22,33,66,34]
# print(min(li))

# ret = pow(2,3)
# print(ret)

# f = 3.1554
# ret = round(f)
# print(ret)

# ret = sum([11,22,33])
# print(ret)

# li1 = [11,22,33,44,55]
# li2 = ["a","bb","C","EE"]
# ret = zip(li1,li2)
# for i in ret:
#     print(i)

# li = [11,55,33,77,22,34,67]
# ret = sorted(li)
# print(ret)

char = ["方","123","1","25","65","5678945678","a","B","A","staryjie","_","a钱","孙","李"]
new_char = sorted(char)
print(new_char)
for i in new_char:
    print(bytes(i,encoding="utf-8"))