#-*- coding: utf-8 -*-
from bs4 import element
from bs4 import BeautifulSoup #bs4库将任何读入的html文件或字符串都转换为utf-8编码
#soup = BeautifulSoup(html_str,'lxml',from_encoding='utf-8')  #创建BeautifulSoup 对象
#soup = BeautifulSoup(open('index.html'),'lxml')   #lxml 第三方html解析库  python内置 是html.parser
soup = BeautifulSoup(open('index.html'),"html.parser",from_encoding='utf-8')
print soup.prettify() #方法prettfy()来实现格式化输出
print  '-'*(90)
#通过标记名查找
print soup.select('title') #直接查找title标记
print soup.select('html head title') #逐层查找title标记
print soup.select('a')
print soup.select('head > title')  #查找head下的title标记
print soup.select('p #link1')  #查找p下的 id='link' 标记
print soup.select('#link1 ~ .sister')  #查找兄弟节点  查找id=‘link1’之后class=‘sisiter’ 的所有兄弟标记
print soup.select('#link1 + .sister')  #查找兄弟节点  查找id=‘link1’之后class=‘sisiter’ 的兄弟标记
print  '-'*(90)
#通过CSS 类名查找
print soup.select('.sister')
print soup.select('[class ~= sister]')
print  '-'*(90)
#通过tag的 id 查找
print soup.select("#link1")
print soup.select('a  #link2')
print  '-'*(90)
#通过是否存在某个属性查找
print soup.select('a[href]')
print  '-'*(90)
#通过某个属性值查找
print soup.select('a[href="http://example.com/elsie"]')
print soup.select('a[href^="*http://example.com/"]')
print soup.select('a[href$="tillie*"]')
print soup.select('a[href*="*.com/el"]')