#!/usr/local/bin/python3
# -*- coding:utf-8 -*-

import socketserver
import subprocess

class MyServer(socketserver.BaseRequestHandler):

    def handle(self):

        # 保证server端一直在监听客户端连接
        while True:
            # 获取客户端连接
            conn = self.request

            # 连接成功后发送消息通知客户端
            conn.sendall(bytes('欢迎使用XXXX系统！',encoding='utf-8'))

            # 保证客户端与服务端连接时一直处于连接状态
            while True:
                # 接收客户端发送的消息
                client_bytes = conn.recv(1024)

                # 判断客户端是否断开连接,如果接收到的消息为空，则断开连接
                if not client_bytes:
                    break

                # 将客户端发送的消息转换成字符串
                client_str= str(client_bytes,encoding='utf-8')
                print(client_str) # 打印消息

                # 解析客户端传过来的字符串，判断客户端需要干什么
                # 如果客户端需要执行shell命令
                func,command = client_str.split('|',1)

                # 执行命令并获取执行结果
                result_str = subprocess.getoutput(command)

                # 将字符串转换成bytes
                result_bytes = bytes(result_str,encoding='utf-8')

                # 为了保证服务端的运行结果完整的传给客户端，设置一个确定字段，客户端可以通过该字段确认是否接收到完整的结果
                info_str = "info|%d" %len(result_bytes)

                # 向客户端发送确认信息
                conn.sendall(bytes(info_str,encoding='utf-8'))

                # 向客户端发送执行结果
                conn.sendall(result_bytes)

            # 关闭连接
            conn.close()

if __name__ == '__main__':
    server = socketserver.ThreadingTCPServer(('127.0.0.1', 8009), MyServer)
    server.serve_forever()