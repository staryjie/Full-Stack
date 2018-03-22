#!/usr/local/bin/python3
# -*- coding:utf-8 -*-

# 封装-析构方法

class Foo:

    def __init__(self,bk): # 构造方法，创建对象时自动执行；如果多个对象只需要一样的封装数据，则只需要self参数即可；如果有不同的数据，可以设定多个形参，在实例化对象的时候传入不同的实参即可。
        self.name = "staryjie" # 如果多个对象需要封装的参数一样，只需要在__init__方法中定义一个就可以
        self.favor = bk

    def __del__(self): # 析构方法，在Python方法销毁对象的时候自动执行，不需要人为写这个方法。这里写出来只是为了方便说明。
        pass

obj1 = Foo("xx") # 类名+()会自动执行__init__()方法，即构造方法
print(obj1.favor,obj1.name)
obj2 = Foo("oo")
print(obj2.favor,obj2.name)

# 封装：
    # 使用场景：当同一类方法具有相同参数时，直接封装到对象即可；
    # 在对象中封装，obj.xxx = "ssssss"
    # 在构造方法中封装，__init__(self):
    #                     self.name = "xxx"
    #                     self.favor = "sss"