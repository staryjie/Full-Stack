#!/usr/local/bin/python3
# -*- coding:utf-8 -*-

import threading
import time

globals_num = 0

lock = threading.RLock()

def Func():
    lock.acquire() # 获得锁
    global globals_num
    globals_num += 1
    time.sleep(1)
    print(globals_num)
    lock.release() #释放锁

for i in range(10):
    t = threading.Thread(target=Func)
    t.start()