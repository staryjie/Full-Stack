#!/usr/bin/python
# -*- coding:utf-8 -*-

'''
该脚本在Python2.7环境中运行
'''

from wsgiref.simple_server import make_server
import random

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

def index():
    # p = ConnectionPool()
    # print(p)
    p = ConnectionPool.get_instance()
    print(p)
    ret = p.get_connection()
    print(ret)
    return "index"

def news():
    return "news"

def RunServer(environ, start_response):
    start_response(status="200 OK",headers=[('Content-Type', 'text/html')])
    url = environ['PATH_INFO']
    print(url)
    if url.endswith("index"):
        return index()
    elif url.endswith("news"):
        return news()
    else:
        return "404"

if __name__ == '__main__':
    httpd = make_server('',8000,RunServer)
    print("Serving HTTP on port 8000...")
    httpd.serve_forever()