#!/usr/local/bin/python3
# -*- coding:utf-8 -*-

import socket

sk = socket.socket()
sk.connect(("127.0.0.1",9001))
while True:
    msg = input("请输入内容：")
    sk.sendall(bytes(msg,encoding='utf-8'))

    msg_bytes = sk.recv(1024)
    msg = str(msg_bytes,encoding="utf-8")
    print(msg)