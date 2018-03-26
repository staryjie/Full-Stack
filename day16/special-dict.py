#!/usr/local/bin/python3
# -*- coding:utf-8 -*-

# 特殊类成员 - dict
# 作用： 自定义Form框架的时候可以用到

class Foo:
    '''
    类的注释
    '''

    xxoo = "xxoo"

    def __init__(self):
        self.name = "staryjie"

    def __getitem__(self, item):
        print(item)

    def __setitem__(self, key, value):
        print(key,value)

    def __delitem__(self, key):
        print(key)

r = Foo()
print(r.__dict__)
print(Foo.__dict__)
# {'__module__': '__main__', '__doc__': '\n    类的注释\n    ', '__init__': <function Foo.__init__ at 0x1041141e0>, '__dict__': <attribute '__dict__' of 'Foo' objects>, '__weakref__': <attribute '__weakref__' of 'Foo' objects>}
print(Foo.__doc__)
