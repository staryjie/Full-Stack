#!/usr/local/bin/python3
# -*- coding:utf-8 -*-

import socket

sk1 = socket.socket()
sk1.bind(("127.0.0.1",9000))
sk1.listen(5)

sk2 = socket.socket()
sk2.bind(("127.0.0.1",9001))
sk2.listen(5)

sk3 = socket.socket()
sk3.bind(("127.0.0.1",9002))
sk3.listen(5)


# while True:
#     conn,address = sk.accept()
#     while True:
#         msg_bytes = conn.recv(1024)
#         msg = str(msg_bytes,encoding="utf-8")
#         print(msg)
#         conn.sendall(bytes(msg + " OK",encoding="utf-8"))
# conn.close()

inputs = [sk1,sk2,sk3]

import select
# select对监听的个数有限制，最多1024个
# poll取消了监听个数的限制，还是采用for循环实现
# epoll，不采用for循环，采用异步的方式实现
while True:
    # 内部自动监听sk1、sk2和sk3两个对象，一旦某个句柄发生变化
    # 如果有人连接sk1
    # r_list = [sk1]
    r_list,w_list,e_list = select.select(inputs,[],inputs,1) # 每次执行到这的时候停一秒，如果没有连接，跳出该次循环
    # select.select(inputs,[],inputs,1) ==> select.select(发生变化的,永远不,发生错误的,等待时间)
    # print(r_list)
    for sk in r_list:
        # print(sk)
        conn,address = sk.accept()
        conn.sendall(bytes("hello",encoding="utf-8"))


    # 谁出错了就将谁移走
    for sk in e_list:
        inputs.remove(sk)