# -*- coding: utf-8 -*-
#python 外部参数传递
from sys import argv #内建变量
first = "bbbb"
script,first = argv #参数名script是固定
if first == "" :
  first = 'cccc'
print argv