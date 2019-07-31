#-*- coding: utf-8 -*-
import re
from bs4 import element
from bs4 import BeautifulSoup #bs4库将任何读入的html文件或字符串都转换为utf-8编码
#soup = BeautifulSoup(html_str,'lxml',from_encoding='utf-8')  #创建BeautifulSoup 对象
#soup = BeautifulSoup(open('index.html'),'lxml')   #lxml 第三方html解析库  python内置 是html.parser
soup = BeautifulSoup(open('index.html'),"html.parser",from_encoding='utf-8')
#print soup.prettify() #方法prettfy()来实现格式化输出

'''
BeautifulSoup 将html文档转化为 复杂的树形结构，所有对象可分为4种
Tag：与原生文档的tag相同  Tag有两个重要属性 name和attributes  每个Tag都有自己的名字 soup.name  还可以修改name  attrs可直接获取class 属性
NavigableString： 获取tag字符串
BeautifulSoup：表示文档的全部对象
Comment：注释掉的内容类型可以判断下 string是否为Comment
'''
print "--------------------------"*(6) 
'''
print soup.title #抽取title
print soup.title.name #抽取title tag name

print soup.p
print soup.p.string   #获取tag内容
print type(soup.p.string)

print soup.a
print soup.a["href"]
print soup.a.get('href')
soup.a["href"] = "myhref"  #更改href 属性
print soup.a.attrs
print soup.a.string
print type(soup.a.string)
if type(soup.a.string) == element.Comment: #  bs4.element.Comment
  print soup.a.string
"""
遍历文档树
子节点：  Tag中的.contents 和 .children 重要。Tag的.contents 属性可以将Tag子节点以列表方式输出  字符串没有contents属性
"""
print soup.head
print soup.head.contents
print len(soup.head.contents)
print soup.head.contents[0]
print soup.head.contents[0].string
print "-"*(88)
for child in soup.head.descendants:  #.descendants属性可对所有tag的子孙节点进行递归循环
  print child
print "-"*(88)
print soup.html.contents
print len(soup.html.contents)
print soup.html.contents[2]
print soup.html.contents[2].string
print soup.html.body.p.contents[0].string
print "for begin"+"-"*(88)
for child in soup.html.descendants:
  print child
print "for end" + "-"*(88)  '''
#获取子节点的内容 涉及三个属性 .string .strings .stripped_strings   string会获取注释内容  get_text() 不会回去注释内容
#.string  如果一个标记里没有标记 会返回最里面的内容 如果有唯一的一个标记也会返回，如果Tag包含多个子节点 .string 会输出None
print soup.head.string
print soup.title.string
print soup.html.string
#.strings 用于Tag中多个包含字符串情况，可进行循环遍历
for string in soup.strings:
  print repr(string) #repr() 函数将对象转化为供解释器读取的形式。
print "-"*(90)
#.stripped_strings属性可以去掉字符串中包含的空格和空行
for string in soup.stripped_strings:
  print repr(string)
print "-"*(90)
#父节点 通过.parent 属性来获取某个元素的父节点
print soup.title
print soup.title.parent
print "-"*(90)
#T通过.parents 属性可递归得到所有父辈节点
print soup.a
for parent in soup.a.parents:
  if parent is None:
    print parent
  else:
    print parent.name
print "-"*(90)
#兄弟节点
print soup.p.next_sibling
print soup.p.prev_sibling  # 等于  previous_siblings
print soup.p.next_sibling.next_sibling  
print "-"*(90)
for sibling in soup.a.next_siblings: #通过.next_sibling和.previous_siblings 属性可对当前兄弟节点迭代输出
  print repr(sibling)
print "-"*(90)
#前后节点
#前后节点要使用 .next_element  .previous_element 这两个属性  与.next_sibling和.previous_siblings 不同是针对所有节点
#不分层次 例如 <head><title>The Dormouse's story</title></head>中下一个节点就是 title;
print soup.head
print soup.head.next_element
print soup.title.previous_element
#遍历前后节点 可通过.next_element 和 .previous_element 的迭代器
#for element in soup.a.next_element:
#  print repr(element)
print "-"*(90)
'''#搜索文档书  核心  find_all()方法
原型： findAll(name, attrs, recursive, text, limit, **kwargs)   如果设置 recursive = False 搜索直接节点
name  查找名字为name的标记 字符串对象会自动忽略 name参数值可以为 字符串，正则表达式，列表,True 和方法
最简单过滤是字符串 bs 会查找与字符串完全匹配的内容
(findAll和 find)仅对Tag对象以及，顶层剖析对象有效
'''
print soup.find_all('b') #查找所有<b>的标记
print soup.find_all('a')
for href  in soup.find_all('a'):
  print href
for tag in soup.find_all(re.compile("^b")):
  print tag
  print tag.name
print "-"*(90)
print soup.find_all(['a','b']) #如果传入列表 将匹配列表中任一元素内容返回
print
for tag in soup.find_all(True): #如果传入True 可以匹配任何值，但不会返回字符串节点
  #print tag
  print tag.name
print soup.find_all('a')
#for i in soup.find_all('a',{'class':'sister'}):
for i in soup.find_all('a'):
  #b = i.find('a',arrtrs = {"class":"sister"}).gettext()
  print i
  print i.get('href')   #通过get函数获得标签的属性,对其他的标签也是同样可用的，并且输出的结果为文档中第一个匹配的对象，如果要搜索其他的标签需要使用find findAll函数。
  #print i.string
print "-"*(90)
#print soup.find_all('a',attrs={'class':'sister','id':'link2'}).get('href')  #利用标签的多个属性值进行搜索  findall 返回类型是列表  不能直接获取tag 内容。
#对搜索结果的个数进行限制： limit=n
#BeautifulSoup中的find和findAll用法相同，不同之处为find返回的是findAll搜索值的第一个值。
'''
pid = soup.find(href=re.compile("^http:")) #使用re正则匹配 后面有讲
p1=soup.p.get_text()
The Dormouse's story
  '''

#过滤器定义
def hasClass_Id(tag):
    return tag.has_attr('class') and tag.has_attr('id')  #匹配属性，返回ture  或 false
print soup.find_all(hasClass_Id)
#如果要查找class 因为是python关键字 需要加下划线
print soup.find_all(class_='sister')
print soup.find(class_='sister') 

'''
搜索函数原型

find_all(name, attrs, recursive, text, limit, **kwargs)         #fand_all返回列表  两个都是搜索当前节点，子孙节点等
find(name, attrs, recursive, text, limit, **kwargs)             #find返回第一个值

find_parents(name, attrs, recursive, text, limit, **kwargs)     #返回所有符合条件后面的兄弟节点
find_parent(name, attrs, recursive, text, limit, **kwargs)      #返回后面第一个tag节点

#通过 .next_siblings属性
find_next_siblings(name, attrs, recursive, text, limit, **kwargs)#返回所有符合条件前面的兄弟节点
find_next_sibling(name, attrs, recursive, text, limit, **kwargs) ##返回前面第一个tag节点

#通过 .next_elements属性
find_all_next(name, attrs, recursive, text, limit, **kwargs)    #对当前tag之后的tag哥字符串进行迭送 返回所有符合节点
find_next(name, attrs, recursive, text, limit, **kwargs)        #返回第一个

#通过 .previous_elements属性
find_all_previous(name, attrs, recursive, text, limit, **kwargs)#对当前tag之前的tag哥字符串进行迭送 返回所有符合节点
find_previous(name, attrs, recursive, text, limit, **kwargs)    #返回第一个


'''