#!/usr/bin/env python
# -*- coding:utf-8 -*-

# a= int.__init__(123)
# a = 123
###################################################str 与 bytes转换
# b1 = bytes("你好",encoding="utf-8")
# print(b1)
#
# b2 = bytes("你好",encoding="gbk")
# print(b2)
#
# s1 = str(b1,encoding="utf-8")
# print(s1)
#
# s2 = str(b2,encoding="gbk")
# print(s2)


##########################################list
#########################list创建和转换
# li = list(["abc","def"])
# print(li)
#
# s1 = "你好"
# li = list(s1) #实质上是做了一个for循环
# print(li)
# t1 = (11,22,33,44)
# li2 = list(t1)
# print(li2)

# dic = {
#     "k1":"abc",
#     "k2":"def",
#     "k3":"ghi"
# }
#
# li3 = list(dic)
# print(li3) # 将key转换成list
#
# li4 = list(dic.values())
# print(li4)
#######################list

# li = ["ab","cd","ac","ad"]
# # new_list = li.append()
# s = "hello"
# li.extend(s) #将另一个可迭代的对象扩充到自己内部 str list dic tuple
# print(li)
# print(li.reverse())
# li.insert(1,"hehe")
# print(li)


####################公共功能
# li = ["alex","staryjie","seven","tom"]
# #索引,拿到指定的一个元素（取单个）
# print(li[2])
# #切片,可以取单个，或者连续多个,返回的是一个列表
# print(li[2:3])
# print(li[0:4])

#for
# for i in li:
#     print(i)
# #len
# print(len(li))
#嵌套
# li2 = ["as","de",{"key":{"ke":"ve"},"key1":"value1"}]
# print(li2[2])
# print(li2[2]["key"]["ke"])

#################################################元组
#
# t1 = ("ab","bc","cd","de")
# t2 = tuple((11,22,33,44))
#
# print(t1.count("ab"))
# print(t2.index(11))

######嵌套
# t3 = (11,22,["jie",{"k1":"v1","key":{"kv":"vv","kv2":"vv2"}}])
# t3[2][1]["key2"] = "value2"
# print(t3[2][1])

# dic = {
#     "k1":"v1"
# }
# dic.update({"k2":"v2"})
# dic["k3"] = "v3"
# print(dic)


###################字典

# a = {"k1":123}
# a = dict(k1=123,k2=456)
# print(a)

###list转换成dict

# li = [11,22,33]
# new_dic = dict(enumerate(li))
# print(new_dic)

####字典的方法
# keys \ vaules \ items \ pop \ clear \ get  \ fromkeys

# dic = {
#     "k1":123,
#     "k2":456,
#     "k4":111
# }
#
# ndic = dic.fromkeys(["k1","k2","k3"],"123")
# print(ndic)

# l1 = ["value"]
# d1 = {
#     "k1":l1,
#     "k2":l1,
#     "k3":l1
# }
# print(d1)


# goods = [
#     {"name": "电脑", "price": 1999},
#     {"name": "鼠标", "price": 10},
#     {"name": "游艇", "price": 20},
#     {"name": "美女", "price": 998},
# ]
#
# comm = goods[1]["price"]
# print(comm)


# a = 10
# b = 15
# ret = a if a>b else b
# print(ret)

# import copy
#
# n1 = 123
# print(id(n1))
# n2 = n1
# print(id(n2))
# #浅拷贝
# n2 = copy.copy(n1)
# print(id(n2))
# #深拷贝
# n3 = copy.deepcopy(n1)
# print(id(n3))

# import copy
# n1 = {
#     "k1":"wu",
#     "k2":123,
#     "k3":["alex",456]
# }
# n3 = copy.deepcopy(n1)
# print(id(n1))
# print(id(n3))


# n2 = copy.copy(n1)
# print(id(n1))
# print(id(n2))
# print(n1["k1"])
# print(n2["k1"])


# def sayhello(name):
#     print("Hello,",name)
#
# sayhello("staryjie")

# def sendEmail():
#     print("sending email ...")
#     if "send secussful":
#         return True
#     else:
#         return False
#
# ret = sendEmail()
# if ret == False:
#     print("failed.")
# else:
#     print("secussful!")


# def drive(name="小马哥"):
#     msg = name + "开车去东北"
#     print(msg)
#
# drive("大麻各庄")

# def f1(a):
#     print(a,type(a))
# f1(123)
#
# def f2(**a):
#     print(a,type(a))
# # f2(123)
# f2(k1="123",k2=123,k3=[11,22,33])

# def f1(*args):
#     print(args,type(args))
# li = [11,22,33,44]
# f1(li,55)
# f1(*li,55)

# def f1(**kwargs):
#     print(kwargs,type(kwargs))
# dic = {
#     "k1":123,
#     "k2":456,
#     "k3":789
# }
# f1(key=dic)
# f1(**dic)

# def lens(args):
#     if len(args) > 5:
#         print("长度大于5")
#     else:
#         print("长度小于5")
# lens("hjhgthz")

