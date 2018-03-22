#!/usr/bin/env python
# -*- coding:utf-8 -*-
import json

#创建用户账户信息
users = {
    "user1":{
        "password":"123456",
        "isLocked":False,
    },
    "user2":{
        "password": "123456",
        "isLocked": False,
    },
    "user3":{
        "password": "123456",
        "isLocked": False,
    }
}
f = open("user.json","wb")
f.write(bytes(json.dumps(users),encoding="utf-8"))
f.close()