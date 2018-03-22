#!/usr/bin/env python
# -*- coding:utf-8 -*-

# s = {11,22,33,44}
# print(s)

# li = [11,222,11,2]
# s = set(li)
# print(s)


# s = {11,22,33,44,55}
# s.clear()
# print(s)


# s.add("jie")
# print(s)

# s1 = {11,22,33,}
# s2 = {11,33,44,}
# ret = s1.difference_update(s2)
# print(ret)

# s = {11,22,33,44,}
# s.discard(22)
# print(s)
# s.discard(55)
# print(s)


# s1 = {22,"hehe",12,45,87}
# s2 = {22,"hehe"}
# ret = s1.issuperset(s2)
# print(ret)



# ret = s1.isdisjoint(s2)
# print(ret)


# s1.intersection_update(s2)
# print(s1)


# s = {11,22,33,44,55,66}
# s.remove(11)
# print(s)
# s.remove(88)


# ret = s.pop()
# print(ret)
# print(s)

# se = {11,22,33,44}
# be = {11,22,77,55}
# r1 = se.difference(be)
# r2 = be.difference(se)
# print(r1)
# print(r2)
# ret = se.symmetric_difference_update(be)
# print(ret)


s1 = {1,2,3,4,5,}
s2 = {2,4,6,7,10,}
s1.update(s2)
print(s1)


# ret = s1.union(s2)
# print(ret)