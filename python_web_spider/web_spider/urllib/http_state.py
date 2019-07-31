#-*- coding: utf-8 -*-
import urllib2
try:
  response = urllib2.urlopen('http://www.baidu.com',timeout=2)
  isa = response.geturl()
  print isa
  print response
  print response.getcode()
except urllib2.URLError as e:
  print e.code
  if hasattr(e,'code'):
    print e.code
'''
状态码 由 response.getcode() 获取
'''