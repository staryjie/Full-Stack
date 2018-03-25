#!/usr/local/bin/python3
# -*- coding:utf-8 -*-

# 类的特殊成员

# 1. __init__     构造方法，类实例化对象的时候自动执行
# 2. __del__      析构方法，Python解释器销毁对象之前自动执行，一般不需要手动去写这个方法
# 3. __call__     特殊方法，将一个类实例化的对象变成一个可调用对象，其实就是通过"对象()"的格式来调用__call__方法）
# 4. __getitem__  特殊方法，让对象通过"[参数]"的方式将参数传入到__getitem__方法中，类似字典的使用方法
# 5. __setitem__  特殊方法，让对象通过"对象名[key = value]"的方式将键值对传入__setitem__方法，类似字典的创建
# 6. __delitem__  特殊方法，让对象通过"del 对象名['key']"的方式将将key传入__delitem__方法，类似字典的del dic['key']

'''
# __call__方法说明：

class Foo:

    def __init__(self):
        print("init ")

    def __call__(self, *args, **kwargs):
        print("call")
        return 1

# r = Foo()
# r() # 在没有__call__方法之前会报错，TypeError: 'Foo' object is not callable
# 在类实例化对象之后，在对象后加()其实就是执行__call__方法

r = Foo()()
print(r)

# 举个例子说明__call__方法的作用：

class Person:

    def __init__(self,name,gender):
        self.name = name
        self.gender = gender

    def __call__(self, *friend): # 定义特殊函数__call__ 将Person类实例化的对象变成可调用对象（可以在对象后直接加上()来执行，其实就是通过"对象()"的格式来调用__call__方法）
        print("My name is %s."%self.name)
        print("My friend is %s."%friend)

p = Person("staryjie","male") # 实例化Person()类的对象
p("Tom") # 通过"对象()"的格式来调用__call__方法）
'''


# dic = dict(k1=123,k2=456)
# print(dic["k1"])
# dic["k1"] = 789
# print(dic["k1"])


'''
# __getitem__方法说明：

'''


class Foo:

    def __init__(self):
        print("init ")

    def __call__(self, *args, **kwargs):
        print("call")
        return 1

    def __getitem__(self, item):
        print(item)

r = Foo()
r()
r["k1"]

# 自己写个例子方便理解

class Example:

    def __init__(self):
        pass

    def __getitem__(self, item):
        if item == "hello":
            return "world"
        elif item == "give me":
            return "five"
        else:
            return "can you try again?"

    def __setitem__(self, key, value):
        print(key,value)

    def __delitem__(self, key):
        print(key + " has been deleted!")

e = Example()
# ret1 = e["hello"]
# ret2 = e["give me"]
# ret3 = e["haha"]
# print(ret1)
# print(ret2)
# print(ret3)

e["12345"] = "上山打老虎"
del e["key123"]

