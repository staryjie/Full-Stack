#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
import threading

# lock = threading.Lock()     #Lock对象
# lock.acquire()
# print("here...1")
# lock.acquire()   #产生了死锁
# print("here...2")
# lock.release()
# print("here...3")
# lock.release()
# print("here...end")

lock = threading.RLock() #Lock对象
lock.acquire()
print("here...1")
lock.acquire() #在同一线程内，程序不会堵塞。
print("here...2")
lock.release()
print("here...3")
lock.release()
print("here...4")