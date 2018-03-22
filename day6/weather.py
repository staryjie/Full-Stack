#!/usr/bin/env python
# -*- coding:utf-8 -*-
import requests        #引用requests模块
cityids = {
    "北京":101010100,
    "海淀":101010200,
    "杭州":101210101
}
flag = True
while flag:
    city = input("请输入城市名称(q/Q退出)：")
    if city.lower() == "q":
        flag = False
        break
    if city in cityids.keys():
        url = "http://www.weather.com.cn/data/cityinfo/" + str(cityids[city]) + ".html"
        r=requests.get(url)
        r.encoding="utf-8"
        # print("城市:"+ r.json()['weatherinfo']['city'],"\n温度:"+r.json()['weatherinfo']['temp'],\
        #      "\n湿度:"+r.json()['weatherinfo']['SD'])
        print(r.json())
    else:
        print("抱歉，暂时不能查到该城市的天气。")