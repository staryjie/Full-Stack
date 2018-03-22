# #!/usr/bin/env python
# # -*- coding:utf-8 -*-
#
# # 查看某个类所包含的方法
# # tmp = "hello"
# # print(dir(tmp))
# # help(type(tmp))
#
# # name = input("Pls enter your name: ")
# # print("It's good to see you," + name)
# # print(len(name))
#
# # s = "HelloWorld"
# # print(s.swapcase())
#
#
# # s = "beautiful girl"
# # print(s.istitle())
# # print(s.title())
#
#
# # s = "give me five"
# # print(s.zfill(15))
#
#
# # s = "staryjie"
# # for item in s:
# #     if item == "t":
# #         break
# #     print(item)
#
# # i = 123
# # print(i.bit_length())
#
# # name = "staryjie"
# # print(name[0])
#
# # name_list = ["staryjie","lily","tom","bob"]
# # print(name_list[0])
# # print(name_list[0:2])
# # print(name_list[2:len(name_list)])
#
# # name_list = ["staryjie","lily","tom","bob"]
# # for name in name_list:
# #     print(name)
#
#
# # name_list = ["staryjie","lily","tom","bob"]
# # name_list.append("jack")
# # print(name_list)
#
# # name_list = ["staryjie","lily","tom","bob","bob","bob"]
# # print(name_list.count("bob"))
#
#
# # name_list = ["staryjie","lily","tom","bob"]
# # del name_list[1:3]
# # print(name_list)
#
#
# # name_tuple = ("staryjie","lily","tom","bob")
# # for item in name_tuple:
# #     print(item)
#
#
# # user_info = {
# #     "name":"staryjie",
# #     "age":25,
# #     "gender":"M"
# # }
# #
# # for k,v in user_info.items():
# #     print(k,v)
#
#
# # print(user_info.keys())
# # print(user_info.values())
# # print(user_info.items())
# #
# # #
# # # for item in user_info:
# # #     print(item)
#
#
# # user_info = {
# #     "name":"staryjie",
# #     "age":25,
# #     "gender":"M"
# # }
# # # print(user_info)
# # test = {
# #     "a1":123,
# #     "a2":456
# # }
# # del test["a1"]
# # print(test)
#
#
# # user_info.update(test)
# # print(user_info)
#
#
#
#
#
#
#
# # if "salary" not in user_info.keys():
# #     user_info.setdefault("salary",25000)
# # print(user_info.get("salary"))
#
#
#
#
#
#
# # user_info.popitem()
# # print(user_info)
#
#
#
#
#
# # for item in user_info.items():
# #     print(item)
#
# # print(user_info.has_key("age"))
#
#
#
#
#
# # print(user_info)
# # user_info.clear()
# # print(user_info)
#
#
# # li = ["11","12","13","14","15","16"]
# # for item in li:
# #     if item == "14":
# #         break
# #     print(item)
#
#
#
# li = ["手机","电脑","鼠标垫","游艇"]
# for k,v in enumerate(li):
#     print(k,v)
# inp = input("请输入商品编号： ")
# print(li[int(inp)])
#
# # for i in range(10,1,-2):
# #     print(i)
#
#
# # li = ["staryjie","lily"]
# #
# # l = len(li)
# # for i in range(0,l):
# #     print(li[i])
#
#
# #有如下值集合 [11,22,33,44,55,66,77,88,99,90...]，将所有大于 66 的值保存至字典的第一个key中，将小于 66 的值保存至第二个key的值中。
# li = [11,22,33,44,55,66,77,88,99,90]
# dic = {
#     "k1":[],
#     "k2":[]
# }
# for i in li:
#     if i <= 66:
#         dic["k1"].append(i)
#     else:
#         dic["k2"].append(i)
# print(dic)


# li = ["alec", " aric", "Alex", "Tony", "rain"]
# tu = ("alec", " aric", "Alex", "Tony", "rain")
# dic = {'k1': "alex", 'k2': ' aric',  "k3": "Alex", "k4": "Tony"}
# #定义三个与之对应的空列表或字典
# li_new = []
# tu_new = []
# dic_new = {}
# #处理li列表
# for i in li:
#     #去除空格
#     ret = i.strip()
#     li_new.append(ret)
#     #判断每个元素是否满足条件，满足就输出
#     if ((ret.startswith("a") or ret.startswith("A")) and ret.endswith("c")):
#         print(ret)
# print("li_new = " ,li_new)
# #处理tu列表
# for i in tu:
#     # 去除空格
#     ret = i.strip()
#     tu_new.append(ret)
#     # 判断每个元素是否满足条件，满足就输出
#     if ((ret.startswith("a") or ret.startswith("A")) and ret.endswith("c")):
#         print(ret)
# print("tu_new = ",tu_new)
# #处理dic
# for k,v in dic.items():
#     # 去除空格
#     kret = k.strip()
#     vret = v.strip()
#     dic_new[kret] = vret
#     # 判断每个key是否满足条件，满足就输出
#     if ((kret.startswith("a") or kret.startswith("A")) and kret.endswith("c")):
#         print(kret)
#     # 判断每个value是否满足条件，满足就输出
#     if ((vret.startswith("a") or vret.startswith("A")) and vret.endswith("c")):
#         print(vret)
# print("dic_new = ",dic_new)

goods = [
    {"name": "电脑", "price": 1999},
    {"name": "鼠标", "price": 10},
    {"name": "游艇", "price": 20},
    {"name": "美女", "price": 998},
]