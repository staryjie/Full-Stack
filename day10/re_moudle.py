#!/usr/bin/env python
# -*- coding:utf-8 -*-
import re
# re.match()
#从头匹配

# 无分组
'''
origin = "hello staryjie bcd lucy hge tom acd 19"
r = re.match("h\w+",origin)
print(r.group())     # 获取匹配到的所有结果
print(r.groups())    # 获取模型中匹配到的分组结果
print(r.groupdict()) # 获取模型中匹配到的分组结果

# 有分组

# 为何要有分组？提取匹配成功的指定内容（先匹配成功全部正则，再匹配成功的局部内容提取出来）

origin = "hello staryjie bcd lucy hge tom acd 19"
r = re.match("(?P<n1>h)(?P<n2>\w+)",origin)
# r = re.match("h(\w+).*(?P<name>\d)$", origin)
print(r.group())     # 获取匹配到的所有结果
print(r.groups())    # 获取模型中匹配到的分组结果
print(r.groupdict()) # 获取模型中匹配到的分组中所有执行了key的组
'''


# re.search()
# #在整个字符串全局中匹配第一个复合规则的字符串
#
# 无分组
'''
origin = "hello staryjie bcd lucy hge tom acd 19"
r = re.search("a\w+", origin)
print(r.group())     # 获取匹配到的所有结果
print(r.groups())    # 获取模型中匹配到的分组结果
print(r.groupdict()) # 获取模型中匹配到的分组结果

# 有分组
origin = "hello staryjie bcd lucy hge tom acd 19"
r = re.search("a(\w+).*(?P<name>\d)$", origin)
print(r.group())     # 获取匹配到的所有结果
print(r.groups())    # 获取模型中匹配到的分组结果
print(r.groupdict()) # 获取模型中匹配到的分组中所有执行了key的组
'''


# re.findall()
# #将匹配到的所有内容放到一个列表中
#1、
# r = re.findall("\d+\w\d+","a2b3c4d5")
# print(r)

# r = re.findall("","a2b3c4d5")
# print(r)

# r = re.findall("(.+)(\w)*(\d+)","a2b3c45")
# print(r)

# 无分组
# origin = "hello staryjie bcd lucy hge tom acd 19"
# r = re.findall("a\w+",origin)
# print(r)

# 有分组
# origin = "hello alex bcd allow hge accept acd 19"
# r = re.findall("(a\w*)", origin)
# print(r)

# origin = "hello alex bcd allow hge accept acd 19"
# r = re.findall("(a)(\w*)", origin)
# print(r)
'''
# origin = "hello alex bcd allow hge accept acd 19"
# r = re.findall("(a)(\w+(e))(x)", origin)
# print(r)

# r = re.findall(r"(\d+asd)*","1asd2asdp3asd23kif")
# print(r)

# a = "staryjie"
# # r = re.findall("(\w)+",a)
# r = re.findall("(\w){1}",a)
# print(r)

# re.finditer()
# origin = "hello alex bcd alex hge accept acd 19"
# r = re.finditer("(a)(\w+(e))(?P<n1>x)", origin)
# for i in r:
#     print(i)
#     print(i.group())
#     print(i.groups())
#     print(i.groupdict())
'''

# re.split()
# origin = "hello alex bcd alex hge accept acd 19"
# r = re.split("(a\w+)",origin,1)
# print(r)



'''
#s = "1 - 2 * ( (60-30 +(-40.0/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )"
#res1 = (-40.0/5)
#"1 - 2 * ( (60-30 +res1 * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )"
#res2 = (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )
#"1 - 2 * ( (60-30 +res1 * res2) - (-4*3)/ (16-3*2) )"
#res3 = (60-30 +res1 * res2)
#"1 - 2 * ( res3 - (-4*3)/ (16-3*2) )"
#res4 = (-4*3)
#"1 - 2 * ( res3 - res4/ (16-3*2) )"
#res5 = (16-3*2)
#"1 - 2 * ( res3 - res4/ res5 )"
#res6 = ( res3 - res4/ res5 )
#"1 - 2 * res6"

#取出最小的括号里面的内容括号里面没有括号
s = "1 - 2 * ( (60-30 +(-40.0/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )"
# res1 = re.split("(\([^()]+\))",s,1)  #这样切割取到的内容还是包含小括号，在计算之前还需要将两边的()去掉，比较麻烦，改用下面的方法，直接去掉了两边的()
res1 = re.split("\(([^()]+)\)",s,1)
r1 = eval(res1[1]) #eval()可以直接计算出字符串表达式的结果
# print(r1)
s1 = res1[0] + str(r1) + res1[2]
print(s1)
#1 - 2 * ( (60-30 +-8.0 * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )
res2 = re.split("\(([^()]+)\)",s1,1)
r2 = eval(res2[1])
# print(r2)
s2 = res2[0] + str(r2) + res2[2]
print(s2)
#1 - 2 * ( (60-30 +-8.0 * 173545.88095238098) - (-4*3)/ (16-3*2) )
res3 = re.split("\(([^()]+)\)",s2,1)
r3 = eval(res3[1])
# print(r3)
s3 = res3[0] + str(r3) + res3[2]
print(s3)
#1 - 2 * ( -1388337.0476190478 - (-4*3)/ (16-3*2) )
res4 = re.split("\(([^()]+)\)",s3,1)
r4 = eval(res4[1])
# print(r4)
s4 = res4[0] + str(r4) + res4[2]
print(s4)
#1 - 2 * ( -1388337.0476190478 - -12/ (16-3*2) )
res5 = re.split("\(([^()]+)\)",s4,1)
r5 = eval(res5[1])
# print(r5)
s5 = res5[0] + str(r5) + res5[2]
print(s5)
#1 - 2 * ( -1388337.0476190478 - -12/ 10 )
res6 = re.split("\(([^()]+)\)",s5,1)
r6 = eval(res6[1])
print(r6)
s6 = res6[0] + str(r6) + res6[2]
print(s6)
#1 - 2 * -1388335.8476190479
r7 = eval(s6)
print(r7)
# print(eval(s))
'''
'''
s = "1 - 2 * ( (60-30 +(-40.0/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )"

# def f1(arg):
#     '''
#     pass
#     return r
#
#
# while True:
#     result = re.split("\(([^()]+)\)",s,1)
#     if len(result) == 3:
#         before = result[0]
#         content = result[1]
#         after = result[2]
#         r = f1(content)
#         new_str = before + str(r) + after
#         s = new_str
#     else:
#         r = f1(s)
#         print(r)
#         break
# '''

# re.sub()
s = "123abc"
res,num = re.subn("\d+","res",s)
print(res,num)