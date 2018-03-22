#!/usr/bin/env python
# -*- coding:utf-8 -*-
import requests
from xml.etree import ElementTree as ET

# http://www.cnblogs.com/wupeiqi/articles/5501365.html

'''
num = input("QQ number: ")
url = "http://www.webxml.com.cn//webservices/qqOnlineWebService.asmx/qqCheckOnline?qqCode=" + num
response = requests.get(url)
result = response.text

node = ET.XML(result)

if node.text == "Y":
    print("在线")
else:
    print("离线")
'''

r = requests.get('http://www.webxml.com.cn/WebServices/TrainTimeWebService.asmx/getDetailInfoByTrainCode?TrainCode=K234&UserID=')
result = r.text
root = ET.XML(result)

for node in root.iter('TrainDetailInfo'):
    # print(node.tag)
    # print(node.attrib)
    res = node.find('TrainStation').text
    time  = node.find('StartTime').text
    km = node.find('KM').text
    print(res,time,km)