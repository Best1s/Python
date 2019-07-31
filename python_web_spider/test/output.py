#coding: utf-8
'''
from web_spider.UrlManager import UrlManager
#import sys
#print sys.path
c = None
a = UrlManager()
b = a.add_new_url(c)

print b


from test import Test
a = Test()
a.output()
#Test.output()  #错误 why?
'''
class clsTest():
    y=''
    def __init__(self):
        self.y='你'

from test import Test
a = Test()
a.output()
Test.output()

x=clsTest
print(x.y)

x=clsTest()
print(x.y)