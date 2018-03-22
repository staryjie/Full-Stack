#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys,time

for i in range(101):
    sys.stdout.write('\r')
    sys.stdout.write("正在下载：%s%% [%s#]"%(int(i),int(i) * '#'))
    sys.stdout.flush()
    time.sleep(0.3)