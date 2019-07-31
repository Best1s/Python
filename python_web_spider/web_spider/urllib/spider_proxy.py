#-*- coding: utf-8 -*-
import urllib2
proxy = urllib2.ProxyHandler({'http':'127.0.0.1:80'})
#opener = urllib2.build_opener([proxy,])  #全局会使用这个代理
urllib2.install_opener(opener) #全局会使用这个代理  不使用则 opener = urllib2.build_opener(proxy,)
response = urllib2.urlopen('http://www.zhihu.com')
print response.code
print response.read()