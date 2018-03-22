#!/usr/bin/env python
# -*- coding:utf-8 -*-
import subprocess

# ret = subprocess.check_output("ipconfig")
# res = ret.decode("gbk")
# print(res)

'''
obj = subprocess.Popen(["python"],stdin=subprocess.PIPE,stderr=subprocess.PIPE,stdout=subprocess.PIPE,universal_newlines=True)
obj.stdin.write("print(1)\n")
obj.stdin.write("print(2)")
obj.stdin.close()

cmd_out = obj.stdout.read()
obj.stdout.close()
cmd_error = obj.stderr.read()
obj.stderr.close()

print(cmd_out)
print(cmd_error)
'''

