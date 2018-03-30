#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
import socket

ip_port = ('127.0.0.1',9000)
sk = socket.socket()
sk.connect(ip_port)
sk.settimeout(5)

while True:
    data_bytes = sk.recv(1024)
    data = str(data_bytes,encoding="utf-8")
    print('receive:',data)
    inp = input('please input:')
    sk.sendall(bytes(inp,encoding="utf-8"))
    if inp == 'exit':
        break

sk.close()