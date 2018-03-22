#!/usr/bin/env python
# -*- coding:utf-8 -*-
import requests
from xml.etree import ElementTree as ET

r = requests.get('http://www.webxml.com.cn/WebServices/WeatherWebService.asmx/getWeatherbyCityName?theCityName=杭州')
result = r.text
print(result)