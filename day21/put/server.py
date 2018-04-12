#!/usr/local/bin/python3
# -*- coding:utf-8 -*-

import os,socket

# 文件上传，支持断点续传

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# print(BASE_DIR)
home = os.path.join(BASE_DIR,'file_upload')
# print(home)

ip_port = ('127.0.0.1',9000)

sk = socket.socket()
sk.bind(ip_port)
sk.listen(5)


while True:
    print('waitting ......')
    conn,addr = sk.accept()

    conn.sendall(bytes('Welcome to XXX System !',encoding='utf-8'))

    flag = True
    while flag:
        client_bytes = conn.recv(1024)
        client_str = str(client_bytes,encoding='utf-8')


        func,file_name,file_bytes_size,target_path = client_str.split('|',3)
        file_bytes_size=int(file_bytes_size)
        path=os.path.join(home,file_name)

        has_recevied = 0

        if os.path.exists(path):
            # 2003 代表 该文件已存在
            conn.sendall(bytes('2003',encoding='utf-8'))
            is_continue = str(conn.recv(1024),encoding='utf-8')

            # 2004 代表 要续传
            if is_continue == '2004':
                has_file_size = os.stat(path).st_size
                conn.sendall(bytes(str(has_file_size),encoding='utf-8'))
                has_recevied += has_file_size

                f = open(path,'ab')

            # 不续传
            else:
                f = open(path,'wb')
        else:
            # 2002 代表服务端没有该文件，等待上传
            conn.send(bytes('2002',encoding='utf-8'))
            f = open(path,'wb')

        while has_recevied < file_bytes_size:
            try:
                data = conn.recv(1024)
                if not data:
                    raise Exception
            except  Exception:
                flag = False
                break

            f.write(data)
            has_recevied += len(data)

        print("文件接收完毕！")
        f.close()