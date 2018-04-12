#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
import socket,time

# 定义一个客户端要连接的服务端的ip和端口
ip_port = ('127.0.0.1',8009)

# 创建socket对象
sk = socket.socket()

# socket对象连接服务端
sk.connect(ip_port)
print("客户端启动中...")
time.sleep(1)
print("服务器连接成功！")

# 客户端连接成功后，打印服务端发送过来的确认连接消息
print(str(sk.recv(1024),encoding='utf-8'))

# 保持与服务端的连接
while True:
    # 获取用户输入，根据输入判断要告诉服务端接下来的操作是要做什么
    # 比如 cmd|who  通过cmd表示要执行shell命令，通过'|'分割，'who'表示要执行的命令
    inp = input("Pls input: ").strip()

    # 开始判断用户输入
    if inp.startswith('cmd'):
        sk.sendall(bytes(inp,encoding='utf-8'))
        basic_info_bytes = sk.recv(1024)
        # print(str(basic_info_bytes,encoding='utf-8'))

        # 获取服务端发送过来的结果确认值
        result_length = int(str(basic_info_bytes,encoding='utf-8').split('|')[1])

        # print(result_length)

        # 根据确认字段，开始接收命令执行结果
        # 已接收的内容的长度
        has_received_len = 0

        # 接收的内容
        content_bytes = bytes()

        # 为了防止服务端传过来的数据不止1024，所以开始循环接收，直到跟服务端发送过来的确认字段长度一样
        while has_received_len < result_length:
            fetch_bytes = sk.recv(1024)
            has_received_len += len(fetch_bytes)

            content_bytes += fetch_bytes
        # 接收完毕，将bytes转换成str
        cmd_result = str(content_bytes,encoding='utf-8')
        print(cmd_result)

sk.close()
