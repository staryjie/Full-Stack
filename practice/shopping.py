#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 购物车
# 功能要求：
# 要求用户输入总资产，例如：2000
# 显示商品列表，让用户根据序号选择商品，加入购物车
# 购买，如果商品总额大于总资产，提示账户余额不足，否则，购买成功。
# 附加：可充值、某商品移除购物车

goods = [
    {"name": "电脑", "price": 1999},
    {"name": "鼠标", "price": 10},
    {"name": "游艇", "price": 20},
    {"name": "美女", "price": 998},
]
car = {}
asset_all = 0
totalPrice = 0
li = input("请输入您的总资产：")
if li.isdigit():
    asset_all = int(li)
    print("总资产为：",asset_all)
else:
    print("请输入数字！")

while True:
    for k,v in enumerate(goods,1):
        print(k,v["name"],v["price"])

    id = input("请输入商品序号(q/Q结算)：")
    if id.lower() == "q":
        break
    id = int(id)
    if id > 0 and id <= 4:
        if id in car.keys():
            renum = car[id].get("number")
            get = {id:{"name":name,"price":price,"number":renum+1}}
            car.update(get)
        else:
            name = goods[id -1].get("name")
            price = goods[id -1].get("price")
            get = {id:{"name":name,"price":price,"number":1}}
            car.update(get)
    else:
        print("商品不存在！")
    # print(car)
# print(car)
print("结算：")
print("商品\t单价\t数量")
for k,v in car.items():
    print(v["name"],"\t",v["price"],"\t",v["number"])
    p = v["price"] * v["number"]
    totalPrice += p
if totalPrice > asset_all:
    print("余额不足！")
print("商品总价：",totalPrice)
print("账户余额：",(asset_all - totalPrice))