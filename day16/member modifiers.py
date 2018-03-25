#!/usr/local/bin/python3
# -*- coding:utf-8 -*-

# 成员修饰符
# 1.共有，哪里都可以访问到
# 2.私有，只能通过类中的方法间接访问

class Foo:

    xo = "xo" # 静态字段，类调用

    __ox = "ox" # 私有静态字段，只有类内部的方法才能访问

    def __init__(self):
        self.__name = "staryjie"

    def fetch(self):
        print(Foo.__ox)

    def ptzd(self):
        print(self.__name)

    def __ptff(self):
        print("呵呵，你直接访问访问不到")

    def visit(self):
        print("类中其他的方法才可以调用私有才成员")
        self.__ptff()

    @staticmethod
    def __static():
        print("static method")

    def vist_static(self):
        print("类中其他的方法才可以调用私有才成员")
        self.__static()
        Foo.__static()

    @staticmethod
    def hehe():
        Foo.__static()

    @classmethod
    def __classma(cls):
        print("class method")

    def vis_clas(self):
        self.__classma()

    @classmethod
    def vis_class(cls):
        Foo.__classma()

    @property
    def __texing(self):
        print("texing fangfa")

    def vis_tex(self):
        self.__texing

    @property
    def vis_texing(self):
        self.__texing

class Bar(Foo):

   def fetch(self):
      print(self.__name)

# print(Foo.xo)
# print(Foo.__ox) # 这里访问不到，只能在内部访问
# obj = Foo()
# obj.fetch()


# obj = Foo()
# print(obj.__name) # 私有的普通字段，只能类中的方法才可以访问
# obj.ptzd() # 私有的普通字段，类中的方法能够访问到

# obj = Bar()
# print(obj.__name) # 私有的普通字段，基类也不能直接拿到
# obj.fetch() # 私有的普通字段，基类的内部方法也拿不到

# obj = Foo()
# obj.__ptff() # 私有的普通方法，只有该类中的其他方法才能够调用
# obj.visit()
# obj.__static() # 私有的静态方法，只有该类中的其他方法才能够调用
# obj.vist_static()
# obj.hehe()


# obj = Foo()
# obj.__classma() # 私有的类方法，只有该类中的其他方法才能够调用
# obj.vis_clas()
# obj.vis_class()

obj = Foo()
# obj.__texing # 私有的普通特性，只有该类中的其他方法才能够调用
obj.vis_tex()
obj.vis_texing


# 对于私有修饰符修饰的成员只能在自己类中的方法才能访问，该类的子类也无法访问
# 适用于所有的类成员（字段、方法、特性）