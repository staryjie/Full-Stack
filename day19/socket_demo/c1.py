#!/usr/local/bin/python3
# -*- coding:utf-8 -*-

import socket

obj = socket.socket()               # 创建socket对象
obj.connect(('127.0.0.1',9000,))    # 连接指定的IP和端口
print("Waitting for connection...")
while True:
    msg_re = input("请输入要发送的内容(q/Q退出)：")
    if msg_re.lower() == "q":
        obj.sendall(bytes(msg_re,encoding="utf-8"))
        break
    else:
        obj.sendall(bytes(msg_re,encoding="utf-8"))
        result = obj.recv(1024)  # 接收最多1024字节的消息,服务端没有返回消息的时候会阻塞
        msg = str(result, encoding="utf-8")
        print(msg)

obj.close()