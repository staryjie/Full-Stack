#!/usr/local/bin/python3
# -*- coding:utf-8 -*-

import json,sys
import urllib.request
from urllib.parse import urlencode


def main():
    if len(sys.argv) < 2:
        print("请在命令行传入手机号码文件！")
        sys.exit("参数错误！")
    # 配置您申请的APPKey
    appkey = "0ea8e44e4612fb794c29f4979de48ef7"

    # 1.手机归属地查询
    request1(appkey, "GET")


# 手机归属地查询
def request1(appkey, m="GET"):
    with open(sys.argv[1], 'r+') as f1:
        with open("result.txt", "w+") as f2:
            for line in f1.readlines():
                phoneNum = line
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
                        msg = str(phoneNum).strip() + ": " + str(res["result"]["province"]).strip() + " " + str(
                            res["result"]["city"]).strip() + "\n"
                        # print(phoneNum, ":", res["result"]["province"], " ", res["result"]["city"])
                        f2.write(msg)
                        f2.flush()
                        # print(msg)
                    else:
                        print("%s:%s" % (res["error_code"], res["reason"]))
                else:
                    print("request api error")
    print("查询完成，结果请查看当前目录下的result.txt")


if __name__ == '__main__':
    main()