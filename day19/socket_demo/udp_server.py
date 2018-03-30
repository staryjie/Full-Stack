#!/usr/local/bin/python3
# -*- coding:utf-8 -*-

import socket

ip_port = ("127.0.0.1",9000)

sk = socket.socket(socket.AF_INET,socket.SOCK_DGRAM,0)
sk.bind(ip_port)

while True:
    data,(host,port) = sk.recvfrom(1024)
    print(data,host,port)
    sk.sendto(bytes("OK",encoding="utf-8"),(host,port))

sk.close()