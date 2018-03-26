#!/usr/local/bin/python3
# -*- coding:utf-8 -*-

# 异常处理

'''
# 常见的异常：

AttributeError 试图访问一个对象没有的树形，比如foo.x，但是foo没有属性x
IOError 输入/输出异常；基本上是无法打开文件
ImportError 无法引入模块或包；基本上是路径问题或名称错误
IndentationError 语法错误（的子类） ；代码没有正确对齐
IndexError 下标索引超出序列边界，比如当x只有三个元素，却试图访问x[5]
KeyError 试图访问字典里不存在的键
KeyboardInterrupt Ctrl+C被按下
NameError 使用一个还未被赋予对象的变量
SyntaxError Python代码非法，代码不能编译(个人认为这是语法错误，写错了）
TypeError 传入对象类型与要求的不符合
UnboundLocalError 试图访问一个还未被设置的局部变量，基本上是由于另有一个同名的全局变量，
导致你以为正在访问它
ValueError 传入一个调用者不期望的值，即使值的类型是正确的
'''

'''
# 更多的异常：

ArithmeticError
AssertionError
AttributeError
BaseException
BufferError
BytesWarning
DeprecationWarning
EnvironmentError
EOFError
Exception
FloatingPointError
FutureWarning
GeneratorExit
ImportError
ImportWarning
IndentationError
IndexError
IOError
KeyboardInterrupt
KeyError
LookupError
MemoryError
NameError
NotImplementedError
OSError
OverflowError
PendingDeprecationWarning
ReferenceError
RuntimeError
RuntimeWarning
StandardError
StopIteration
SyntaxError
SyntaxWarning
SystemError
SystemExit
TabError
TypeError
UnboundLocalError
UnicodeDecodeError
UnicodeEncodeError
UnicodeError
UnicodeTranslateError
UnicodeWarning
UserWarning
ValueError
Warning
ZeroDivisionError
'''

# 不同的异常需要用不同的异常来捕捉，不知道会有什么异常的话可以使用Exception来捕捉
'''
inp = input("请输入内容： ")
try:
    num = int(inp)
    print(num)
except ValueError as e:
    print("数据类型转换失败！",e)
'''


'''
li = [1,2,3,4,5,6,7,8,9,0]
inp = input("请输入内容")
try:
    inp = int(inp)
    print(li[inp])
except IndexError as inde:
    print("没有该索引的值！",inde)
except KeyError as ke:
    print("键错误！",ke)
except ValueError as ve:
    print("值错误！",ve)
except Exception as e:
    print("错误！",e)
'''
# 当我们需要收集程序运行过程中产生的吧不同的错误来进行分析时，可以把一些有意义的错误放在Exception前面，最后在放Exception

'''
dic = {
    "k1":123,
    "k2":456,
    "k3":789,
}

key = input("请输入key值：")
try:
    print(dic[key])
except KeyError as e:
    print("key值错误！",e)
'''


# 完整的异常处理代码块
'''
try:
    # 主代码块
    pass
except KeyError as ke:
    # 异常时执行该代码
    pass
except ValueError as ve:
    pass
except IndexError as ie:
    pass
except Exception as e:
    pass
else:
    # 主代码块执行完成，执行该代码块
    pass
finally:
    # 无论是否异常，都要执行的代码块
    pass
'''

# 主动触发异常

# try:
#     print("123")
#     raise Exception("something wrong!") # 通过raise主动创建一个异常对象，封装了错误信息
# except Exception as e: # e 也是一个对象，但是在e的类中有一个__str__方法，调用print和str方法的时候，就自动调用__str__方法，将对象转换成字符串输出
#     print(e)

class Foo:

    def __init__(self,arg):
        self.xo = arg

    def __str__(self): # 将对象转换成字符串
        return self.xo

obj = Foo("staryjie")
print(obj)