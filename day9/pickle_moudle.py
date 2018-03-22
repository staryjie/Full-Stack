#!/usr/bin/env python
# -*- coding:utf-8 -*-
import pickle,json

account = {
    1000:{
        "name":"staryjie",
        "email:":"staryjie123@163.com",
        "balance":15000,
        "phone_number":18989474962,
        "bank_acc":{
            "ICBC":6228655342122,
            "ABC":45678987654567,
            "CBC":67890987654566
        }
    },
    1001:{
        "name":"staryjie",
        "email:":"someone@163.com",
        "balance":2000,
        "phone_number":17686543219,
        "bank_acc":{
            "ICBC":6228621342122,
        }
    },
}
f = open("account.db","wb")
# f.write(pickle.dumps(account))
bytes(json.dumps(account),encoding="utf-8")
# pickle.dump(account,f)
f.close()