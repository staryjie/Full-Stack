#!/usr/bin/env python
# -*- coding:utf-8 -*-

shopping_cart = []
salary = 2000
goods = [
    {"name": "电脑", "price": 3000},
    {"name": "鼠标", "price": 103},
    {"name": "游艇", "price": 200000},
    {"name": "美女", "price": 998},
]
for i in enumerate(goods):
    index = i[0]  # 序号
    p_list = i[1]  # 商品清单
    p_name_list = p_list.get('name')  # 商品名称列表
    p_price_list = p_list.get('price')  # 商品价格列表
    print(index, ":", p_name_list, p_price_list)

while True:
    choice = input("please enter your choice:").strip()
    if choice.isdigit():  # 如果选择为正整数
        choice = int(choice)  # 输入为数字
        if choice < len(goods) and choice >= 0:  # 选择小于列表长度大于0时
            p_item = goods[choice]  # 加入购物车
            p_name = p_item.get('name')
            p_monery = p_item.get('price')
            if p_monery <= salary:  # 如果商品价格小于等于余额
                shopping_cart.append(p_item)  # 加入购物车
                salary -= p_monery  # 结算
                print("购买的商品\033[32m:%s\033[0m已加入到购物车".center(40, '-') % p_name)
                for p_item in shopping_cart:
                    print(p_name, p_monery)
                    print("您的余额为\033[31m:%s\033[0m元" % salary)
            else:
                print("您的余额不足，差%s元" % (abs(p_monery - salary)))
        else:
            print("没有此件商品!")
    else:
        print("参数错误")
    if choice == "q" or choice == "quit":
        cost = 0
        print("您购买的商品清单如下:")
        for p in shopping_cart:
            print(p_name, p_monery)
            cost += p_monery
        print("\033[32m消费总金额:", cost, "元\033[0m")
        print("\033[32m您的余额为:", salary, "元\033[0m")
        break