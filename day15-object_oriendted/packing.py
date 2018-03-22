#!/usr/local/bin/python3
# -*- coding:utf-8 -*-

# 封装

class Stary:

    def fetch(self):
        print(self.backend)

    def add_record(self,record):
        print(self.backend)

    def del_record(self):
        print(self.backend)

# 创建对象1
obj = Stary()
# 在对象中封装数据
obj.backend = "www.staryjie.com" # 将backend放在内存中
# 执行方法，执行过程中可以根据self去obj中去取已经封装在里面的数据
obj.fetch()

# 创建对象2
obj2 = Stary()
obj2.backend = "idea.staryjie.com" # 将backend放在内存中
obj2.fetch()

# 相对于函数式编程，函数式编程的函数中必须要带上这个参数，并且在执行的时候必须要将实参传入；而面向对象编程的封装功能之后，只需要封装一遍就可以了，可以重复调用。
# 当进行类似如数据库操作的时候，在连接数据库的配置中，我们必须要知道地址(主机名)、用户名、密码、端口等等信息，如果不用封装功能，那么操作非常不方便。