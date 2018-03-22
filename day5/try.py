#!/usr/bin/python
# -*- coding: utf-8 -*-
import json,time
import urllib.request
from urllib.parse import urlencode

def main():
    # 配置您申请的APPKey
    appkey = "0ea8e44e4612fb794c29f4979de48ef7"

    # 1.手机归属地查询
    request1(appkey, "GET")


# 手机归属地查询
def request1(appkey, m="GET"):
    flag = True
    while flag:
        phoneNum = input("请输入手机号码(q/Q退出)：")
        if phoneNum.lower() == "q":
            print("退出...")
            break
        # f = open("phoneNumber.log","r")
        # for line in f.readlines():
        #     phoneNum = line
        url = "http://apis.juhe.cn/mobile/get"
        params = {
            "phone": phoneNum,  # 需要查询的手机号码或手机号码前7位
            "key": appkey,  # 应用APPKEY(应用详细页查询)
            "bytes": ""  # 返回数据的格式,xml或json，默认json
        }
        params = urlencode(params)
        if m == "GET":
            f = urllib.request.urlopen("%s?%s" % (url, params))
        else:
            f = urllib.request.urlopen(url, params)

        content = f.read().decode("utf-8")
        # print(content)
        res = json.loads(content)
        if res:
            error_code = res["error_code"]
            if error_code == 0:
                # 成功请求
                print(phoneNum, ":", res["result"]["province"], " ", res["result"]["city"])
                time.sleep(1)
            else:
                print("%s:%s" % (res["error_code"], res["reason"]))
        else:
            print("request api error")
        # f.close()


if __name__ == '__main__':
    main()