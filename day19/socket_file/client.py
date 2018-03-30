#!/usr/local/bin/python3
# -*- coding:utf-8 -*-

import socket
import os

ip_port = ("127.0.0.1",9000)

sk = socket.socket()
sk.connect(ip_port)

ret_bytes = sk.recv(1024)
ret_str = str(ret_bytes,encoding="utf-8")
print(ret_str)

# 发送文件大小，用于服务端判断文件是否已经上传完成
size = os.stat('f.jpg').st_size
sk.sendall(bytes(str(size),encoding="utf-8"))

msg_bytes = sk.recv(1024) # 接收服务端确认信息，确认之后开始发送文件
msg_str = str(msg_bytes,encoding="utf-8")
print(msg_str)

# 开始上传文件
with open("f.jpg","rb") as f:

    for line in f:
        sk.sendall(line)

sk.close()


# 关于粘包问题
# 在文件发送的过程中需要依赖系统的缓冲区，由缓冲区负责发送文件，缓冲区并不是一个干净的环境
# 但是在这里我们不知道缓冲区是什么时候，怎么发送文件的，可能缓冲区发送的数据可能会和别的数据一起发送过去，造成服务端接收的数据并不是客户端发送的


# 解决粘包问题
# 确认包，在客户端发送完文件大小之后，不直接发送文件，写一个recv，等待服务端返回确认接收信息，确认之后开始发送文件