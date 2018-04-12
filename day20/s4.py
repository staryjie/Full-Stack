#!/usr/local/bin/python3
# -*- coding:utf-8 -*-

import socketserver

# socketserver源码剖析

class MyServer(socketserver.BaseRequestHandler):

    def handle(self):
        # print self.request,self.client_address,self.server
        conn = self.request
        conn.sendall(bytes('欢迎致电 10086，请输入1xxx,0转人工服务.',encoding='utf-8'))
        Flag = True
        while Flag:
            data = conn.recv(1024)
            if data == 'exit':
                Flag = False
            elif data == '0':
                conn.sendall(bytes('通过可能会被录音.balabala一大推',encoding='utf-8'))
            else:
                conn.sendall(bytes('请重新输入.',encoding='utf-8'))


if __name__ == '__main__':
    # socketserver内部就是调用：socket + select + 多线程
    # 创建了一个ip和端口，类名
    # MyServer ===> RequestHandlerClass()
    # obj = self.RequestHandlerClass()
    # obj.handle()
    # ThreadingTCOServer.init() ==> TCPServer.init() ==> BaseTCPServer.init()

    # 1、server对象
    #   self.server_address = ('127.0.0.1',8009)
    #   self.RequestHandlerClass = MyServer
    #   self.socket 创建的socket对象
    server = socketserver.ThreadingTCPServer(('127.0.0.1',8009),MyServer)
    # 2、server对象的serve_forever方法
    #       BaseTCPServer.serve_forever()
    server.serve_forever()