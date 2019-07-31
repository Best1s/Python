#-*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import json
'''
url = 'http://seputu.com'
user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
headers = {'User-Agent':user_agent}
r = requests.get(url,headers)
with open ('index.html','w+') as f:
  f.write(r.text.encode('utf8'))
'''
content = []
soup = BeautifulSoup(open('index.html'),"html.parser",from_encoding='utf-8')  #html .parser
for mulu in soup.find_all(class_='mulu'):
  h2 = mulu.find('h2')
  if h2 != None:
    h2_title = h2.string.encode('utf-8')  #获取标题
    print h2_title
    list = []
    for a in mulu.find(class_='box').find_all('a'):  #获取所有a标记中的url 和章节
      box_title = a.string.encode('utf-8')
      href = a.get('href').encode('utf-8')
      #box_title = a.get('title')
      #print href,box_title
      list.append({'box_title':box_title,'href':href})
    content.append({'title':h2_title,'content':list})
    #content.append(list)
    #content.append()
with open('test.json','w') as fp:
  json.dump(content,fp=fp,indent=4,ensure_ascii=False)
'''

json方法
在使用之前 我们要了解两个名字 序列化和反序列化

序列化encoding : 把一个Python对象转化成json字符串
反序列化decoding: 把json字符串转化成python
常用的方法：
json.dumps():将一个Python数据类型转换为json数据类型
json.loads()：将json数据类型转换为python数据类型
json.dump()：将数据以json的数据类型写入文件中
json.load() ： 以json数据类型的方式读取文件


---------------------------------------------------------------------------------------------------

#dumps dump 函数原型
dumps(obj,skipkeys=False,ensure_ascii=True,check_circular=True,allow_nan=True,
      cls=None,indent=None,separators=None,encoding='urf-8',default=None,sort_kets=False,**kw):

dump(obj,fp,skipkeys=False,ensure_ascii=True,check_circular=True,allow_nan=True,
     cls=None,indent=None,separators=None,encoding='urf-8',default=None,sort_kets=False,**kw):

skipkeys: 如果dict的keys内的数据不是python的基本类型(str,unicode,int,long,float,bool,None)，设置为False时，就会报TypeError的错误。此时设置成True，则会跳过这类key 

ensure_ascii: 当它为True的时候，所有非ASCII码字符显示为\uXXXX序列，只需在dump时将ensure_ascii设置为False即可，此时存入json的中文即可正常显示

indent：应该是一个非负的整型，如果是0或空 就是顶格分行显示，如果为空就是一行最紧凑显示，否则会换行且按照indent的数值显示前面的空白分行显示，这样打印出来的json数据也叫pretty-printed json 

separators：分隔符，实际上是(item_separator, dict_separator)的一个元组，默认的就是(‘,’,’:’)；这表示dictionary内keys之间用“,”隔开，而KEY和value之间用“：”隔开。 

encoding: 默认是UTF-8 编码，设置JSON数据编码方式，处理中文时一定要注意

sort_keys：将数据根据keys的值进行排序。 

Serialize obj as a JSON formatted stream to fp (a.write()-supporting file-like object).


---------------------------------------------------------------------------------------------------
#load  和loads 函数原型 解码

load(fp, cls=None, object_hook=None, parse_float=None,
      parse_int=None, parse_constant=None, object_pairs_hook=None, **kw):

loads(s, encoding=None, cls=None, object_hook=None, parse_float=None,
      parse_int=None, parse_constant=None, object_pairs_hook=None, **kw):

encoding:指定编码格式。
parse_float: 如果指定，将把每一个JSON字符串按照float解码调用 ，默认情况下相当于float(num_str)
parse_int: 如果指定，将把每一个JSON字符串按照int解码调用 ，默认情况下相当于int(num_str)
'''
