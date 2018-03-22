
#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys
import time

# print(sys.argv)

# while True:
#     for i in range(0,11):
#         print(i)
#         if i == 4:
#             sys.exit(2)

# print(sys.platform)

#进度条
for i in range(100):
    sys.stdout.write(">")
    sys.stdout.flush()
    time.sleep(0.3)