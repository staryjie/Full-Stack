#!/usr/bin/env python
# -*- coding:utf-8 -*-

#new_dict.keys存在的，在old中添加，old中存在，new中不存在的，old中删除

old_dict = {
    "#1":33,
    "#2":22,
    "#3":100
}

new_dict = {
    "#1":33,
    "#4":22,
    "#7":100
}

old_set = set(old_dict.keys())
new_set = set(new_dict.keys())
#获取哪些需要删除、哪些需要新增，哪些需要更新
del_set = old_set.difference(new_set)
add_set = new_set.difference(old_set)
update_set = old_set.intersection(new_set)
#删除
for key in del_set:
    del old_dict[key]
#新增
for key in add_set:
    old_dict[key] = new_dict[key]
#更新
for key in update_set:
    old_dict[key] = new_dict[key]

print(old_dict)