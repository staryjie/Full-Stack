#!/usr/bin/env python
# -*- coding:utf-8 -*-

######正则表达式
import re

###字符匹配
# ret = re.findall("sta","fghjklstafdastaryjiesfuikostbmnj")
# print(ret)


# ret = re.findall("st.ry","fghjkstaryjiefghjkstbryghj")
# print(ret)

# ret = re.findall("^st","fghjklstghjk")
# res = re.findall("^f.h","fghjklstghjk")
# print(ret)
# print(res)

# ret = re.findall("k.w$","dfghjklw")
# print(ret)

# ret = re.findall("sa?","agbnsaaaaaaaaaaaaddb")
# print(ret)


# ret = re.findall("sa{3}","ghjksaaghjisaaaaaaatghj")
# res = re.findall("sa{1,3}","ghjksaaghjisaaaaaaatghj")
# print(ret)
# print(res)

# ret = re.findall('a[.]d','asabdrseacdsea.d')
# print(ret)

# ret = re.findall("[a-z]","12s121.z")
# print(ret)

# ret = re.findall("[^0-9]","s4567sa890f")
# print(ret)

# ret = re.findall("\d\d","sasas1da32")
# print(ret)

# ret = re.findall("\s","#$%sa^ sa1")
# print(ret)


# ret = re.findall("(ab)","abseabbdgh")
# print(ret)


# ret = re.findall("(\d+)","sasasa123ada3")
# res = re.findall("(\d+?)","sasasa123ada3")
# print(ret)
# print(res)

# ret = re.search(r"a(\d+)","a12345678b").group()
# res = re.search(r"a(\d+?)","a12345678b").group()
# print(ret)
# print(res)
# ret = re.findall(r"a(\d+)","a23b")
# res = re.findall(r"a(\d+?)","a23b")
# ret1 = re.findall(r"a(\d+)b","a23b")
# res1 = re.findall(r"a(\d+?)b","a23b") #最后有b这个字符时，？不起作用，无法取消贪婪匹配
# print(ret)
# print(res)
# print(ret1)
# print(res1)

# ret = re.search(r"(one)(two)xxx\2","qweaonetwoxxxtwo").group()
# print(ret)

# ret = re.findall(r"\babc\b","abc abcfghjklghj")
# res = re.findall("\\babc\\b","abc abcfghjklghj")
# print(ret)
# print(res)

# ret = re.search("com","COM",re.I).group()
# print(ret)

# ret = re.findall(".","a\nbcd")
# res = re.findall(".","a\nbcd",re.S)
# print(ret)
# print(res)

# a = "123abc456"
# ret = re.search("([0-9]*)([a-z]*)([0-9]*)",a).group(0)
# ret1 = re.search("([0-9]*)([a-z]*)([0-9]*)",a).group(1)
# ret2 = re.search("([0-9]*)([a-z]*)([0-9]*)",a).group(2)
# ret3 = re.search("([0-9]*)([a-z]*)([0-9]*)",a).group(3)
# print(ret)
# print(ret1)
# print(ret2)
# print(ret3)

# ret = re.subn("g.t","have","I get A,I got B,I got C")
# print(ret)

# s1 = "staryjie"
# s2 = "@staryjie"
# ret1 = re.match(r"\w+",s1)
# ret2 = re.match(r"\w+",s2)
# if ret1:
#     print(ret1.group())
# else:
#     print("not match")
# if ret2:
#     print(ret2.group())
# else:
#     print("not match")

# s = "%1/2staryjiefghstaryjie"
# ret = re.search(r"\w",s)
# if ret:
#     print(ret.group())
# else:
#     print("not match")


# s = "JGood is a handsome boy, he is cool, clever, and so on"
# regex = re.compile(r"\w*oo\w*")
# ret = regex.findall(s)
# print(ret)

# regex = re.compile(r"\d+")
# ret = regex.split("one1two2three3four4")
# print(ret)

# ret = re.split("[bc]","abcd")
# print(ret)

# source = "1 - 2 * ( (60-30 +(-40.0/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )"
# ret = re.search("\([^()]+\)",source).group()
# print(ret)
# cc = re.search(r"\d+\.?\d*([*/]|\*\*)[\-]?\d+\.?\d*",ret).group()
# result = eval(cc)
# print(result)

# regex = re.compile(r"\d+")
# ret = regex.finditer("12 drump44ers drumming, 11 ... 10 ...")
# for i in ret:
#     print(i.group(),i.span())

# regex = re.compile(r"(([01]?\d?\d|2[0-4]\d|25[0-5])\.){3}([01]?\d?\d|2[0-4]\d|25[0-5])")
# ret = regex.search("212.168.1.1").group()
# print(ret)

# ret = re.findall(r"\\","abc\com")
# print(ret)

# ret = re.findall(r"I\b","I MISS IOU")
# print(ret)