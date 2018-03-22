#!/usr/bin/env python
# -*- coding:utf-8 -*-

############冒泡排序


# a1 = 123
# a2 = 456
#
# tmp = a1
# a1 = a2
# a2 = tmp
# print(a1,a2)

# li = [11,22,33,4]
# a1 = li[0]
# li[0] = li[1]
# li[1] = a1
# print(li)

# li = [33,2,10,1]
#
# for i in range(len(li) - 1):
#     if li[i] > li[i+1]:
#         temp = li[i]
#         li[i] = li[i+1]
#         li[i+1] = temp
#         # [2, 10, 1, 33]
# print(li)
#
# for i in range(len(li) - 2):
#     if li[i] > li[i+1]:
#         temp = li[i]
#         li[i] = li[i+1]
#         li[i+1] = temp
#         # [2, 10, 1, 33]
# print(li)
#
# for i in range(len(li) - 3):
#     if li[i] > li[i+1]:
#         temp = li[i]
#         li[i] = li[i+1]
#         li[i+1] = temp
#         # [2, 10, 1, 33]
# print(li)

li = [33,2,10,1,21,22,3,5,89]
for j in range(1,len(li)):
    for i in range(len(li) - j):
        if li[i] > li[i+1]:
            temp = li[i]
            li[i] = li[i+1]
            li[i+1] = temp
print(li)