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
#定义购物车
shopping_car = {}

#获取用户总资产
asset_all = 0
asset = input("请输入您的总资产：")
if asset.isdigit():
    asset_all = int(asset)
else:
    print("请输入数字!")
while True:
    #循环输出商品列表
    print("序号\t","商品\t","单价\t")
    print("-----------------------")
    for k,v in enumerate(goods,1):
        print(" ",k,"\t",goods[k -1].get("name"),"\t",goods[k -1].get("price"))

    id = input("请输入商品序号(q/Q结算)：")
    if id.lower() == "q":
        break
    if id.isdigit() and int(id) >0 and int(id) <=4:
        id = int(id)
        if id in shopping_car.keys():
            renum = shopping_car[id].get("number")
            get = {id:{"name":name,"price":price,"number":renum+1}}
            shopping_car.update(get)
        else:
            name = goods[id -1].get("name")
            price = goods[id -1].get("price")
            get = {id:{"name":name,"price":price,"number":1}}
            shopping_car.update(get)
    else:
        print("商品不存在！")
    #计算购物车中商品总价
    # 已购商品总价
    totalPrice = 0
    for k, v in shopping_car.items():
        p = (v["price"]) * (v["number"])
        totalPrice += p
    if totalPrice >= asset_all:
        print(totalPrice)
        print("账户余额不足,退出到结算平台！")
        break
#账户余额不足，或者用户选择结算
print("账单结算：")
print("商品\t","单价\t","数量\t")
print("-----------------------")
for k,v in shopping_car.items():
    print(v["name"],"\t",v["price"],"\t",v["number"])
print("购物车商品总价：",totalPrice)
if totalPrice <= asset_all:
    print("账户余额：",asset_all-totalPrice)
else:
    print("账户余额不足以支付，需充值金额：",-(asset_all-totalPrice))