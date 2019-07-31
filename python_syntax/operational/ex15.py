#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sys import argv
script,filename = argv
txt = open(filename,"a+")

line1 = "This is a test!"

print txt.read()
txt.write("\n")
txt.write(line1)
#txt.close()
print " second read!"
#txt.seek(0)  #seek() 方法用于移动文件读取指针到指定位置。
print txt.read()
