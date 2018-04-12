#!/usr/local/bin/python3
# -*- coding:utf-8 -*-

import socket
import sys
import re
import os

ip_port = ('127.0.0.1',9000)

sk = socket.socket()
sk.connect(ip_port)

print(str(sk.recv(1024),encoding='utf-8'))


def bar(num=1,sum=100):

    rate = float(num) / float(sum)
    rate_num = int(rate * 100)
    temp = '\r%d %%' %(rate_num,)
    sys.stdout.write(temp)
    sys.stdout.flush()


while True:
    inp = input("Pls input: ").strip()
    func,file_path = inp.split('|',1)
    local_path,target_path = re.split("\s*",file_path,1)
    file_bytes_size = os.stat(local_path).st_size
    file_name = os.path.basename(local_path)

    post_info = "post|%s|%s|%s" %(file_name,file_bytes_size,target_path)
    sk.sendall(bytes(post_info,encoding='utf-8'))

    result_exist = str(sk.recv(1024),encoding='utf-8')

    has_sent = 0
    if result_exist == '2003':
        inp = input("文件已存在，是否续传？(y/Y): ").strip()
        if inp.lower() == 'y':
            sk.sendall(bytes('2004',encoding='utf-8'))
            # server端给客户端已经传了多少
            result_continue_pos = str(sk.recv(1024),encoding='utf-8')
            print(result_continue_pos)
            has_sent = int(result_continue_pos)
        else:
            sk.sendall(bytes('2005',encoding='utf-8'))

    file_obj = open(local_path,'rb')
    file_obj.seek(has_sent)

    while has_sent < file_bytes_size:
        data = file_obj.read(1024)
        sk.sendall(data)
        has_sent += len(data)
        bar(has_sent,file_bytes_size)
    file_obj.close()
    print('上传成功！')