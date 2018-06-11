#!/usr/local/bin/python3
# -*- coding:utf-8 -*-

import threading
import time

def worker(num):
    '''
    threading worker function
    :param num:
    :return:
    '''
    time.sleep(1)
    print("Thread %d" %num)
    return

for i in range(10):
    t = threading.Thread(target=worker,args=(i,),name="t.%d" %i)
    t.start()