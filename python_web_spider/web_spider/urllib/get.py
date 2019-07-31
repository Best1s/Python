# -*- coding: utf-8 -*-
import urllib
import urllib2
#url = "https://vdazrk-8080-yqtrfy.dev.ide.live/"
url = 'http://xxxx/Public/verify.html'
referer = url
#定义请求头信息
user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
#将user_agent ,referer写入头信息
headers = {'User-Agent':user_agent,'Referer':referer}

#请求
#request = urllib2.Request(url)
#响应
#response = urllib2.urlopen(request)

postdata = {'username':'admin','password':'admin'}
data = urllib.urlencode(postdata)

req = urllib2.Request(url,data,headers) #也可以用req.add_header('User-Agent',user_agent) 写入头信息

response = urllib2.urlopen(req)
html = response.read()
#print html
#with open ('test.png','wb') as f:
#  f.write(html)