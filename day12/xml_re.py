#!/usr/bin/env python
# -*- coding:utf-8 -*-
import requests
from xml.etree import ElementTree as ET

# 1、解析XML

'''
##### 方法一

# 打开文件，读取XML内容
str_xml = open('first.xml', 'r').read()
# 将字符串解析成xml特殊对象，root代指xml文件的根节点
root = ET.XML(str_xml)
'''


##### 方法二

#利用ElementTree.parse将文件直接解析成xml对象

# 直接解析xml文件

tree = ET.parse("first.xml")
# 获取xml文件的根节点,Element类型
root = tree.getroot()


# 2、操作XML
'''
#顶层标签
print(root.tag,root.attrib)
# 遍历XML文档的第二层
for child in root:
    # 第二层节点的标签名称和标签属性
    print(child.tag,child.attrib)
    # 遍历XML文档的第三层
    for i in child:
        # 第二层节点的标签名称和内容
        print(i.tag,i.attrib)
'''


#创建节点，Element类型(可以通过makeelement()方法创建，也可以直接通过ET.Element()创建)
# child = root.makeelement('tt',{'kk':'vv'})
child = ET.Element('tt',{'kk':'vv'})
#将子节点加入到root节点(在内存中，想要写入文件，需要写入)
# rechild = child.makeelement('tt',{'kk':'123123'})
rechild = ET.Element('tt',{'kk':'123123'})
root.append(child)
child.append(rechild)
# tree.write("first.xml",short_empty_elements=False) #short_empty_elements=False 自闭和关闭（当节点没有内容的时候默认自闭合）
tree.write("first.xml")