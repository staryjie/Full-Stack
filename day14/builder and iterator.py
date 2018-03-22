#!/usr/local/bin/python3
# -*- coding:utf-8 -*-

# 生成器，具有生成一个数据的能力
# 迭代器，具有访问一个能生成数据的对象的能力
# http://www.cnblogs.com/wupeiqi/articles/5484747.html

'''
def f1():
    return "asdf"
    print(123)

ret = f1()
print(ret)
'''

'''
# 关键字yiled,生成器函数

def xrange():
    print("111") # 在生成器函数中print()并不会输出内容
    yield 1      # yiled在运行的时候也不会有数据生成，只有循环生成器函数的对象的时候才会生成数据
    print("222")
    yield 2
    print("333")
    yield 3
    print("444")
    yield 4
    print("555")
    yield 5

# 获取生成器对象，即创建生成器
r = xrange()
print(r) # 执行的时候并不会输出内容，而是一个对象的内存地址

# ret = r.__next__() # 执行生成器函数对象的next()方法的时候会输出内容
# print(ret)

for i in r:   # 循环生成器函数对象的时候也会输出内容，生成器才会生成数据
    print(i)
'''

'''
def xrange_pro(n):
    start = 0
    while True:
        if start > n:
            return
        yield start
        start +=1

obj = xrange_pro(5)

# 迭代器，一个一个往下找数据，不能往回找
n1 = obj.__next__()
n2 = obj.__next__()
n3 = obj.__next__()
n4 = obj.__next__()
n5 = obj.__next__()
n6 = obj.__next__()
print(n1,n2,n3,n4,n5,n6)
'''

li = [11,22,33,44]

for i in li:
    print(i)