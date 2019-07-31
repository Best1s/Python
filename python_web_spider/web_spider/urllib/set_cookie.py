import urllib2

opener = urllib2.build_opener()
opener.addheaders.append(('Cookie','email'+'best.oneself@foxmail.com'))
req = urllib2.Request("http://www.zhihu.com")
response = opener.open(req)
print response.headers
retdata = response.read()
print
#print retdata  #网页内容