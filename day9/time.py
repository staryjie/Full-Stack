#!/usr/bin/env python
# -*- coding:utf-8 -*-

import time
import datetime


# print(datetime.date.fromtimestamp(time.time()))

# print(datetime.datetime.now() + datetime.timedelta(3))
# print(datetime.datetime.now() + datetime.timedelta(-3))
# print(datetime.datetime.now() + datetime.timedelta(hours=3))

# print(datetime.datetime.now() + datetime.timedelta(minutes=30))
# time_obj = time.localtime(time.time() - 86400)
# print("%s-%s-%s %s:%s"%(time_obj.tm_year,time_obj.tm_mon,time_obj.tm_mday,time_obj.tm_hour,time_obj.tm_min))

# print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))

# print(time.strptime("2018-2-2","%Y-%m-%d"))

# print(datetime.date.today())

# print(datetime.date.fromtimestamp( time.time() - 86400 ))

# current_time = datetime.datetime.now()
# print(current_time)
# print(current_time.timetuple())
# print(current_time.replace(1993,1,28))

str_to_date = datetime.datetime.strptime("21/11/06 16:30","%d/%m/%y %H:%M")
print(str_to_date)