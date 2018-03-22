#!/usr/bin/env python
# -*- coding:utf-8 -*-
import shutil

# 将文件内容拷贝到另一个文件中
# shutil.copyfileobj(open("file","r"),open("new_file","w"))

# 拷贝文件
# shutil.copyfile("f1.log","f1_copy.log")

# 拷贝权限。内容、组、用户均不变
# shutil.copymode("f1.log","f2.log")

# 仅拷贝状态的信息，包括：mode bits, atime, mtime, flags
# shutil.copystat("f1.log","f2.log")

# 拷贝文件和权限
# shutil.copy("f1.log","f2.log")

import zipfile

# 添加压缩包
# z = zipfile.ZipFile("laxia.zip","a")
# z.write("f2.log")
# z.close()

# 解压

z = zipfile.ZipFile("laxia.zip","r")
z.extractall()
z.close()