#-*- coding: utf-8 -*-
import urllib2
import socket
socket.setdefaulttimeout(10) #10s timeout
urllib2.socket.setdefaulttimeout(10) #另一种方式

#urlopen函数提供对Timeout的设置  eg:
#import urllib2
request = urllib2.Request('http://www.zhihu.com')
response = urllib2.urlopen(request,timeout=0.1)
html = response.read()
print html