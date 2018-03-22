#!/usr/local/bin/python3
# -*- coding:utf-8 -*-

# 封装

class Stary:

    def fetch(self):
        print(self.backend)

    def add_record(self,record):
        print(self.backend)

    def del_record(self):
        print(self.backend)

# 创建对象1
obj = Stary()
obj.backend = "www.staryjie.com" # 将backend放在内存中
obj.fetch()

# 创建对象2
obj2 = Stary()
obj2.backend = "idea.staryjie.com" # 将backend放在内存中
obj2.fetch()