#!/usr/local/bin/python3
# -*- coding:utf-8 -*-

import socket

sk = socket.socket()                # 创建socket对象sk
sk.bind(("0.0.0.0",9000,))          # 监听IP和端口
sk.listen(5)                        # 开始监听，只等待5个，超过的不监听
    # print("before")
while True:
    conn,address = sk.accept()      # 接收客户端请求，没有接收到客户端请求的时候会阻塞
    # conn.sendall(bytes("Welcome!Connected!...",encoding="utf-8"))       # 连接成功后，给客户端发送消息
    # print("after")
    while True:
        result = conn.recv(1024)
        msg = str(result,encoding="utf-8")
        print(msg)
        if msg.lower() == "q":
            break
        message = input("请输入回复内容： ")
        conn.sendall(bytes(message, encoding="utf-8"))
        # print("self: 你说的都对。")
    print(conn,address)