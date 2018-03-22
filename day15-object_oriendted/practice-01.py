#!/usr/local/bin/python3
# -*- coding:utf-8 -*-

'''
在终端输出如下信息:
小明，10岁，男，上山去砍柴
小明，10岁，男，开车去东北
小明，10岁，男，最爱大保健
老李，90岁，男，上山去砍柴
老李，90岁，男，开车去东北
老李，90岁，男，最爱大保健

'''

# 函数式方法实现

def kanchai(name,age,gender):
    print("%s,%s岁,%s,上山去砍柴"%(name,age,gender))

def qudongbei(name,age,gender):
    print("%s,%s岁,%s,开车去东北"%(name,age,gender))

def dabaojian(name,age,gender):
    print("%s,%s岁,%s,最爱大保健"%(name,age,gender))

kanchai("小明","10","男")
qudongbei("小明","10","男")
dabaojian("小明","10","男")

kanchai("老李","90","男")
qudongbei("老李","90","男")
dabaojian("老李","90","男")


# 面向对象方法实现

class Something:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender

    def kanchai(self):
        print("%s,%s岁,%s,上山去砍柴" % (self.name, self.age, self.gender))

    def qudongbei(self):
        print("%s,%s岁,%s,开车去东北" % (self.name, self.age, self.gender))

    def dabaojian(self):
        print("%s,%s岁,%s,最爱大保健" % (self.name, self.age, self.gender))

xiaoming = Something("小明","10","男")
xiaoming.kanchai()
xiaoming.qudongbei()
xiaoming.dabaojian()

laoli = Something("老李","90","男")
laoli.kanchai()
laoli.qudongbei()
laoli.dabaojian()