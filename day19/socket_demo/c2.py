#!/usr/local/bin/python3
# -*- coding:utf-8 -*-


import socket

ip_port = ("127.0.0.1",9000)

sk = socket.socket(socket.AF_INET,socket.SOCK_DGRAM,0)

while True:
    inp = input("请输入内容： ").strip()
    if inp == "exit":
        break
    sk.sendto(bytes(inp,encoding="utf-8"),ip_port)

sk.close()