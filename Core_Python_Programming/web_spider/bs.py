#-*- coding: utf-8 -*-
import re
from bs4 import element
from bs4 import BeautifulSoup #bs4库将任何读入的html文件或字符串都转换为utf-8编码
#soup = BeautifulSoup(html_str,'lxml',from_encoding='utf-8')  #创建BeautifulSoup 对象
#soup = BeautifulSoup(open('index.html'),'lxml')   #lxml 第三方html解析库  python内置 是html.parser
soup = BeautifulSoup(open('1.xml'),"html.parser")
#for i  in soup.strings:
#  print i
#for sibling in soup.i.next_siblings: #通过.next_sibling和.previous_siblings 属性可对当前兄弟节点迭代输出
#  print repr(sibling)
for i in  soup.find('i').children:
  #print i
  print i.find_next(i.name)
  
  '''
  if str(i.name):
  #if isinstance(i,element.Tag): #使用isinstance过滤掉空行内容
  #  pass
    #print i.string
    for ci in i.find(str(i.name)):
      print ci.string
  else:
    print i.string
  #for skup in i.find_all('skup'):
  #  print skup.i.strings
例如：选取class="nav"的div下的ul下的li中所有的文本数据。
//div[@class="nav"]/ul/li/text()
  '''
print soup.originalEncoding