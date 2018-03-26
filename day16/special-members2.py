#!/usr/local/bin/python3
# -*- coding:utf-8 -*-

# 类的特殊成员

# 7. __getslice__
# 8. __setitem__
# 9. __delslice__

# 这三个方法是Python2中的，在Python3中分别对应__getitem__\__setitem__\__delitem__


# 列表的切片
# r = list([11,22,33,44,55,66,77,88,99])
# print(r[1:5:2])       r[1:5:2] __getsklce , python2中的方法，在Python3中还是调用__getitem__，将[1：5：2]封装成一个对象之后传给item

class Foo:

    def __init__(self):
        pass

    def __getitem__(self, item):
        print(item,type(item),"__getitem__")

    def __setitem__(self, key, value):
        print(key,value,type(key),type(value),"__setitem__")

    def __delitem__(self, key):
        print(key,type(key),"__delitem__")

obj = Foo()
obj[1:5:2] # 由此可见，在Python3中，在执行__getitem__方法的时候是将[1:5:2]封装成一个对象，这个对象属于slice类，然后传给item变量的。
# slice(1, 5, 2) <class 'slice'> __getitem__
obj[1:3] = [11,22,33]
# slice(1, 3, None) [11, 22, 33] <class 'slice'> <class 'list'> __setitem__  # __setslice__
del obj[1:3]
# slice(1, 3, None) <class 'slice'> __delitem__  # __delslice__


