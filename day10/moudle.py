#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os,hashlib

# info = os.stat(r"D:\Axure RP8 Pro.zip")
# print(info)

# info = os.path.dirname(r"D:\software\Axure RP8 Pro.zip")
# print(info)

# str1 = "D:"
# str2 = "home"
# str3 = "index"
# path = os.path.join(str1,str2,str3)
# print(path)


# hash = hashlib.md5(bytes("staryjie",encoding="utf-8"))
# hash.update(bytes("123",encoding="utf-8"))
# print(hash.hexdigest())

# hash = hashlib.sha512()
# hash.update(bytes("123",encoding="utf-8"))
# print(hash.hexdigest())

# import hmac
# h = hmac.new(bytes("staryjie",encoding="utf-8"))
# h.update(bytes("123",encoding="utf-8"))
# print(h.hexdigest())

hash = hashlib.md5(bytes("staryjie",encoding="utf-8"))
hash.update(bytes("123",encoding="utf-8"))
print(hash.hexdigest())