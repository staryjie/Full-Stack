#!/usr/local/bin/python3
# -*- coding:utf-8 -*-

# Python中一切皆对象，类也属于对象，类默认是由type创建的

# 类可以创建对象，类默认是由type创建的，也可以由__mataclass__ = xxx 指定由xxx来创建

# 写个例子：

class MyType(type):

    def __init__(self,what,bases=None,dict=None):
        super(MyType,self).__init__(what,bases,dict)

    def __call__(self, *args, **kwargs):
        obj = self.__new__(self,*args,**kwargs)

        self.__init__(obj)

class Foo(object):              # Foo = MyType(...)
    __mataclass__ = MyType      # 指定Foo类由MyType创建

    def __init__(self,name):
        self.name = name

    def __new__(cls, *args, **kwargs):
        return object.__new__(cls,*args,**kwargs)

# 第一阶段：解释器从上到下执行代码创建Foo类
# 第二阶段：通过Foo类创建obj对象

obj = Foo("staryjie")