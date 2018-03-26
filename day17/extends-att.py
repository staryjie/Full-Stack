#!/usr/local/bin/python3
# -*- coding:utf-8 -*-


'''
# 多继承易错点

class A:
    def bar(self):
        self.f1()

class B(A):
    def f1(self):
        print("B")

class C:
    def f1(self):
        print("C")

class D(C,B):
    pass

class E(B,C):
    pass

d1 = D()
d1.f1()
d1.bar()

e1 = E()
e1.f1()
e1.bar()

b1 = B()
b1.bar()
'''



class Animal:
    def __init__(self):
        print("Animal的构造方法")
        self.ty = "动物"

class Cat(Animal):
    def __init__(self):
        print("Cat的构造方法")
        self.n = "猫"
        # self.ty = "动物"  # 执行父类的构造方法
        super(Cat,self).__init__() # 执行父类的构造方法
        # Animal.__init__(self)  # 执行父类的构造方法

# a = Animal()
c = Cat()
print(c.__dict__)