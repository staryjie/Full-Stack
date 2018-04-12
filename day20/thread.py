#!/usr/local/bin/python3
# -*- coding:utf-8 -*-

import threading,time

# 多线程

def process(arg):
    time.sleep(1)
    print(arg)

# process(1)

# for i in range(11):
#     process(i)


for i in range(11):
    t = threading.Thread(target=process,args=(i,))
    t.start()