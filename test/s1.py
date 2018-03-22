#!/usr/bin/env python
# -*- coding:utf-8 -*-

name = input("Name: ")
age = int(input("Age: "))
job = input("Job: ")
hometown = input("HomeTwon: ")

info = '''
-------- info of %s --------
Name:       %s
Age:        %d
Job:        %s
HomeTown:   %s
---------- end of info -----------
'''%(name,name,age,job,hometown)
print(info)