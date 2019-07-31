#-*- coding: utf-8 -*-
from lxml import etree
html_str='''
<html><head><title>The Dormouse's story</title></head>
<body>
  <p class="title"><b>The Dormouse's story</b></p>
  <p class="story">Once upon a time there were three little sisters; and their names were
  <a href="http://example.com/elsie" class="sister" id='link1'><!--Elsieaaaaaaaaaaa --></a>
  <a href="http://example.com/lacie" class="sister" id='link2'><!--Lacie --></a> and
  <p>这一段语句是测试编码</p>
  <a href="http://example.com/tillie" class="sister" id='link3'>Tillie</a>;
  and they lived at the bottom of a well .</p>
  <p class="story">...</p>

html = etree.HTML(html_str)
result = etree.tostring(html)
print(result)
'''
#html = etree.parse('index.html')
#result= etree.tostring(html,pretty_print=True)
#print(result)
html = etree.HTML(html_str)
urls = html.xpath(".//*[@class='sister']/@href")  #需要熟悉 构造XPath 表达式
print urls

#HTML 解析要熟悉 正则 Beautiful Soup  XPath 灵活运用  还需要 Firebug   FirePath  Match Tracer 的配合使用