#-*- coding: utf-8 -*-
import requests
r = requests.get('http://www.baidu.com')
print 'content-->' + r.content  #返回字节形式
print
print 'text-->' + r.text  #返回文本形式
print 'encoding-->' + r.encoding  #根据http头猜测网页编码格式
print
r.encoding = 'utf-8'   #手动指定编码模式
print 'new text-->' + r.text