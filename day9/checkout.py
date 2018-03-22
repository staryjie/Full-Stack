#!/usr/bin/env python
# -*- coding:utf-8 -*-
import pickle

f = open("account.db","rb")
# print(f.read())
account_dic = pickle.loads(f.read())
# account_dic = pickle.load(f.read())
# print(account_dic[1000]['balance'])
