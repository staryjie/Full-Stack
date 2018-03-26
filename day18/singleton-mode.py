#!/usr/local/bin/python3
# -*- coding:utf-8 -*-

# 设计模式 -- 单例模式
# 保证一个类仅有一个实例，并提供一个访问它的全局访问点。
# 当所有实例中封装的数据相同时
'''
# 单例模式存在的意义：
    1、当类只能有一个实例而且用户可以从一个众所周知的访问点访问它时。
    2、当这个唯一实例应该是通过子类化可扩展的，并且用户应该无需更改代码就能使用一个扩展的实例时。
'''
import random

# 例子：数据库连接池
class ConnectionPool:

    __instance = None

    def __init__(self):
        self.ip = "96.112.126.2"
        self.port = "3306"
        self.username = "root"
        self.passwoed = "123456"

        # 连接池已经创建的连接
        self.conn_list = [1,2,3,4,5,6,7,8,9,10]

    @staticmethod
    def get_instance():
        if ConnectionPool.__instance:
            return ConnectionPool.__instance
        else:
            # 创建一个对象，并将对象赋值给静态字段
            ConnectionPool.__instance = ConnectionPool()
            return ConnectionPool.__instance

    def get_connection(self):
        '''
        获取连接
        :return:
        '''
        r = random.randrange(1,11)
        msg = "获得连接池中的%s号连接！"%str(r)
        return msg


obj1 = ConnectionPool.get_instance()
print(obj1)
obj2 = ConnectionPool.get_instance()
print(obj2)



# pool = ConnectionPool()

for i in range(10):
    pool = ConnectionPool.get_instance()
    print("去连接池",pool,"中获取一个连接...")
    conn = pool.get_connection()
    print(conn)