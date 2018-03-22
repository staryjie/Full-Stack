#!/usr/bin/env python
# -*- coding:utf-8 -*-
import requests,json

response = requests.get('http://www.weather.com.cn/adat/sk/101010500.html')
response.encoding = "utf-8"
result = response.text
# print(result,type(result))
dic = json.loads(result)
print(dic)
