#!/usr/local/bin/python3
# -*- coding:utf-8 -*-

import threading

def do(event):
    print("start")
    event.wait()
    print("execute")

event_obj = threading.Event()

for i in range(10):
    t = threading.Thread(target=do,args=(event_obj,))
    t.start()

event_obj.clear()
inp = input("inp: ")
if inp == "true":
    event_obj.set()