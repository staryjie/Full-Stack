#!/usr/local/bin/python3
# -*- coding:utf-8 -*-

import socket

ip_port = ("127.0.0.1",9000)        # 定义一个元组，包含监听的IP和端口

sk = socket.socket(socket.AF_INET,socket.SOCK_DGRAM,0)  # 使用IPV4和UDP传输
sk.bind(ip_port)

while True:
    data = sk.recv(1024)
    print(data)

sk.close()