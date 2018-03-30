#!/usr/local/bin/python3
# -*- coding:utf-8 -*-

import socket

ip_port = ("127.0.0.1",9000)

sk = socket.socket()
sk.bind(ip_port)
sk.listen(5)

while True:
    conn,address = sk.accept()
    conn.sendall(bytes("欢迎登陆staryjie-ftp!",encoding="utf-8"))
    f = open("new.jpg","wb")

    # 先接收文件大小
    file_size = str(conn.recv(1024),encoding="utf-8")
    conn.sendall(bytes("确认文件大小，开始接收文件...",encoding="utf-8"))
    print(file_size)
    total_size = int(file_size)

    recv_size = 0

    # 开始接收文件
    while True:
        if total_size == recv_size: # 当文件大小和之前接收到的文件大小相等时终止
            break
        data = conn.recv(1024)
        f.write(data)
        recv_size += len(data)  # 每次接收完数据写入之后累计接收文件的总大小

    f.close()

sk.close()