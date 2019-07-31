#-*- coding: utf-8 -*-
import requests
from lxml import etree
import csv
import re

'''
#CSV 写入 需要创建weiter 对象

#CSV （Comma-Separated Values,逗号分割值,也称字符分割值）
headers = ['ID','UserName','Password','Age','Country']
rows = [(1001,'qiye','qiye_pass',24,'China'),     
        (1002,'Mary','Mary_pass',20,'USA'),
        (1003,'Jack','Jack_pass',20,'USA')
       ]
with open ('qiye.csv','w') as f:
  f_csv = csv.writer(f)
  f_csv.writerow(headers)
  f_csv.writerows(rows)


#rows 列表中的数据元组 也可以是字典数据

headers = ['ID','UserName','Password','Age','Country']
rows = [{'ID':1001,'UserName':'qiye','Password':'qiye_pass','Age':24,'Country':'China'},     
        {'ID':1002,'UserName':'Mary','Password':'Mary_pass','Age':20,'Country':'USA'},
        {'ID':1003,'UserName':'Jack','Password':'Jack_pass','Age':20,'Country':'USA'}
       ]
with open ('qiye1.csv','w') as f:
  f_csv = csv.DictWriter(f,headers)
  f_csv.writeheader()
  f_csv.writerows(rows)

'''
'''
#CSV 读取  需要创建reader 对象

with open('qiye.csv') as f:
  f_csv = csv.reader(f)
  headers = next(f_csv)
  print headers
  for row in f_csv:
    print row


#命名元组  使用索引访问数据

from collections import namedtuple
#import csv
with open('qiye.csv') as f:
  f_csv = csv.reader(f)
  headings = next(f_csv)
  Row = namedtuple('Row',headings)
  for r in f_csv:
    row = Row(*r)
    print row.UserName,row.Password   #可直接通过row.Date等获取相应的元素。
    print row

'''
'''
#另一种是读取到字典序列中

#import csv
with open('qiye.csv') as f:
  f_csv = csv.DictReader(f)
  for row in f_csv:
    print row.get('UserName'),row.get('Password')

'''
'''
url = 'http://seputu.com'
user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
headers = {'User-Agent':user_agent}
r = requests.get(url,headers)
with open ('index.html','w+') as f:
  f.write(r.text.encode('utf8'))
'''
#html = etree.HTML('index.html')
'''
lxml.etree.XMLSyntaxError: Opening and ending tag mismatch: meta line 3 and head, line 3, column 87

解决办法：
自己创建html解析器，增加parser参数

from lxml import etree
parser = etree.HTMLParser(encoding="utf-8")
htmlelement = etree.parse("baidu.html", parser=parser)
print(etree.tostring(htmlelement, encoding="utf-8").decode("utf-8")）

html = etree.HTML(html_str)
result = etree.tostring(html)
print(result)
'''

url = 'http://seputu.com'
user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
headers = {'User-Agent':user_agent}
r = requests.get(url,headers)
html = etree.HTML(r.text)

'''
#解析内容 标题 链接，章节等数据
for div_mulu in div_mulus:
  div_h2 =div_mulu.xpath('./div[@class="mulu-title"]/center/h2/text()')
  if len(div_h2) > 0:
    h2_title = div_h2[0]
    a_s = div_mulu.xpath('./div[@class="box"]/ul/li/a')
    for a in a_s:
      href = a.xpath('./@href')[0] #找到href 属性
      box_title = a.xpath('./@titele')[0].encode('utf-8')  #找到title属性


#小标题时间和内容分离
pattern = re.compile(r'\s*\[(.*)\]\s+(.*)')
match = pattern.search(box_title)
if match != None:
  date = match.group(1)
  real_title = match.group(2)
'''

div_mulus = html.xpath('.//*[@class="mulu"]')  #找到所有div class=mulu的标记
#pattern = re.compile(r'\s*\[(.*)\]\s+(.*)')
rows = []
for div_mulu in div_mulus:
  div_h2 =div_mulu.xpath('./div[@class="mulu-title"]/center/h2/text()')
  #print len(div_h2)
  if len(div_h2) > 0:
    h2_title = div_h2[0].encode('utf-8')
    a_s = div_mulu.xpath('./div[@class="box"]/ul/li/a')    
    for a in a_s:
      href = a.xpath('./@href')[0].encode('utf-8')
      box_title = a.xpath('./@title')[0]
      pattern = re.compile(r'\s*\[(.*)\]\s+(.*)')
      match = pattern.search(box_title)  #没有匹配成功的re.search（）返回None
      if match != None:
        date = match.group(1).encode('utf-8')    #group[0] 返整体  group[1] 返回匹配pattern第一部分
        real_title = match.group(2).encode('utf-8') 
        content = (h2_title,real_title,href,date)
        #print content
        rows.append(content)

#将获取的数据按照 title,real_title,href,date 的格式写入CSV
headers = ['title','real_title','href','date']
with open ('test.csv','w') as f:
  f_csv = csv.writer(f,)
  f_csv.writerow(headers)
  f_csv.writerows(rows)