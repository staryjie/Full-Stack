#!/usr/bin/env python
# -*- coding:utf-8 -*-
import pickle,json

account_file = open("account.db","rb")
account_dic = json.loads(account_file.read().decode("utf-8"))
#修改余额
account_dic[1000]['balance'] -= 500
account_file.close()
print(account_dic)
# print(account_dic[1000]['balance'])
f = open("account.db","wb")
# f.write(pickle.dumps(account_dic))
# json.dump(account_dic,f)
f.close()
