#!/usr/bin/env python
# -*- coding:utf-8 -*-
#####   文件操作

#一、打开文件
#二、操作文件
#三、关闭文件

# open(文件名,模式,编码)
# f = open("ha.log","r")
# data = f.read()
# print(data)
# f.close()

#只读模式
# f = open("ha.log","r")
# data = f.read()
# f.close()

#只写模式
# f = open("ha1.log","w")
# f.write(" test test")
# f.close()

# f = open("text-x.log","x")
# f.write(" test test")
# f.close()

#追加模式,不可读
# f = open("ha.log","a")
# f.write("666")
# f.close()

# f = open("ha.log","r")
# data = f.read()
# f.close()
# print(type(data))
# b = bytes(data,encoding="utf-8")
# print(b)

#以字节的方式打开
# 只读，rb
# f = open("ha.log","rb")
# data = f.read()
# print(data)
# print(type(data))
# f.close()

#只写,写入的内容需要转换成字节
# f = open("ha.log","wb")
# f.write(bytes("中国",encoding="utf-8"))
# f.close()

'''
普通打开方式：
    Python内部读取到字节，并自动(默认utf-8编码)转换成字符串

字节打开方式：
    读取的时候：
        以字节的方法读取文件内容，不进行转换，直接输出读取到的字节
    写入的时候：
        因为python是以字节的方式打开的，所以写入的数据必须也是字节类型，
        所以我们需要通过bytes()将字符串转换成字节。

'''

# "+",能读能写

# r+，读取到的是文件中的内容，写入之后不会覆盖之前已有的内容
# f = open("ha.log","r+",encoding="utf-8")
# print(f.tell())  #获取指针位置
# data  = f.read()
# print(data)
# f.write("中国人")
# f.seek(0) #设置指针位置
# data  = f.read()
# print(data)
# print(f.tell())
# f.close()


#w+,先清空内容，写入后，将指针放到开头之后可以读
# f = open("ha.log","w+",encoding="utf-8")
# f.write("中国人") #写完之后，指针在最后面，需要将指针放到开头才能继续读取
# f.seek(0)
# data = f.read()
# print(data)
# f.close()

#x+，与w+一样，只是文件存在的时候会报错


#a+，在打开文件的同时，将指针放在最后，如果需要读取，需要将指针放在最前
f = open("ha.log","a+",encoding="utf-8")
f.seek(0)
data = f.read()
print(data)
f.write("staryjie")
f.seek(0)
data = f.read()
print(data)
f.close()