#!/usr/local/bin/python3
# -*- coding:utf-8 -*-

import socketserver

# r = socketserver.ThreadingTCPServer()
# r.server_forever()

'''
+------------+
| BaseServer |
+------------+
|
v
+-----------+        +------------------+
| TCPServer |------->| UnixStreamServer |
+-----------+        +------------------+
|
v
+-----------+        +--------------------+
| UDPServer |------->| UnixDatagramServer |
+-----------+        +--------------------+
'''

class A:

    def f1(self):
        print("A的f1")

    def f2(self):
        print("A的f2")

class B:
    def f4(self):
        print("B的f4")
        self.f1()

class C(B):
    def f0(self):
        print("C的f0")
        self.f4()

    def f1(self):
        print("C的f1")

    def f2(self):
        print("C的f2")

class D(A,C):
    pass

d = D()
d.f0()