#!/usr/local/bin/python3
# -*- coding:utf-8 -*-

class Person:

    def __init__(self,name,age,weight):
        self.name = name
        self.age = age
        self.weight = weight
        print("%s现在的体重为%s" % (self.name, self.weight))

    def eat(self):
        print("%s岁的%s吃了一斤橘子。"%(self.age,self.name))
        self.weight = self.weight + 1
        print("%s现在的体重为%s" % (self.name, self.weight))

    def run(self):
        print("%s岁的%s跑了10公里的路程。" % (self.age, self.name))
        self.weight = self.weight - 2
        print("%s现在的体重为%s" % (self.name, self.weight))

    def zhaoduixiang(self):
        print("%s在%s岁的时候找了一个对象。" % (self.name, self.age))

    def jianshen(self):
        self.weight = self.weight - 1
        print("%s现在的体重为%s"%(self.name,self.weight))


tom = Person("Tom","22",200)
tom.eat()
tom.run()
tom.jianshen()
tom.zhaoduixiang()