#!/usr/local/bin/python3
# -*- coding:utf-8 -*-

# 继承-基础

class Animals: # 父类，基类

    def eat(self):
       print(self.name + " 吃")

    def he(self):
        print(self.name + " 喝")

    def piao(self):
        print("aipiao")


class Cat(Animals): # 子类，派生类

    def __init__(self,name):
        self.name = name

    def jiao(self):
        print(self.name + " 喵")

class Uncle:

    def du(self):
        print("赌博")

    def piao(self):
        print("aaaaaaaaa")


class Dog(Animals,Uncle): # 子类，派生类,python中的类可以同时继承多个类

    def __init__(self,name):
        self.name = name

    def jiao(self):
        print(self.name + " 汪")

    def piao(self):
        print("buaipiao")

alex = Dog("alex") # 创建实例
alex.jiao()
alex.eat()
alex.he()
alex.piao() # 当父类喝子类拥有同样的方法时，优先调用子类的方法
alex.du()

tom = Cat("tom")
tom.jiao()
tom.eat()
tom.he()

object = Animals()
object.piao()