#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# __author__:cjx
import sys

china_map = {
    '山东': {
        '青岛': ['四方', '黄岛', '崂山', '李沧', '城阳'],
        '济南': ['历城', '槐荫', '高新', '长青', '章丘'],
        '烟台': ['龙口', '莱山', '牟平', '蓬莱', '招远']
    },
    '江苏': {
        '苏州': ['沧浪', '相城', '平江', '吴中', '昆山'],
        '南京': ['白下', '秦淮', '浦口', '栖霞', '江宁'],
        '无锡': ['崇安', '南长', '北塘', '锡山', '江阴']
    },
    '浙江': {
        '杭州': ['西湖', '江干', '下城', '上城', '滨江'],
        '宁波': ['海曙', '江东', '江北', '镇海', '余姚'],
        '温州': ['鹿城', '龙湾', '乐清', '瑞安', '永嘉']
    },
    '安徽': {
        '合肥': ['蜀山', '庐阳', '包河', '经开', '新站'],
        '芜湖': ['镜湖', '鸠江', '无为', '三山', '南陵'],
        '蚌埠': ['蚌山', '龙子湖', '淮上', '怀远', '固镇']
    },
    '广东': {
        '深圳': ['罗湖', '福田', '南山', '宝安', '布吉'],
        '广州': ['天河', '珠海', '越秀', '白云', '黄埔'],
        '东莞': ['莞城', '长安', '虎门', '万江', '大朗']
    }
}

province_list = list(china_map.keys())    # 用list函数把字典的key生成列表并赋值

while True:            # 最外层死循环
    print(' 省 '.center(50, '*'))            # 利用字符串类型的方法打印提示符
    for i,p in enumerate(province_list):    # 利用enumerate函数取出元素对应的索引及元素
        print(i+1,p)            # 由于列表的索引是从0开始计数的，因此要 +1 展示更好合适
    p_id = input('请输入要查看的省名称编号,退出请输入 q：')
    if p_id.isdigit():
        p_id = int(p_id)       # 把输入的编号转换成int型
        if p_id > 0 and p_id <= len(province_list):   # 判断是否输入的是有效的
            pro_name = province_list[p_id - 1]       # 用用户输入的编号取出对应的城市名，索引从0开始的，因此要 -1 才是对应的值
            city_list = list(china_map[pro_name].keys())      # 根据用户输入，获取二级菜单列表
            while True:                # 进入二级菜单死循环
                print(' 市 '.center(50, '*'))
                for i, c in enumerate(city_list):
                    print(i+1, c)
                c_id = input('请输入你要查看的市名称编号，返回上一级请输入 b,退出请输入 q ：')
                if c_id.isdigit():
                    c_id = int(c_id)
                    if 0 < c_id <= len(city_list):
                        city_name = city_list[c_id-1]
                        town_list = china_map[pro_name][city_name]
                        while True:
                            print(' 县 '.center(50, '*'))
                            for i, t in enumerate(town_list):
                                print(i+1, t)
                            b_or_q = input('已经到最后一层，返回上一级请输入 b,退出请输入 q ：')
                            if b_or_q == 'b':
                                break          # 跳出循环，即回到第一级循环
                            elif b_or_q == 'q':
                                exit(0)
                            else:
                                print('输入有误！')
                    else:
                        print('您输入的ID %d 不存在！' % c_id)
                elif c_id == 'b':
                    break              # 跳出循环，即回到第二级循环
                elif c_id == 'q':
                    sys.exit('正在退出 ......')
                else:
                    print('无效输入')

        else:
            print('您输入的ID %d 不存在！' % p_id)     # 如果输入的不是正确的范围提示输入的不存在
    elif p_id == 'q':
        exit()
    else:
        print('无法识别您的输入')       # 如果输入的不是可以转换成数字的字符就提示非法输入